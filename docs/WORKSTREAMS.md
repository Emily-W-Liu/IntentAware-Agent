# 任务认领与验收指南

本项目分为六个工作板块。组员可根据兴趣与技能认领整个模块，也可以认领其中的具体子任务。

## 认领流程

1. 打开对应的 GitHub Issue，阅读开发任务、交付内容和验收标准。
2. 在评论区写明要负责的模块或具体子任务。
3. 确认分工后，从 `main` 创建功能分支开展开发。
4. 完成后提交 Pull Request，附上运行方法、测试结果和需要注意的问题。
5. 由其他组员审核，通过验收后合并代码并关闭 Issue。

## 开发板块

| 板块 | 主要任务 | 交付目录 |
| --- | --- | --- |
| [A — 桌面界面与交互](https://github.com/Ir1svanquish/IntentAware-Agent/issues/1) | PySide6 工作台、自动识别反馈、人工修正、支线与委托交互 | `src/intentaware/ui/` |
| [B — NLP 目标理解与活动分类](https://github.com/Ir1svanquish/IntentAware-Agent/issues/2) | 本地标题推断、四类活动判断、置信度与理由；后续 NLP/LLM 接入 | `src/intentaware/nlp/` |
| [C — 任务记忆与恢复](https://github.com/Ir1svanquish/IntentAware-Agent/issues/3) | SQLite、任务进度、分心记录与恢复建议 | `src/intentaware/memory/` |
| [D — 异步委托与结果展示](https://github.com/Ir1svanquish/IntentAware-Agent/issues/4) | 后台 Agent、公开来源检索、引用核验及延迟交付 | `src/intentaware/delegation/` |
| [E — 实验设计与结果评估](https://github.com/Ir1svanquish/IntentAware-Agent/issues/5) | G/P/I/D 实验、任务日志、分类指标和结果分析 | `experiments/` |
| [F — 数据结构与系统集成](https://github.com/Ir1svanquish/IntentAware-Agent/issues/6) | 前台采集、任务监视器、共享协议、应用装配及集成测试 | `src/intentaware/activity/`、`src/intentaware/contracts/` |

具体开发步骤和验收清单请查看各板块 Issue。

## 共用接口

各模块围绕以下数据结构协作：

- `Goal`：任务目标与下一步行动。
- `ActivitySnapshot`：当前应用名称、窗口标题和观察来源，仅提供有限的活动线索。
- `CaptureResult`：观察结果，以及正常、空闲、排除或不可用状态。
- `TaskSuggestion`：候选任务、下一步、活动描述、置信度与原因。
- `ActivityContext`：自动补充或用户提交的活动，连同目标和已确认进度。
- `Classification`：活动类别及判断理由。
- `Detour`：暂存的问题、笔记和链接。
- `Progress`：已确认的任务进度。
- `DelegationJob`：异步委托内容与运行状态。
- `Checkpoint`：任务检查点。
- `ExperimentEvent`：实验事件与时间记录。

窗口观察数据定义在 [`activity/models.py`](../src/intentaware/activity/models.py)，任务与实验数据定义在 [`contracts/models.py`](../src/intentaware/contracts/models.py)。[`TaskMonitor`](../src/intentaware/activity/monitor.py) 协调稳定采样与人工修正；[`DesktopSession`](../src/intentaware/session.py) 管理目标、分类、委托和实验条件。具体调用方式见[上手指南](GETTING_STARTED.md#开发从哪个文件开始)。

## 通用验收要求

- [ ] 交付代码、必要的使用说明及测试。
- [ ] 提供正常流程与异常情况的验证方法。
- [ ] 输入输出符合共享的数据结构。
- [ ] 自动识别更改覆盖无标题、低置信度、平台不可用、暂停、排除和延迟返回；临时切换窗口不替换当前任务。
- [ ] 不将窗口观察当作已确认进度或有效编辑，不把持续观察到的原始标题写入事件日志。
- [ ] 所需依赖、配置和运行步骤完整。
- [ ] 相关模块能够正常调用，不引入明显的集成问题。
- [ ] 不提交 API 密钥或未经授权的私人数据。
- [ ] 通过其他组员的 Pull Request 审核。

## 四周开发安排

| 周次 | 重点 |
| --- | --- |
| 第 1 周 | 开发环境、基础界面、数据结构与实验准备 |
| 第 2 周 | NLP 分类、任务记忆与恢复流程 |
| 第 3 周 | 异步委托、延迟展示与集成测试 |
| 第 4 周 | 实验评估、问题修复、项目演示与最终报告 |

[返回项目首页](../README.md) · [查看完整 TODO](../TODO.md) · [团队协作规范](../CONTRIBUTING.md)
