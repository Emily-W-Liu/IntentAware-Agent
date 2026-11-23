语言 / Language：**简体中文** | [English](README.en.md)

# PySide6 桌面应用源码

从仓库根目录安装后，用 `python -m intentaware --demo` 启动中文窗口。默认分类器和委托执行器均为离线演示。目标、进度和偏离记录使用本地 SQLite。委托任务随当前应用会话结束。

- A [桌面交互](ui/README.md)在 `ui/window.py`，负责接收输入和显示结果。
- B [目标与活动分类](nlp/README.md)在 `nlp/demo.py`，实现离线四分类。
- C [任务记忆](memory/README.md)在 `memory/store.py`，负责 SQLite 存储。
- D [异步委托](delegation/README.md)在 `delegation/demo.py`，提供离线后台演示。
- E [研究评估](../../experiments/)使用当前实验轮次的 JSONL 日志。
- F [接口与集成](contracts/README.md)维护 `contracts/`、`session.py` 和 `__main__.py`，负责共享类型、功能开关和应用装配。

[运行、扩展与测试](../../docs/GETTING_STARTED.md) · [项目首页](../../README.md) · [认领任务](../../docs/WORKSTREAMS.md)
