语言 / Language：**简体中文** | [English](WORKSTREAMS.en.md)

# 四周桌面版 · 自由认领与验收

> **拟议技术路线：PySide6 + Python + SQLite + LLM API；待导师确认对原 Proposal 的变更。** 不做 Chrome 扩展或跨应用自动读取。五人认领 A–E；F 为可兼任的全组接口与集成任务。

## 如何认领

1. 打开 [Issues](https://github.com/Ir1svanquish/IntentAware-Agent/issues)，阅读任务、依赖、交付和验收清单。
2. 在对应 Issue 评论「我认领 X 模块的 ___ 子任务，预计交付 ___；依赖 ___」。可多人共享模块，但要避免修改同一文件冲突。
3. 由仓库维护者设置 Assignee 或在评论确认，组员从 `main` 创建独立功能分支。
4. 提交 PR，说明运行方式、测试结果、遗留风险；经至少一名其他成员审查通过后合并。
5. 所有验收项满足后才关闭 Issue。未完成部分保留并说明。

## 六大板块

| Issue | 范围 | 核心交付 |
|---|---|---|
| [A 桌面交互](https://github.com/Ir1svanquish/IntentAware-Agent/issues/1) | PySide6 界面，手动目标/上下文输入及功能控制 | 可运行窗口、交互、错误/加载状态 |
| [B NLP](https://github.com/Ir1svanquish/IntentAware-Agent/issues/2) | 目标澄清、活动四分类及理由 | 可替换 LLM Adapter、Prompt、结构化输出与测试 |
| [C 记忆与恢复](https://github.com/Ir1svanquish/IntentAware-Agent/issues/3) | Detour、SQLite、已确认进度与下一步 | CRUD、恢复建议及持久化测试 |
| [D 委托与投递](https://github.com/Ir1svanquish/IntentAware-Agent/issues/4) | 后台检索≤2 来源、引用核查、I/D 展示 | 非阻塞 Worker、任务状态、检查点控制 |
| [E 评估](https://github.com/Ir1svanquish/IntentAware-Agent/issues/5) | G/P/I/D、日志、标注、Baseline、Pilot | 评估脚本与可复现分析 |
| [F 契约与集成](https://github.com/Ir1svanquish/IntentAware-Agent/issues/6) | Python 数据模型、SQLite/LLM 接口与测试集成 | 数据协议、Mock、冒烟测试；全组审核 |

## 项目共用数据契约（建议）

`Goal`、`ActivityContext`、`Classification`、`Detour`、`Progress`、`DelegationJob`、`Checkpoint`、`ExperimentEvent`。先写类型/接口和模拟响应，不要因等待真实 LLM 而阻塞各模块。

**研究必须保留：** 四分类（direct progress / necessary preparation / optional exploration / unclear）；G/P/I/D 控制变量；D 允许提前查看；委托最多一次澄清及两份公开来源；实验样本与 Prompt 调试样本隔离。

**必须向导师确认：** 原 Proposal 的自动网页活动感知和「下一次有意义的主任务编辑」测量，如何映射至手动输入的桌面端。不能以「返回任务」按钮代替真正的编辑事件；可考虑在研究环境提供受控任务编辑器。

## 通用验收标准

- [ ] 新环境可按 README 启动/复现，所有未实现部分明确标注
- [ ] 提交有意义的正常及错误/边界测试
- [ ] 输入输出符合共享 Python 数据契约
- [ ] 无密钥或未经同意的私人上下文被提交/上传
- [ ] 涉及模型的功能记录 Prompt/模型版本，评估不混用保留样本
- [ ] 涉及 G/P/I/D 的功能不破坏控制条件
- [ ] 另一位组员 Review PR；不提前关闭不满足验收条件的 Issue

## 一个⽉时间安排

**第 1 周：** 范围确认、契约、可运行 UI 骨架和实验准备；**第 2 周：** NLP + Memory MVP；**第 3 周：** Delegation + Pilot；**第 4 周：** 评估、分析、报告。招募与伦理工作从第一周启动。

[详细 TODO](../TODO.md) · [协作规则](../CONTRIBUTING.md)
