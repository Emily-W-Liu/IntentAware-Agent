# F 共享数据契约与集成

[`models.py`](models.py) 定义目标、分类、进度、委托、实验事件等数据类型。[`interfaces.py`](interfaces.py) 定义可替换的分类和委托协议。[`session.py`](../session.py) 验证返回值、启用条件、协调后台工作和记录事件。[`__main__.py`](../__main__.py) 负责应用启动与依赖装配。

修改共享类型或返回值时，运行 [`tests/test_session.py`](../../../tests/test_session.py) 和完整测试。核对 I/D 的委托完成与交付分开记录，以及 JSONL 只包含当前实验轮次。

[模块分工](../../../docs/GETTING_STARTED.md#开发从哪个文件开始) · [认领与验收](https://github.com/Ir1svanquish/IntentAware-Agent/issues/6)
