语言 / Language：**简体中文** | [English](WORKSTREAMS.en.md)

# 组员自由认领指南

**HKU COMP7607 NLP · Group 14 · IntentAware-Agent**

本页为工作板块的统一说明，**以已提交 Proposal 为范围依据**。这里的技术实现和具体验收样例属于团队建议，尚未经过全员确定。项目当前仅包含文档与目录骨架。

## 如何认领任务

1. 打开 [GitHub Issues](https://github.com/Ir1svanquish/IntentAware-Agent/issues)，选择感兴趣的板块。
2. 阅读对应 Issue 的工作范围、依赖、交付物和验收要求。先检查是否已经有人认领。
3. 在 Issue 留言：`我想认领 [模块/子任务]；预计负责 [范围]；需要协作 [接口/人员]`。**不要求一个人包下全部模块**，也可多人拆分。
4. 请仓库维护者在 Issue 添加 Assignee，或具备权限者自行认领；未完成权限配置时，以 Issue 评论确认的分工为准。
5. 先对齐 API/数据协议，再从 `main` 创建 `feature/<topic>` 分支。通过 Pull Request 提交修改，在 PR 描述中写 `Closes #Issue编号`（只有确认全部验收条件满足时才使用自动关闭）。
6. 至少由另一名组员审查并根据验收清单复现；通过后合并。未达成的条目继续保持未完成并记录原因。

**避免冲突：** 同一 Issue 可由一人协调、多人共同负责；优先把开发任务拆成明确的子任务并在评论分工。不要把 GitHub Issues 列表当作已经自动分配的工作。

## 建议的五个主要板块

| 板块 | 主要内容 | 建议依赖 | 交付目录 |
| --- | --- | --- | --- |
| A 扩展与交互 | React 侧边栏、页面上下文、提醒与操作 | F 的 API 协议 | `apps/extension/` |
| B NLP 目标与活动分类 | 目标澄清、四分类、理由、Prompt、评估基线 | F 的分类数据结构 | `services/backend/app/modules/goals/`、`intent/` |
| C 任务记忆与恢复 | 保存分心、进度、下一步、恢复建议 | B 的目标模型、F 的协议 | `services/backend/app/modules/memory/` |
| D 异步委托与延迟展示 | 请求确认、检索、证据核查、Worker、结果投递 | F 的 API 协议，A 的交互 | `services/backend/app/modules/delegation/`、`delivery/` |
| E 研究实验与分析 | G/P/I/D、标注、基线、日志、Pilot、统计 | 全部模块；尽早制定日志 | `experiments/`、`tests/` |

另外设置 **F 基础接口与集成**，所有成员参与评审，可由任意一名组员牵头，避免技术决策互相矛盾。以上目录为建议开发路径，实际可以按合并后的架构调整。

## 跨模块协议（优先对齐）

建议至少确认：`Goal`、`ActivityContext`、`ActivityClassification`、`Detour`、`DelegationRequest`、`DelegationJob`、`Checkpoint`、`ExperimentEvent`。若接口暂未实现，先提供 Mock JSON 和说明，让其他人并行开发。

- **活动分类：** `direct_progress` / `necessary_preparation` / `optional_exploration` / `unclear`；分类要返回理由。
- **委托任务：** 创建草稿 → 用户确认（最多一次澄清）→ 后台检索最多两份公开来源 → 答案含来源链接和未解决点 → 立即或在检查点交付；支持提前查看、修改和取消。
- **实验对照：** G=目标提醒；P=G+分心记录及恢复；I=P+委托立即展示；D=P+委托检查点展示（允许提前查看）。
- **隐私与可靠性：** 页面摘录必须经用户批准；避免上传密钥及私人数据；记录模型版本、Prompt 版本、延迟、Token 使用和失败原因。实验数据必须可追溯但不暴露参与者身份。

## 通用验收定义（Definition of Done）

- [ ] 代码、说明和测试或人工复现步骤已经提交到 PR。
- [ ] 在 README 或模块说明中写清启动方式、输入输出和依赖；没有实现的功能必须明确说明。
- [ ] 具备正常案例、异常/边界案例的可复现检查；不能仅凭截图声称完成。
- [ ] 涉及 API 变化时同步修改契约，通知依赖模块。
- [ ] 涉及 NLP 时区分训练/调 Prompt 数据和保留评估数据，保存可复现的配置。
- [ ] 涉及实验时保持 G/P/I/D 核心模型、提醒规则及相应控制变量一致。
- [ ] 至少一名其他成员根据验收标准审查；没有满足的条件不得勾选或关闭 Issue。

## 认领留言模板

```text
我想认领：模块 __ / 子任务 __
我负责的范围：
预计交付：
依赖或需要协调的问题：
```

请继续参考 [TODO 总清单](../TODO.md) 与 [协作规范](../CONTRIBUTING.md)。
