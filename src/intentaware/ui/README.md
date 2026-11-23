# A 桌面交互

[`window.py`](window.py) 的 `MainWindow` 展示目标、活动分析、暂存支线、任务恢复、委托和运行事件。界面用 `session.start_analysis()` 发起后台分类，定时在主线程调用 `session.poll()` 刷新任务状态。

交互修改后，在 D 条件下检查等待委托期间仍可操作窗口、答案在检查点前隐藏、取消后不显示答案。界面回归用例位于 [`tests/test_ui.py`](../../../tests/test_ui.py)。

[六步演示](../../../docs/GETTING_STARTED.md#六步跑通离线演示) · [认领与验收](https://github.com/Ir1svanquish/IntentAware-Agent/issues/1)
