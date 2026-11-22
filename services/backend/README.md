语言 / Language：**简体中文** | [English](README.en.md)

# 旧版后端服务目录（暂停使用）

四周方案不再要求单独的 FastAPI 后端；核心 NLP、Memory、Delegation 将作为 **Python 本地模块**，与 PySide6 界面通过共享接口配合。此处仅保留旧文档占位；请在 `src/intentaware/` 开发。异步查询不应阻塞 UI，首版只要求应用打开时运行。
