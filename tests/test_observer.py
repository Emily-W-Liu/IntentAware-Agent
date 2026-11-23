import ctypes
import os
import subprocess
from types import SimpleNamespace

import pytest

from intentaware.activity import observer
from intentaware.activity.models import ActivitySnapshot


class NativeFunction:
    def __init__(self, function):
        self.function = function
        self.argtypes = None
        self.restype = None

    def __call__(self, *args):
        return self.function(*args)


def windows_api(*, title="main.py - Workbench - Visual Studio Code", app="Code.exe", pid=421,
                query_ok=True, open_ok=True):
    state = {"window": 2**40 + 17, "handle": 2**40 + 23, "closed": [], "titles": 0}

    def process_id(window, output):
        assert window == state["window"]
        output._obj.value = pid
        return 5

    def window_text(window, output, capacity):
        assert window == state["window"]
        state["titles"] += 1
        output.value = title[:capacity - 1]
        return len(output.value)

    def image_name(handle, flags, output, capacity):
        assert handle == state["handle"]
        assert flags == 0
        if not query_ok:
            return 0
        output.value = "C:\\Programs\\" + app
        capacity._obj.value = len(output.value)
        return 1

    user32 = SimpleNamespace(
        GetForegroundWindow=NativeFunction(lambda: state["window"]),
        GetWindowThreadProcessId=NativeFunction(process_id),
        GetWindowTextW=NativeFunction(window_text),
    )
    kernel32 = SimpleNamespace(
        OpenProcess=NativeFunction(lambda access, inherit, process: state["handle"] if open_ok else 0),
        QueryFullProcessImageNameW=NativeFunction(image_name),
        CloseHandle=NativeFunction(lambda handle: state["closed"].append(handle) or 1),
    )
    return user32, kernel32, state


def test_snapshot_key_survives_pid_and_time_changes_but_tracks_content():
    first = ActivitySnapshot("Code.exe", "main.py", 123, observed_at="first")
    later = ActivitySnapshot("Code.exe", "main.py", 456, observed_at="later")
    assert first.key == later.key
    assert first.key != ActivitySnapshot("Code.exe", "other.py").key
    assert ActivitySnapshot("a", "bc").key != ActivitySnapshot("ab", "c").key


def test_windows_captures_real_title_and_uses_pointer_sized_handle_signatures():
    user32, kernel32, state = windows_api()
    result = observer.WindowsForegroundObserver(user32=user32, kernel32=kernel32).capture()
    assert result.status == "ok"
    assert result.snapshot.app_name == "Code.exe"
    assert result.snapshot.window_title == "main.py - Workbench - Visual Studio Code"
    assert result.snapshot.process_id == 421
    assert result.snapshot.source == "window_title"
    assert ctypes.sizeof(user32.GetForegroundWindow.restype) == ctypes.sizeof(ctypes.c_void_p)
    assert ctypes.sizeof(kernel32.OpenProcess.restype) == ctypes.sizeof(ctypes.c_void_p)
    assert ctypes.sizeof(kernel32.CloseHandle.argtypes[0]) == ctypes.sizeof(ctypes.c_void_p)
    assert state["closed"] == [state["handle"]]


@pytest.mark.parametrize("query_ok, open_ok, closed_count", [(False, True, 1), (True, False, 0)])
def test_windows_failed_app_lookup_returns_no_title_and_closes_open_handle(query_ok, open_ok, closed_count):
    user32, kernel32, state = windows_api(query_ok=query_ok, open_ok=open_ok)
    result = observer.WindowsForegroundObserver(user32=user32, kernel32=kernel32).capture()
    assert result.status == "unavailable"
    assert result.snapshot is None
    assert state["titles"] == 0
    assert len(state["closed"]) == closed_count


def test_windows_own_window_is_idle_without_reading_title():
    user32, kernel32, state = windows_api(pid=os.getpid())
    result = observer.WindowsForegroundObserver(user32=user32, kernel32=kernel32).capture()
    assert result.status == "idle"
    assert result.snapshot is None
    assert state["titles"] == 0
    assert state["closed"] == []


def test_windows_password_manager_is_excluded_before_reading_title():
    user32, kernel32, state = windows_api(app="KeePassXC.exe", title="Secret account")
    result = observer.WindowsForegroundObserver(user32=user32, kernel32=kernel32).capture()
    assert result.status == "excluded"
    assert result.snapshot is None
    assert state["titles"] == 0


def test_windows_private_suffix_is_checked_before_display_title_is_shortened():
    user32, kernel32, state = windows_api(app="chrome.exe", title="x" * 600 + " - Incognito")
    result = observer.WindowsForegroundObserver(user32=user32, kernel32=kernel32).capture()
    assert result.status == "excluded"
    assert result.snapshot is None
    assert "x" * 20 not in result.message


def test_windows_long_title_is_bounded():
    user32, kernel32, state = windows_api(title="项目" * 400)
    result = observer.WindowsForegroundObserver(user32=user32, kernel32=kernel32).capture()
    assert result.status == "ok"
    assert 0 < len(result.snapshot.window_title) <= 512


def test_windows_title_that_fills_native_buffer_is_not_retained():
    user32, kernel32, state = windows_api(title="x" * 10000 + " - Incognito")
    result = observer.WindowsForegroundObserver(user32=user32, kernel32=kernel32).capture()
    assert result.snapshot is None
    assert result.status == "unavailable"


@pytest.mark.parametrize("app,title", [
    ("1Password.exe", "Vault"), ("org.keepassxc.KeePassXC", "Vault"),
    ("Bitwarden", "Vault"), ("chrome.exe", "Account - InPrivate"),
    ("firefox", "Shopping — Mozilla Firefox (Private Browsing)"),
    ("msedge.exe", "页面 - 无痕浏览"), ("brave.exe", "Page (Private)"),
])
def test_private_snapshots_are_excluded(app, title):
    assert observer.is_private_snapshot(ActivitySnapshot(app, title))


def test_regular_code_title_with_private_keyword_is_not_mistaken_for_private_browsing():
    assert not observer.is_private_snapshot(ActivitySnapshot("Code.exe", "private methods - tutorial - Visual Studio Code"))


def xprop_output(*, title='"研究计划.pdf"', app='"evince", "Evince"', pid="421"):
    return (f"_NET_WM_PID(CARDINAL) = {pid}\nWM_CLASS(STRING) = {app}\n"
            f"_NET_WM_NAME(UTF8_STRING) = {title}\nWM_NAME(STRING) = \"legacy\"\n")


def fake_xprop(monkeypatch, properties, *, after="0x4600007"):
    calls = []

    def run(command, **kwargs):
        calls.append(command)
        assert kwargs["timeout"] <= 1.0
        assert not kwargs.get("shell", False)
        assert "-len" in command
        if "-root" in command:
            window = "0x4600007" if len(calls) == 1 else after
            output = f"_NET_ACTIVE_WINDOW(WINDOW): window id # {window}\n"
        else:
            assert "0x4600007" in command
            output = properties
        return subprocess.CompletedProcess(command, 0, output, "")

    monkeypatch.setattr(observer.subprocess, "run", run)
    return calls


def test_x11_reads_utf8_title_and_window_class_with_bounded_queries(monkeypatch):
    calls = fake_xprop(monkeypatch, xprop_output())
    result = observer.X11ForegroundObserver("/usr/bin/xprop").capture()
    assert result.status == "ok"
    assert result.snapshot == ActivitySnapshot("Evince", "研究计划.pdf", 421, observed_at=result.snapshot.observed_at)
    assert len(calls) == 3


def test_x11_decodes_escaped_quotes_and_utf8_bytes(monkeypatch):
    fake_xprop(monkeypatch, xprop_output(title=r'"\344\270\255\346\226\207 \"draft\".pdf"'))
    result = observer.X11ForegroundObserver().capture()
    assert result.snapshot.window_title == '中文 "draft".pdf'


def test_x11_changed_foreground_is_not_reported_as_stable(monkeypatch):
    fake_xprop(monkeypatch, xprop_output(), after="0x4600008")
    result = observer.X11ForegroundObserver().capture()
    assert result.status == "idle"
    assert result.snapshot is None


def test_x11_missing_process_identity_is_unavailable(monkeypatch):
    fake_xprop(monkeypatch, xprop_output(pid="not found."))
    result = observer.X11ForegroundObserver().capture()
    assert result.status == "unavailable"
    assert result.snapshot is None


def test_x11_private_windows_return_no_title(monkeypatch):
    fake_xprop(monkeypatch, xprop_output(title='"Secret - Private Browsing"', app='"firefox", "Firefox"'))
    result = observer.X11ForegroundObserver().capture()
    assert result.status == "excluded"
    assert result.snapshot is None


def test_x11_timeout_is_reported_without_exposing_subprocess_output(monkeypatch):
    def timeout(command, **kwargs):
        raise subprocess.TimeoutExpired(command, kwargs["timeout"], output="sensitive title")

    monkeypatch.setattr(observer.subprocess, "run", timeout)
    result = observer.X11ForegroundObserver().capture()
    assert result.status == "unavailable"
    assert result.snapshot is None
    assert "sensitive" not in result.message


@pytest.mark.parametrize("platform,environment,expected", [
    ("darwin", {}, "macOS"),
    ("linux", {"WAYLAND_DISPLAY": "wayland-0", "DISPLAY": ":0"}, "Wayland"),
    ("linux", {"XDG_SESSION_TYPE": "wayland", "DISPLAY": ":0"}, "Wayland"),
    ("linux", {}, "X11"),
])
def test_factory_reports_unsupported_environments_without_fake_capture(monkeypatch, platform, environment, expected):
    monkeypatch.setattr(observer.sys, "platform", platform)
    for key in ("WAYLAND_DISPLAY", "DISPLAY", "XDG_SESSION_TYPE"):
        monkeypatch.delenv(key, raising=False)
    for key, value in environment.items():
        monkeypatch.setenv(key, value)
    result = observer.create_observer().capture()
    assert result.status == "unavailable"
    assert result.snapshot is None
    assert expected in result.message
