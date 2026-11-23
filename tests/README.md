语言 / Language：**简体中文** | [English](README.en.md)

# 测试

安装开发依赖后，从仓库根目录运行：

```bash
python -m pytest
```

测试覆盖离线四分类、SQLite 重启保存、活动分析与委托的后台执行、取消、G/P/I/D 功能限制、完成与交付的事件顺序，以及实际 Qt 窗口的按钮操作。所有测试使用临时数据库，不访问真实模型或互联网。

| 文件 | 主要检查 |
| --- | --- |
| `test_classifier.py` | 四种分类、规则优先级和上下文 |
| `test_storage.py` | 保存、更新、删除、重启、事件导出 |
| `test_session.py` | 多模块流程、异步任务、条件切换和异常 |
| `test_ui.py` | 界面操作、后台响应、结果展示和窗口布局 |

Linux 无显示环境可设置 `QT_QPA_PLATFORM=offscreen` 后运行测试。[启动与开发指南](../docs/GETTING_STARTED.md)
