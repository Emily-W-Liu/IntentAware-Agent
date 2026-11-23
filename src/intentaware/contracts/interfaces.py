"""组员通过实现这些小接口替换离线演示模块。"""

from threading import Event
from typing import Protocol

from .models import ActivityContext, Classification, DelegationResult


class Classifier(Protocol):
    def classify(self, context: ActivityContext) -> Classification:
        """返回四分类及理由；失败时抛出有意义的异常。"""
        ...


class Delegator(Protocol):
    def run(self, question: str, cancel: Event) -> DelegationResult:
        """在后台执行。检查 cancel，并为外部请求设置有限超时。"""
        ...
