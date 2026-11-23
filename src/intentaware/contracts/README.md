# F 共享数据契约与集成

[`models.py`](models.py) 定义目标、分类、用户确认的进度、委托和实验事件。[`interfaces.py`](interfaces.py) 定义可替换的分类与委托协议。前台观察相关的 `ActivitySnapshot`、`CaptureResult` 和 `TaskSuggestion` 定义在 [`activity/models.py`](../activity/models.py)。

[`TaskMonitor`](../activity/monitor.py) 协调观察、稳定采样、首次任务生成、人工修正及新任务建议。[`DesktopSession`](../session.py) 验证返回值、管理 G/P/I/D 功能开关、接收后台结果并记录事件。[`__main__.py`](../__main__.py) 装配真实观察、模拟观察或手动启动模式。

自动推断不能填入已确认进度，原始持续窗口标题不能写入事件导出。人工修正更新当前任务；采用新任务建议则建立新的任务标识，旧支线继续归属于旧任务。

修改共享类型或返回值后，运行 [`test_session.py`](../../../tests/test_session.py)、[`test_monitor.py`](../../../tests/test_monitor.py) 和相关界面测试。核对暂停后的延迟结果不会生效、G/P/I/D 功能限制仍有效、I/D 的完成与交付分开记录，以及 JSONL 只包含当前轮次。

[模块分工](../../../docs/GETTING_STARTED.md#开发从哪个文件开始) · [认领与验收](https://github.com/Ir1svanquish/IntentAware-Agent/issues/6)
