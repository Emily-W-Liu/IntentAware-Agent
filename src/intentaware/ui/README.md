# A 桌面交互

[`window.py`](window.py) 的 `MainWindow(session, monitor=None, demo=False)` 使用侧栏导航，先展示当前主任务、下一步、窗口线索和活动关联；输入表单只在点击“修正”或展开“手动补充活动”后出现。支线与恢复、委托、实验与记录、设置分别位于次级页面。

正常模式由 [`TaskMonitor`](../activity/monitor.py) 自动采集和识别，Qt 定时器在主线程轮询 `session.poll()` 和 `monitor.poll()`。会话中的目标、已确认进度和分类结果是显示依据；刷新不会覆盖正在编辑的修正草稿或排除列表。关闭窗口时停止轮询并关闭观察器和会话。暂停、排除或无法读取窗口时，界面不再把旧活动或旧分类显示为当前状态。

[`theme.py`](theme.py) 集中管理配色与系统中文字体，[`icons.py`](icons.py) 提供 Qt 渲染的矢量图标。标题和长内容支持换行，完整内容可从工具提示查看。识别仅使用本机的应用名称与窗口标题；界面明确区分模拟观察与当前的离线委托演示。

交互修改后，检查自动识别无需填写表单、修正草稿不被覆盖、暂停后仍可手动分析、采用新任务需要明确操作，以及小尺寸窗口的按钮可达性。在 D 条件下还需检查等待委托期间窗口可操作、答案在检查点前隐藏、取消后不显示答案。回归用例位于 [`test_ui.py`](../../../tests/test_ui.py) 与 [`test_automatic_ui.py`](../../../tests/test_automatic_ui.py)。

[自动识别使用指南](../../../docs/GETTING_STARTED.md#自动识别的日常使用) · [模拟观察与离线委托](../../../docs/GETTING_STARTED.md#跑通模拟观察与离线委托) · [认领与验收](https://github.com/Ir1svanquish/IntentAware-Agent/issues/1)
