# Project TODO / 项目任务清单

**Group 14 · COMP7607 NLP**  
**Status / 状态:** Initial planning / 初始规划

> Check a box only after the work is actually completed. / 仅在任务真实完成后勾选。
> **Suggested roles / 建议分工:** A = Extension, B = NLP, C = Memory, D = Delegation, E = Evaluation & Integration. These are **not yet assigned to specific students**. / A–E 尚未分配给具体组员。

## P0 — Setup & shared contracts / 环境与接口约定

- [ ] Confirm five members' roles and responsibilities / 确定五名组员的职责分工
- [ ] Review the approved proposal together / 全组核对已提交 Proposal
- [ ] Agree on core data models and OpenAPI endpoints / 统一核心数据模型与 OpenAPI 接口
- [ ] Decide LLM provider, budget, test credentials and privacy policy / 确定模型供应商、费用、测试凭据和隐私规则
- [ ] Set up extension and backend development environments / 建立前端扩展与后端开发环境
- [ ] Add basic lint/test checks and a smoke-test workflow / 添加基本静态检查、测试与冒烟测试流程

## P1 — Core MVP (priority) / 核心最小可用版本（优先）

- [ ] [A] Build React sidebar and page-event integration / 构建 React 侧边栏与网页事件接入
- [ ] [B] Implement goal clarification and confirmed next-step extraction / 实现目标澄清与下一步提取
- [ ] [B] Implement contextual activity classification into four categories with reasons / 实现带理由的四分类活动理解
- [ ] [C] Save detours (links/notes) and confirmed task progress / 保存分心链接、笔记和已确认进度
- [ ] [C] Generate concrete task-resumption suggestions / 生成具体任务恢复建议
- [ ] [A+B+C] Demo a complete goal → detour → resume flow / 演示“目标 → 分心 → 恢复”的完整流程

## P2 — Async delegation / 异步委托

- [ ] [D] Convert side questions into editable scoped requests / 将支线问题转为可编辑、有明确范围的委托
- [ ] [D] Run background retrieval from at most two public sources / 后台检索最多两份公开来源
- [ ] [D] Verify source links and evidence support / 核查引用链接与证据支持
- [ ] [D] Implement job states, error handling, edit and cancel / 实现任务状态、错误处理、修改与取消
- [ ] [D+A] Implement immediate delivery (I) and checkpoint-based delivery (D), including early view / 实现立即展示与检查点延迟展示，并支持提前查看

## P3 — Evaluation / 研究评估

- [ ] [E] Implement G/P/I/D feature flags and consistent logging / 实现四组实验条件切换与统一日志
- [ ] Prepare four comparable browser tasks and counterbalanced orders / 准备四个可比任务与平衡顺序
- [ ] Prepare 60 activity-context examples and obtain two-reviewer checks / 准备 60 个活动样本并由两名评审核查
- [ ] Reserve 40 held-out delegation requests, excluded from prompt development / 保留 40 个委托请求，不用于 Prompt 开发
- [ ] Implement keyword baseline; calculate macro-F1 and false-warning rates / 实现关键词基线并计算 Macro-F1 和误提醒率
- [ ] Track resumption time, completion, output quality, source support, perceived burden, latency and token usage / 记录恢复时间、完成情况、输出质量、引用支持、感知负担、延迟和 Token 用量
- [ ] Confirm participant-consent/ethics requirements; run pilot / 核对参与者同意及伦理要求，完成预实验
- [ ] Conduct planned within-participant study with 12–18 adults / 按计划完成 12–18 人的组内实验

## P4 — Integration & submission / 集成与最终交付

- [ ] Review PRs and test cross-module integration / 审查 PR 并测试跨模块集成
- [ ] Document limitations, errors and incomplete items / 记录局限、错误与尚未完成事项
- [ ] Make demo and reproducible run instructions / 准备演示与可复现运行说明
- [ ] Write results, discussion and final report / 完成结果、讨论与最终报告
- [ ] Perform final submission checklist / 核对最终提交材料

## Definition of done / 完成标准

- An item is done only with committed code/docs and a reproducible check or demonstration. / 只有在代码或文档提交且能够复验后才能标记完成。
- Keep NLP prompts and evaluation examples separated to avoid leakage. / Prompt 开发与最终评估样本必须隔离，避免数据泄漏。
- Do not change G/P/I/D control logic without team agreement. / 未经全组讨论，不得改变 G/P/I/D 的实验对照逻辑。
