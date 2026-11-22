语言 / Language：**简体中文** | [English](README.en.md)

# IntentAware-Agent

**HKU COMP7607 Natural Language Processing · Group 14**

> **状态：四周轻量桌面版方案，待全组及导师确认。** 当前仓库仅有文档骨架，尚无可运行应用。

## 项目简介

一个在写作、编程、阅读和浏览网页时都能使用的轻量桌面 AI 助手。用户主动输入或粘贴获准的任务上下文，系统理解主要目标，判断支线活动的相关性，保存分心内容、辅助恢复任务，并把问题交给后台 Agent 处理。

**与原 Proposal 的差别：** 原提案采用浏览器扩展，自动根据页面切换判断行为，并以浏览器任务开展实验。当前改为 **PySide6 独立桌面 UI + 手动提交上下文**，会影响活动采集与实验测量，**正式替换前应向导师确认**。

## MVP 四大功能

1. **Goal & Intent：** 确认目标与下一步，将活动分类为直接进展、必要准备、可选探索、不确定，并给出理由。
2. **Detour & Resume：** 保存临时想法、链接和已确认的进度，给出具体恢复建议。
3. **Async Delegation：** 经用户确认后后台检索最多两份公开来源，给出有引用和未解决问题的答案。
4. **Deferred Delivery：** I 条件在就绪后展示；D 条件等待用户标记检查点完成，可提前查看或取消。

## 技术栈与范围

| 组件 | 简化实现 |
|---|---|
| 桌面 GUI | PySide6（Python） |
| NLP | 可替换的预训练 LLM API，固定 Prompt/模型版本 |
| 数据 | SQLite |
| 异步查询 | Python Worker/Thread，避免阻塞 GUI |
| 分析 | pandas + scikit-learn |

第一版**不做** Electron、React、Chrome 扩展、自动读 Word/VS Code/网页正文、持续截图、键盘记录和跨平台打包。可选读取 Windows 当前窗口标题，但不将其当作完整任务上下文。后台任务首版只要求软件打开时运行。

## 四周计划

| 周次 | 目标 |
|---|---|
| 第 1 周 | 导师确认变更、五人分工、PySide6 骨架、数据契约、LLM/SQLite；同步准备实验 |
| 第 2 周 | Goal/Intent + Detour/Resume 可演示的完整 MVP |
| 第 3 周 | Delegation、引用检查、延迟展示、G/P/I/D 条件切换和 Pilot |
| 第 4 周 | 实验数据分析、集成测试、Demo 和报告 |

实验准备、参与者招募、同意与伦理确认必须从第一周同步开展。不能假定四周内一定能完成所有招募或审批。

## 实验设计与风险

保留原 Proposal 的 **G（目标提醒）/ P（增加分心记录及恢复）/ I（委托且立即展示）/ D（委托且延迟至检查点）** 四条件对比，及其 12–18 名成人、60 个任务上下文例子、40 个保留委托请求的研究计划。

**关键测量问题：** Proposal 中恢复时间终点是「下一次有意义的主任务编辑」。桌面助手若只接收手动输入，不能自动观察外部软件编辑。实验应考虑受控任务编辑器/日志，或经导师同意明确修改测量指标；**不能把点击“返回任务”当作真正的编辑**。

## 代码与分工

```text
src/intentaware/       # 拟建 Python 桌面主程序及各模块
experiments/           # 实验与指标
docs/                  # 架构、研究协议、认领指引
tests/                 # 测试
TODO.md                # 中文四周任务清单
CONTRIBUTING.md        # 中文协作指南
```

[认领 GitHub Issues](https://github.com/Ir1svanquish/IntentAware-Agent/issues) · [详细认领与验收](docs/WORKSTREAMS.md) · [四周 TODO](TODO.md) · [协作指南](CONTRIBUTING.md)

A 桌面 UI、B NLP、C Memory、D Delegation、E Evaluation，以及全组参与的 F Contracts/Integration 均可自由认领，目前不预先指定负责人。

## 隐私

必须征得同意后才将上下文发给外部模型；不要提交密钥、私人文件、原始浏览记录或可识别的参与者数据，不得伪造实验结果。
