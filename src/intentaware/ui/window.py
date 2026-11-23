"""The Qt window reads session state and forwards user actions on the main thread."""

from collections.abc import Callable
from datetime import datetime
from html import escape
from sqlite3 import Error as SQLiteError
from typing import TYPE_CHECKING

from PySide6.QtCore import QSignalBlocker, Qt, QTimer
from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import (
    QAbstractScrollArea, QComboBox, QFileDialog, QFrame, QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPlainTextEdit, QPushButton, QScrollArea,
    QSizePolicy, QTabWidget, QVBoxLayout, QWidget,
)

from intentaware.contracts import ActivityLabel, Condition, DelegationJob, JobStatus

from .theme import apply_theme

if TYPE_CHECKING:
    from intentaware.session import DesktopSession


CONDITIONS = {
    Condition.G: "G · 目标提醒",
    Condition.P: "P · 支线暂存与任务恢复",
    Condition.I: "I · 委托完成后立即交付",
    Condition.D: "D · 委托在检查点交付",
}
CLASSIFICATIONS = {
    ActivityLabel.DIRECT_PROGRESS: "直接推进",
    ActivityLabel.NECESSARY_PREPARATION: "必要准备",
    ActivityLabel.OPTIONAL_EXPLORATION: "可选探索",
    ActivityLabel.UNCLEAR: "暂不明确",
}
ANALYSIS_HINT = "演示分类将在这里显示，并给出建议的下一步。"
RESUME_HINT = "恢复时将显示已保存的进度和下一步。"
JOB_STATES = {
    JobStatus.RUNNING: "处理中",
    JobStatus.READY: "待交付",
    JobStatus.DELIVERED: "已交付",
    JobStatus.FAILED: "失败",
    JobStatus.CANCELLED: "已取消",
}
EVENT_NAMES = {
    "session_started": "开始运行",
    "session_ended": "结束运行",
    "goal_saved": "保存目标",
    "analysis_requested": "开始分析活动",
    "activity_classified": "完成活动分析",
    "analysis_failed": "活动分析失败",
    "detour_saved": "暂存支线",
    "detour_removed": "移除支线",
    "resume_requested": "请求恢复任务",
    "delegation_submitted": "提交委托",
    "delegation_completed": "完成委托",
    "delegation_delivered": "交付答案",
    "delegation_failed": "委托失败",
    "delegation_cancelled": "取消委托",
    "checkpoint_reached": "到达检查点",
}
UI_ERRORS = (ValueError, RuntimeError, SQLiteError, OSError)
ROW_ID = Qt.ItemDataRole.UserRole


def _label(text: str = "", role: str = "") -> QLabel:
    label = QLabel(text)
    label.setTextFormat(Qt.TextFormat.PlainText)
    if role:
        label.setProperty("role", role)
    return label


def _field(layout: QVBoxLayout, caption: str, widget: QWidget) -> None:
    label = _label(caption)
    label.setBuddy(widget)
    widget.setAccessibleName(caption)
    layout.addWidget(label)
    layout.addWidget(widget)


def _button(text: str, on_click: Callable[[], None], *, primary: bool = False) -> QPushButton:
    button = QPushButton(text)
    button.setProperty("primary", primary)
    button.clicked.connect(on_click)
    return button


def _panel(title: str) -> tuple[QFrame, QVBoxLayout]:
    frame = QFrame()
    frame.setObjectName("panel")
    layout = QVBoxLayout(frame)
    layout.setContentsMargins(16, 14, 16, 16)
    layout.setSpacing(8)
    layout.addWidget(_label(title, "heading"))
    return frame, layout


def _fit_scrollable_view(widget: QAbstractScrollArea, minimum_height: int = 76) -> None:
    # The list or editor scrolls internally as its tab grows into the remaining space.
    widget.setMinimumHeight(minimum_height)
    widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Ignored)


def _selected_id(widget: QListWidget) -> str | None:
    item = widget.currentItem()
    return item.data(ROW_ID) if item else None


def _sync_rows(widget: QListWidget, rows: list[tuple[str, str]], select: str | None = None) -> None:
    selected = select or _selected_id(widget)
    old = [(widget.item(i).data(ROW_ID), widget.item(i).text()) for i in range(widget.count())]
    with QSignalBlocker(widget):
        if old != rows:
            widget.clear()
            for row_id, text in rows:
                item = QListWidgetItem(text)
                item.setData(ROW_ID, row_id)
                item.setToolTip(f"<p>{escape(text)}</p>")
                widget.addItem(item)
        if selected is not None:
            for i, (row_id, _) in enumerate(rows):
                if row_id == selected:
                    widget.setCurrentRow(i)
                    break


class MainWindow(QMainWindow):
    def __init__(self, session: "DesktopSession") -> None:
        super().__init__()
        self.session = session
        self._analyzed_activity: str | None = None
        self.setWindowTitle("IntentAware · 任务工作台")
        self.resize(1160, 800)
        self.setMinimumSize(900, 650)
        self._build()
        apply_theme(self)
        self._load_goal()
        self._refresh()
        self._status("当前目标已载入。" if session.goal else "保存目标后即可分析活动并记录进度。")
        self._timer = QTimer(self, interval=100)
        self._timer.timeout.connect(self._poll)
        self._timer.start()

    def _build(self) -> None:
        root = QWidget()
        root.setObjectName("workbench")
        layout = QVBoxLayout(root)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setCentralWidget(root)

        header = QFrame()
        header.setObjectName("header")
        header_row = QHBoxLayout(header)
        header_row.setContentsMargins(24, 13, 24, 13)
        header_row.setSpacing(13)
        brand = _label("IntentAware")
        brand.setObjectName("brand")
        title = _label("任务工作台")
        title.setObjectName("workbenchTitle")
        mode = _label("离线演示")
        mode.setObjectName("offlineMode")
        header_row.addWidget(brand)
        header_row.addWidget(title)
        header_row.addStretch()
        header_row.addWidget(mode)
        layout.addWidget(header)

        scroll = QScrollArea()
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        canvas = QWidget()
        canvas.setObjectName("workbench")
        columns = QHBoxLayout(canvas)
        columns.setContentsMargins(24, 20, 24, 20)
        columns.setSpacing(18)
        scroll.setWidget(canvas)
        layout.addWidget(scroll, 1)

        left, right = QVBoxLayout(), QVBoxLayout()
        left.setSpacing(14)
        right.setSpacing(14)
        columns.addLayout(left, 1)
        columns.addLayout(right, 2)
        self._build_goal(left)
        self._build_activity(right)
        self.workflow_tabs = QTabWidget()
        self.workflow_tabs.addTab(self._build_detours(), "支线与恢复")
        self.workflow_tabs.addTab(self._build_delegation(), "异步委托")
        self.workflow_tabs.addTab(self._build_events(), "运行事件")
        right.addWidget(self.workflow_tabs, 1)

        footer = QFrame()
        footer.setObjectName("footer")
        footer_row = QHBoxLayout(footer)
        footer_row.setContentsMargins(24, 8, 24, 8)
        self.status_label = _label()
        self.status_label.setObjectName("status_label")
        self.status_label.setAccessibleName("操作反馈")
        self.status_label.setWordWrap(True)
        self.status_label.setMinimumHeight(self.status_label.fontMetrics().height())
        footer_row.addWidget(self.status_label)
        layout.addWidget(footer)

    def _build_goal(self, left: QVBoxLayout) -> None:
        panel, layout = _panel("当前目标")
        self.goal_input = QLineEdit(placeholderText="例如：完成研究报告")
        self.next_step_input = QLineEdit(placeholderText="例如：整理方法章节")
        self.progress_input = QLineEdit(placeholderText="例如：已收集三篇论文")
        _field(layout, "目标名称", self.goal_input)
        _field(layout, "下一步", self.next_step_input)
        _field(layout, "已确认进度", self.progress_input)
        actions = QHBoxLayout()
        self.save_goal_button = _button("保存目标", self._save_goal, primary=True)
        self.sample_button = _button("填入示例", self._fill_sample)
        actions.addWidget(self.save_goal_button)
        actions.addWidget(self.sample_button)
        actions.addStretch()
        layout.addSpacing(4)
        layout.addLayout(actions)
        left.addWidget(panel)

        options, settings = _panel("实验设置")
        self.condition_combo = QComboBox()
        for condition, text in CONDITIONS.items():
            self.condition_combo.addItem(text, condition.value)
        self.condition_combo.currentIndexChanged.connect(self._change_condition)
        _field(settings, "实验条件", self.condition_combo)
        left.addWidget(options)
        left.addStretch()

    def _build_activity(self, right: QVBoxLayout) -> None:
        panel, layout = _panel("当前活动")
        self.activity_input = QPlainTextEdit(placeholderText="写下正在做什么，或粘贴一段相关内容。")
        self.activity_input.setFixedHeight(88)
        self.activity_input.textChanged.connect(self._refresh_classification)
        _field(layout, "活动描述", self.activity_input)
        actions = QHBoxLayout()
        self.analyze_button = _button("分析活动", self._analyze, primary=True)
        self.detour_button = _button("暂存为支线", self._add_detour)
        actions.addWidget(self.analyze_button)
        actions.addWidget(self.detour_button)
        actions.addStretch()
        layout.addLayout(actions)
        self.classification_label = _label(role="feedback")
        self.classification_label.setAccessibleName("活动分类结果")
        self.classification_label.setWordWrap(True)
        self.classification_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        layout.addWidget(self.classification_label)
        right.addWidget(panel)

    def _build_detours(self) -> QWidget:
        tab = QWidget()
        layout = QVBoxLayout(tab)
        self.detour_hint = _label(role="muted")
        layout.addWidget(self.detour_hint)
        self.detour_list = QListWidget(wordWrap=True)
        self.detour_list.setAccessibleName("已暂存支线")
        _fit_scrollable_view(self.detour_list)
        layout.addWidget(self.detour_list, 1)
        actions = QHBoxLayout()
        self.resume_button = _button("恢复任务", self._resume, primary=True)
        actions.addWidget(self.resume_button)
        actions.addStretch()
        layout.addLayout(actions)
        self.resume_label = _label(RESUME_HINT, "feedback")
        self.resume_label.setAccessibleName("任务恢复提示")
        self.resume_label.setWordWrap(True)
        self.resume_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        layout.addWidget(self.resume_label)
        return tab

    def _build_delegation(self) -> QWidget:
        tab = QWidget()
        layout = QVBoxLayout(tab)
        controls = QHBoxLayout()
        self.question_input = QLineEdit(placeholderText="例如：如何整理访谈资料？")
        self.question_input.returnPressed.connect(self._submit)
        form = QVBoxLayout()
        _field(form, "委托问题", self.question_input)
        controls.addLayout(form, 1)
        self.submit_button = _button("提交委托", self._submit, primary=True)
        controls.addWidget(self.submit_button, alignment=Qt.AlignmentFlag.AlignBottom)
        layout.addLayout(controls)
        self.job_list = QListWidget()
        self.job_list.setAccessibleName("委托列表")
        _fit_scrollable_view(self.job_list)
        self.job_list.setMaximumHeight(120)
        self.job_list.currentItemChanged.connect(self._refresh_job_result)
        layout.addWidget(self.job_list, 1)
        self.job_result = QPlainTextEdit(readOnly=True, placeholderText="选择一项委托查看状态或已交付的答案。")
        self.job_result.setAccessibleName("委托结果")
        _fit_scrollable_view(self.job_result, 82)
        layout.addWidget(self.job_result, 2)
        actions = QHBoxLayout()
        self.checkpoint_button = _button("到达检查点", self._checkpoint, primary=True)
        self.reveal_button = _button("提前查看", self._reveal)
        self.cancel_button = _button("取消委托", self._cancel)
        actions.addWidget(self.checkpoint_button)
        actions.addWidget(self.reveal_button)
        actions.addWidget(self.cancel_button)
        actions.addStretch()
        layout.addLayout(actions)
        return tab

    def _build_events(self) -> QWidget:
        tab = QWidget()
        layout = QVBoxLayout(tab)
        header = QHBoxLayout()
        header.addWidget(_label("本次运行 · UTC", "muted"))
        header.addStretch()
        self.export_button = _button("导出 JSONL", self._export)
        header.addWidget(self.export_button)
        layout.addLayout(header)
        self.event_list = QListWidget()
        self.event_list.setAccessibleName("本次运行事件")
        _fit_scrollable_view(self.event_list)
        layout.addWidget(self.event_list, 1)
        return tab

    def _load_goal(self) -> None:
        if self.session.goal:
            self.goal_input.setText(self.session.goal.title)
            self.next_step_input.setText(self.session.goal.next_step)
            self.progress_input.setText(self.session.progress.note if self.session.progress else "")

    def _status(self, text: str = "", *, error: bool = False) -> None:
        self.status_label.setText(text)
        self.status_label.setProperty("error", error)
        self.status_label.style().unpolish(self.status_label)
        self.status_label.style().polish(self.status_label)

    def _perform(self, action: Callable[[], str | None]) -> None:
        try:
            message = action()
            self._refresh()
        except UI_ERRORS as error:
            self._status(str(error), error=True)
        else:
            self._status(message or "")

    def _fill_sample(self) -> None:
        self.goal_input.setText("完成研究报告初稿")
        self.next_step_input.setText("整理三篇文献，写出方法章节的提纲")
        self.progress_input.setText("已确定研究问题，收集了三篇参考文献")
        self.activity_input.setPlainText("顺便浏览了一些演示文稿模板，想保存下来以后参考。")
        self.question_input.setText("被打断后，怎样更快地恢复当前任务？")
        self._status("已填入示例。点击“保存目标”后可尝试分析活动。")

    def _save_goal(self) -> None:
        def save() -> str:
            self.session.set_goal(self.goal_input.text(), self.next_step_input.text(), self.progress_input.text())
            self._load_goal()
            self._analyzed_activity = None
            self.resume_label.setText(RESUME_HINT)
            return "已保存当前目标和进度。"

        self._perform(save)

    def _change_condition(self) -> None:
        def change() -> str:
            condition = Condition(self.condition_combo.currentData())
            self.session.set_condition(condition)
            self._analyzed_activity = None
            self.resume_label.setText(RESUME_HINT)
            return f"已切换到 {condition.value} 条件。"

        self._perform(change)
        self._sync_condition()

    def _sync_condition(self) -> None:
        with QSignalBlocker(self.condition_combo):
            self.condition_combo.setCurrentIndex(self.condition_combo.findData(self.session.condition.value))

    def _analyze(self) -> None:
        def analyze() -> None:
            activity = self.activity_input.toPlainText().strip()
            self.session.start_analysis(activity)
            self._analyzed_activity = activity

        self._perform(analyze)

    def _add_detour(self) -> None:
        def add() -> str:
            self.session.add_detour(self.activity_input.toPlainText())
            self.workflow_tabs.setCurrentIndex(0)
            return "已将当前活动暂存为支线。"

        self._perform(add)

    def _resume(self) -> None:
        self._perform(lambda: self.resume_label.setText(self.session.resume()))

    def _submit(self) -> None:
        def submit() -> str:
            job = self.session.submit_delegation(self.question_input.text())
            self.question_input.clear()
            self.workflow_tabs.setCurrentIndex(1)
            self._refresh_jobs(job.id)
            return "已提交委托。"

        self._perform(submit)

    def _checkpoint(self) -> None:
        def checkpoint() -> str:
            count = self.session.checkpoint()
            return f"已记录检查点，交付了 {count} 项答案。"

        self._perform(checkpoint)

    def _reveal(self) -> None:
        if job_id := _selected_id(self.job_list):
            def reveal() -> str:
                self.session.reveal_job(job_id)
                return "已提前交付选中的答案。"

            self._perform(reveal)

    def _cancel(self) -> None:
        if job_id := _selected_id(self.job_list):
            self._perform(lambda: self.session.cancel_job(job_id))

    def _export(self) -> None:
        path, _ = QFileDialog.getSaveFileName(self, "导出本次运行事件", "intentaware-events.jsonl", "JSON Lines (*.jsonl)")
        if path:
            self._perform(lambda: f"已导出 {self.session.export_events(path)} 条运行事件。")

    def _refresh(self) -> None:
        memory = self.session.memory_enabled
        delegation = self.session.delegation_enabled
        pending = self.session.analysis_pending
        self._sync_condition()
        self.analyze_button.setEnabled(not pending)
        self.activity_input.setEnabled(not pending)
        self.sample_button.setEnabled(not pending)
        self.detour_button.setEnabled(memory and not pending)
        self.resume_button.setEnabled(memory)
        self.question_input.setEnabled(delegation)
        self.submit_button.setEnabled(delegation)
        self.checkpoint_button.setEnabled(delegation)
        current_tab = self.workflow_tabs.currentIndex()
        if (current_tab == 0 and not memory) or (current_tab == 1 and not delegation):
            self.workflow_tabs.setCurrentIndex(2)
        self.workflow_tabs.setTabEnabled(0, memory)
        self.workflow_tabs.setTabEnabled(1, delegation)
        self._refresh_classification()

        detours = self.session.detours if memory else []
        self.detour_hint.setText(f"已暂存 {len(detours)} 条支线" if detours else "暂无支线。可在上方暂存当前活动。")
        _sync_rows(self.detour_list, [(item.id, item.text) for item in detours])
        self._refresh_jobs()
        _sync_rows(self.event_list, [
            (event.id, f"{datetime.fromisoformat(event.occurred_at):%H:%M:%S}   {event.condition.value}   "
                       f"{EVENT_NAMES.get(event.name, event.name)}")
            for event in reversed(self.session.events)
        ])

    def _refresh_classification(self) -> None:
        text = ANALYSIS_HINT
        if self.session.analysis_pending:
            text = "正在分析活动…"
        elif self._analyzed_activity == self.activity_input.toPlainText().strip():
            if self.session.analysis_error:
                text = f"分析失败：{self.session.analysis_error}"
            elif result := self.session.classification:
                text = f"{CLASSIFICATIONS[result.label]} · 演示分类\n{result.reason}\n建议下一步：{result.suggested_next_step}"
        self.classification_label.setText(text)

    def _refresh_jobs(self, select: str | None = None) -> None:
        jobs = self.session.jobs if self.session.delegation_enabled else []
        _sync_rows(self.job_list, [(job.id, f"{JOB_STATES[job.status]}   {job.question}") for job in reversed(jobs)], select)
        self._refresh_job_result()

    def _refresh_job_result(self) -> None:
        selected = _selected_id(self.job_list)
        job = next((job for job in self.session.jobs if job.id == selected), None)
        ready = job is not None and job.status == JobStatus.READY
        running = job is not None and job.status == JobStatus.RUNNING
        self.reveal_button.setEnabled(ready)
        self.cancel_button.setEnabled(ready or running)
        text = self._job_text(job)
        if self.job_result.toPlainText() != text:
            self.job_result.setPlainText(text)

    @staticmethod
    def _job_text(job: DelegationJob | None) -> str:
        if not job:
            return ""
        if job.status == JobStatus.DELIVERED and job.result:
            sources = "\n".join(f"{source.title}\n{source.url}" for source in job.result.sources)
            return f"{job.result.answer}\n\n来源\n{sources}" if sources else job.result.answer
        if job.status == JobStatus.READY:
            return "答案已就绪。到达检查点后交付，也可以提前查看。"
        if job.status == JobStatus.FAILED:
            return f"委托失败：{job.error or '未收到有效的答案。'}"
        return JOB_STATES[job.status]

    def _poll(self) -> None:
        try:
            if self.session.poll():
                self._refresh()
        except UI_ERRORS as error:
            self._status(str(error), error=True)

    def closeEvent(self, event: QCloseEvent) -> None:
        self._timer.stop()
        try:
            self.session.close()
        except UI_ERRORS as error:
            self._status(str(error), error=True)
        super().closeEvent(event)
