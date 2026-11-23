"""Automatic collection must preserve user intent, privacy and main-thread storage."""

import json
import time
from threading import Event

import pytest

from intentaware.activity.models import ActivitySnapshot, CaptureResult
from intentaware.activity.monitor import TaskMonitor
from intentaware.contracts import Goal
from intentaware.memory.store import SQLiteStore
from intentaware.session import DesktopSession


class Clock:
    value = 0.0

    def __call__(self):
        return self.value


class Observer:
    def __init__(self):
        self.result = CaptureResult(ActivitySnapshot("Code.exe", "train.py - IntentAware - Visual Studio Code"))
        self.calls = 0

    def capture(self):
        self.calls += 1
        return self.result


@pytest.fixture
def setup_monitor(tmp_path):
    sessions, monitors = [], []

    def create(*, observer=None, stable_seconds=0, clock=None, **kwargs):
        session = DesktopSession(SQLiteStore(tmp_path / f"data-{len(sessions)}.sqlite3"))
        observer = observer or Observer()
        monitor = TaskMonitor(session, observer, stable_seconds=stable_seconds,
                              interval_seconds=0, clock=clock or time.monotonic, **kwargs)
        sessions.append(session)
        monitors.append(monitor)
        return session, monitor, observer

    yield create
    for monitor in monitors:
        monitor.close()
    for session in sessions:
        session.close()


def until(session, monitor, predicate):
    deadline = time.monotonic() + 2
    while not predicate() and time.monotonic() < deadline:
        session.poll()
        monitor.poll()
        time.sleep(0.002)
    assert predicate(), "automatic pipeline did not reach expected state"


def test_initial_task_and_activity_need_no_form_submission(setup_monitor):
    session, monitor, _ = setup_monitor()
    until(session, monitor, lambda: session.goal is not None and session.classification is not None)
    assert "IntentAware" in session.goal.title
    assert monitor.activity_text
    assert session.progress.note == ""  # Observing a window is not proof of completed work.
    assert monitor.goal_origin == "automatic"
    assert session.classification_activity == monitor.activity_text
    observed = [e for e in session.events if e.name == "activity_observed"]
    assert len(observed) == 1
    assert "train.py" not in json.dumps([e.details for e in session.events])


def test_obvious_leisure_waits_for_work_before_creating_the_first_task(setup_monitor):
    observer = Observer()
    observer.result = CaptureResult(ActivitySnapshot("chrome.exe", "搞笑合集 - 抖音 - Google Chrome"))
    session, monitor, _ = setup_monitor(observer=observer)
    until(session, monitor, lambda: bool(monitor.activity_text))

    assert session.goal is None
    assert "搞笑合集" in monitor.activity_text

    observer.result = CaptureResult(ActivitySnapshot("Code.exe", "train.py - IntentAware - Visual Studio Code"))
    until(session, monitor, lambda: session.goal is not None)
    assert session.goal.title == "继续开发「IntentAware」"


def test_corrected_legacy_automatic_task_keeps_its_source_after_reopening(tmp_path):
    path = tmp_path / "previous.sqlite3"
    store = SQLiteStore(path)
    store.save_goal(Goal("继续开发「IntentAware」", "处理 train.py"))
    store.set_setting("goal_origin", "automatic")

    session = DesktopSession(store)
    try:
        session.set_goal("完成训练模块", "用小数据集验证")
    finally:
        session.close()

    session = DesktopSession(SQLiteStore(path))
    monitor = TaskMonitor(session, Observer(), stable_seconds=0, interval_seconds=0)
    try:
        until(session, monitor, lambda: monitor.suggestion is not None)
        assert session.goal.title == "完成训练模块"
        assert monitor.switch_suggestion is None
        assert "IntentAware" not in json.dumps([event.details for event in session.events])
    finally:
        monitor.close()
        session.close()


def test_stability_filters_brief_window_switches(setup_monitor):
    clock = Clock()
    session, monitor, observer = setup_monitor(stable_seconds=3, clock=clock)
    until(session, monitor, lambda: monitor.state == "sampling")
    assert session.goal is None
    observer.result = CaptureResult(ActivitySnapshot("chrome.exe", "New Tab - Google Chrome"))
    clock.value = 2
    until(session, monitor, lambda: monitor.snapshot and "New Tab" in monitor.snapshot.window_title)
    clock.value = 10
    for _ in range(10):
        session.poll()
        monitor.poll()
        time.sleep(0.002)
    assert session.goal is None


def test_activity_switch_never_silently_replaces_main_goal(setup_monitor):
    session, monitor, observer = setup_monitor()
    until(session, monitor, lambda: session.goal is not None and not session.analysis_pending)
    original = session.goal
    session.add_detour("保留这条记录")
    observer.result = CaptureResult(ActivitySnapshot("WINWORD.EXE", "Group14 Proposal.docx - Word"))
    until(session, monitor, lambda: monitor.suggestion and "Proposal" in monitor.suggestion.title and not session.analysis_pending)
    assert session.goal == original
    monitor.adopt_suggestion()
    assert session.goal.id != original.id
    assert "Proposal" in session.goal.title
    assert session.detours == []
    assert session.store.list_detours(original.id)[0].text == "保留这条记录"


def test_correction_survives_more_observations(setup_monitor):
    session, monitor, observer = setup_monitor()
    until(session, monitor, lambda: session.goal is not None and not session.analysis_pending)
    monitor.correct_task("完成 NLP 小组项目", "实现自动任务识别", "已经搭好框架")
    observer.result = CaptureResult(ActivitySnapshot("chrome.exe", "Python documentation - Google Chrome"))
    until(session, monitor, lambda: monitor.suggestion and "Python" in monitor.suggestion.title)
    assert session.goal.title == "完成 NLP 小组项目"
    assert session.progress.note == "已经搭好框架"
    assert monitor.goal_origin == "manual"


def test_pause_drops_late_capture_and_persists(setup_monitor):
    entered, release = Event(), Event()

    class BlockingObserver(Observer):
        def capture(self):
            entered.set()
            release.wait(2)
            return super().capture()

    session, monitor, observer = setup_monitor(observer=BlockingObserver())
    monitor.poll()
    assert entered.wait(1)
    monitor.pause()
    release.set()
    for _ in range(10):
        monitor.poll()
        time.sleep(0.002)
    assert session.goal is None
    assert monitor.snapshot is None
    assert monitor.state == "paused"
    assert session.store.get_setting("activity_monitor.enabled") is False
    monitor.resume()
    until(session, monitor, lambda: session.goal is not None)


def test_exclusion_drops_current_data_and_blocks_future_capture(setup_monitor):
    session, monitor, _ = setup_monitor()
    until(session, monitor, lambda: session.goal is not None)
    saved = session.goal
    monitor.exclude_current_app()
    until(session, monitor, lambda: monitor.state == "excluded")
    assert monitor.snapshot is None
    assert monitor.suggestion is None
    assert monitor.activity_text == ""
    assert session.goal == saved
    assert "code" in monitor.excluded_apps
    assert session.store.get_setting("activity_monitor.excluded_apps") == ["code"]


def test_private_injected_capture_is_also_filtered(setup_monitor):
    observer = Observer()
    observer.result = CaptureResult(ActivitySnapshot("chrome.exe", "Private notes - Incognito - Google Chrome"))
    session, monitor, _ = setup_monitor(observer=observer)
    until(session, monitor, lambda: monitor.state == "excluded")
    assert session.goal is None
    assert monitor.snapshot is None
    assert "Private notes" not in json.dumps([e.details for e in session.events])


def test_unavailable_capture_and_self_focus_keep_app_usable(setup_monitor):
    session, monitor, observer = setup_monitor()
    until(session, monitor, lambda: session.goal is not None and not session.analysis_pending)
    current = monitor.snapshot
    observer.result = CaptureResult(None, "idle", "正在使用 IntentAware，显示最近一次识别的活动。")
    until(session, monitor, lambda: monitor.state == "idle")
    assert monitor.snapshot == current
    observer.result = CaptureResult(None, "unavailable", "当前系统不支持前台窗口识别。")
    until(session, monitor, lambda: monitor.state == "unavailable")
    assert monitor.snapshot is None
    assert session.goal is not None
    monitor.correct_task("手动修正后仍可使用", "继续编写")
    assert session.goal.title == "手动修正后仍可使用"


def test_paused_preference_and_exclusions_survive_restart(tmp_path):
    path = tmp_path / "settings.sqlite3"
    session = DesktopSession(SQLiteStore(path))
    monitor = TaskMonitor(session, Observer())
    monitor.set_excluded_apps(["Code.exe", "code", " chrome.exe "])
    monitor.pause()
    monitor.close()
    session.close()
    session = DesktopSession(SQLiteStore(path))
    monitor = TaskMonitor(session, Observer())
    try:
        assert monitor.enabled is False
        assert monitor.state == "paused"
        assert set(monitor.excluded_apps) == {"code", "chrome"}
    finally:
        monitor.close()
        session.close()


def test_return_to_previous_window_during_sampling_restores_activity(setup_monitor):
    clock = Clock()
    session, monitor, observer = setup_monitor(clock=clock, stable_seconds=3)
    original = observer.result
    until(session, monitor, lambda: monitor.state == "sampling")
    clock.value = 4
    until(session, monitor, lambda: session.goal is not None and session.classification is not None)
    original_activity = monitor.activity_text
    observer.result = CaptureResult(ActivitySnapshot("WINWORD.EXE", "Another project.docx - Word"))
    until(session, monitor, lambda: monitor.state == "sampling")
    assert monitor.activity_text == ""
    observer.result = original
    until(session, monitor, lambda: monitor.state == "watching" and monitor.activity_text == original_activity)
    assert monitor.snapshot.key == original.snapshot.key
    assert monitor.suggestion.source_key == original.snapshot.key
    until(session, monitor, lambda: session.classification is not None and not session.analysis_pending)
    assert session.classification_activity == original_activity


def test_close_discards_pending_capture_without_late_db_access(setup_monitor):
    entered, release = Event(), Event()

    class BlockingObserver(Observer):
        def capture(self):
            entered.set()
            release.wait(2)
            return super().capture()

    session, monitor, _ = setup_monitor(observer=BlockingObserver())
    monitor.poll()
    assert entered.wait(1)
    monitor.close()
    session.close()
    release.set()
    assert monitor.poll() is False
    assert session.goal is None


def test_explicit_analysis_after_correction_is_not_replaced_by_same_window(setup_monitor):
    session, monitor, observer = setup_monitor()
    until(session, monitor, lambda: session.goal is not None and session.classification is not None)
    monitor.correct_task("完成论文初稿", "整理实验结果")
    manual = "顺便刷短视频"
    monitor.analyze_manual(manual)
    until(session, monitor, lambda: session.classification_activity == manual)
    for _ in range(20):
        session.poll()
        monitor.poll()
        time.sleep(0.002)
    assert session.classification_activity == manual
    assert not session.analysis_pending
    observer.result = CaptureResult(ActivitySnapshot("WINWORD.EXE", "研究报告.docx - Word"))
    until(session, monitor, lambda: session.classification_activity and session.classification_activity != manual)
    assert "研究报告" in session.classification_activity
