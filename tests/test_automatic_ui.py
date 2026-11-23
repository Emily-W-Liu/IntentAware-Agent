"""Automatic desktop interactions with the real monitor and a controlled OS boundary."""

import time

import pytest
from PySide6.QtTest import QTest
from PySide6.QtWidgets import QApplication

from intentaware.activity.models import ActivitySnapshot, CaptureResult
from intentaware.activity.monitor import TaskMonitor
from intentaware.memory.store import SQLiteStore
from intentaware.nlp.local import LocalActivityClassifier
from intentaware.session import DesktopSession
from intentaware.ui import MainWindow


class WindowObserver:
    def __init__(self):
        self.result = CaptureResult(ActivitySnapshot("Microsoft Word", "研究报告.docx - Microsoft Word"))

    def capture(self):
        return self.result

    def observe(self, app_name, title):
        self.result = CaptureResult(ActivitySnapshot(app_name, title))


def wait_until(predicate):
    deadline = time.monotonic() + 3
    while not predicate() and time.monotonic() < deadline:
        QTest.qWait(20)
    assert predicate(), "automatic state did not reach the Qt workbench"


def observe(window, monitor, title, app_name="Microsoft Word"):
    monitor.observer.observe(app_name, title)
    wait_until(lambda: monitor.snapshot is not None and monitor.snapshot.window_title == title
               and bool(monitor.activity_text) and not window.session.analysis_pending)


@pytest.fixture(scope="module")
def app():
    return QApplication.instance() or QApplication(["automatic-ui", "-platform", "offscreen"])


@pytest.fixture
def automatic_window(app, tmp_path):
    session = DesktopSession(SQLiteStore(tmp_path / "automatic-ui.sqlite3"), classifier=LocalActivityClassifier())
    monitor = TaskMonitor(session, WindowObserver(), stable_seconds=0, interval_seconds=0.02)
    window = MainWindow(session, monitor=monitor)
    window.show()
    wait_until(lambda: session.goal is not None and session.classification is not None and not session.analysis_pending)
    yield window, session, monitor
    window.close()


def test_observations_update_without_editing_or_analyze_click(automatic_window):
    window, session, monitor = automatic_window
    assert window.task_title.text() == "撰写「研究报告」"
    assert not window.correction_editor.isVisible()
    assert not window.manual_panel.isVisible()

    observe(window, monitor, "访谈记录.docx - Microsoft Word")

    assert "访谈记录.docx" in window.window_title_label.text()
    assert "Microsoft Word" in window.activity_source.text()
    assert session.goal.title == "撰写「研究报告」"


def test_polling_preserves_an_open_correction_draft(automatic_window):
    window, session, monitor = automatic_window
    window.correction_button.click()
    window.goal_input.setText("我正在写最终结论")
    window.next_step_input.setText("核对访谈结论")
    observe(window, monitor, "新的窗口标题.docx - Microsoft Word")

    assert window.goal_input.text() == "我正在写最终结论"
    window.save_goal_button.click()

    assert session.goal.title == "我正在写最终结论"
    assert session.goal.next_step == "核对访谈结论"
    assert window.task_title.text() == "我正在写最终结论"
    assert monitor.goal_origin == "manual"
    assert not window.correction_editor.isVisible()


def test_pause_hides_stale_activity_and_classification(automatic_window):
    window, session, monitor = automatic_window
    reason = session.classification.reason
    assert reason in window.classification_label.text()

    window.pause_button.click()

    assert monitor.state == "paused"
    assert "恢复" in window.pause_button.text()
    assert "暂停" in window.activity_label.text()
    assert reason not in window.classification_label.text()
    assert window.task_title.text() == "撰写「研究报告」"
    window.pause_button.click()
    wait_until(lambda: monitor.snapshot is not None)


def test_task_switch_requires_the_visible_adoption_action(automatic_window):
    window, session, monitor = automatic_window
    original_id = session.goal.id
    observe(window, monitor, "login.py - AccountPortal - Visual Studio Code", app_name="Code.exe")
    assert window.suggestion_card.isVisible()
    assert session.goal.title == "撰写「研究报告」"

    window.adopt_suggestion_button.click()

    assert session.goal.title == "继续开发「AccountPortal」"
    assert session.goal.id != original_id
    assert not window.suggestion_card.isVisible()


def test_corrected_task_does_not_offer_its_original_title_as_a_switch(automatic_window):
    window, session, monitor = automatic_window
    previous = session.goal.id
    window.correction_button.click()
    window.goal_input.setText("完成研究报告的方法章节")
    window.save_goal_button.click()

    assert session.goal.id == previous
    assert not window.suggestion_card.isVisible()
    observe(window, monitor, "访谈记录.docx - Microsoft Word")
    assert window.suggestion_card.isVisible()
    observe(window, monitor, "研究报告.docx - Microsoft Word")
    assert not window.suggestion_card.isVisible()


def test_cancel_correction_restores_the_suggestion_actions(automatic_window):
    window, _, monitor = automatic_window
    window.correction_button.click()
    observe(window, monitor, "访谈记录.docx - Microsoft Word")
    assert not window.suggestion_card.isVisible()

    window.cancel_correction_button.click()

    assert window.suggestion_card.isVisible()
    assert window.adopt_suggestion_button.isEnabled()


def test_dismissed_suggestion_stays_hidden_for_other_files_in_the_same_project(automatic_window):
    window, session, monitor = automatic_window
    original = session.goal
    observe(window, monitor, "login.py - AccountPortal - Visual Studio Code", app_name="Code.exe")
    assert window.suggestion_card.isVisible()
    window.dismiss_suggestion_button.click()

    assert session.goal == original
    assert not window.suggestion_card.isVisible()
    observe(window, monitor, "tests.py - AccountPortal - Visual Studio Code", app_name="Code.exe")
    assert not window.suggestion_card.isVisible()
    observe(window, monitor, "readme.py - NewProject - Visual Studio Code", app_name="Code.exe")
    assert window.suggestion_card.isVisible()


def test_excluding_current_app_updates_settings_and_clears_activity(automatic_window):
    window, session, monitor = automatic_window
    window.settings_nav.click()
    window.exclude_current_button.click()

    assert monitor.excluded_apps == ["microsoft word"]
    assert "microsoft word" in window.excluded_apps_input.toPlainText()
    assert "排除" in window.monitor_status.text()
    assert session.goal.title == "撰写「研究报告」"
    assert monitor.snapshot is None


def test_manual_analysis_stays_usable_while_automatic_capture_is_paused(automatic_window):
    window, session, monitor = automatic_window
    window.pause_button.click()
    window.manual_toggle.click()
    window.activity_input.setPlainText("顺便浏览了一些演示文稿模板")
    window.analyze_button.click()
    wait_until(lambda: session.classification is not None and not session.analysis_pending)

    assert "手动补充" in window.classification_label.text()
    assert session.classification.reason in window.classification_label.text()
    assert monitor.state == "paused"


def test_low_signal_window_does_not_offer_an_empty_task_switch(automatic_window):
    window, session, monitor = automatic_window
    observe(window, monitor, "新标签页 - Google Chrome", app_name="chrome.exe")

    assert not window.suggestion_card.isVisible()
    assert session.goal.title == "撰写「研究报告」"
    assert "需要确认" in window.confidence_label.text()


def test_closing_window_stops_observation_application(automatic_window):
    window, _, monitor = automatic_window
    previous = monitor.snapshot
    window.close()
    monitor.observer.observe("Code.exe", "other.py - OtherProject - Visual Studio Code")
    for _ in range(3):
        assert monitor.poll() is False
        QTest.qWait(40)
    assert monitor.snapshot == previous
