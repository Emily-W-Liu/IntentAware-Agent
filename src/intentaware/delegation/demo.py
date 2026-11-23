"""Offline worker: demonstrate execution and delivery without making web requests."""

from concurrent.futures import CancelledError
from threading import Event

from intentaware.contracts import DelegationResult


class DemoDelegator:
    def __init__(self, delay_seconds: float = 1.2):
        if delay_seconds < 0:
            raise ValueError("演示延迟不能小于零。")
        self.delay_seconds = delay_seconds

    def run(self, question: str, cancel: Event) -> DelegationResult:
        """Replace this method with bounded retrieval + generation for module D."""
        if not question.strip():
            raise ValueError("请输入需要委托的问题。")
        if cancel.wait(self.delay_seconds):
            raise CancelledError("任务已取消。")
        return DelegationResult(
            answer=(
                "离线委托演示\n\n"
                f"已接收问题：{question.strip()}\n\n"
                "后台任务已经完成，主窗口在等待期间仍可继续操作。\n"
                "接入真实检索与模型后，这里将显示问题的回答、来源和未解决点。\n\n"
                "本次没有联网检索，也没有生成事实性答案。"
            ),
        )
