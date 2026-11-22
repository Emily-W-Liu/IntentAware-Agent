# Contributing / 团队协作指南

## Working agreement / 基本约定

- **One shared repository / 统一仓库:** `main` is the integration branch; use a separate branch for each change. / `main` 为集成分支，每项修改建立独立分支。
- **Proposed branch names / 建议分支名:** `feature/extension-sidebar`, `feature/intent-classifier`, `feature/task-memory`, `feature/delegation-agent`, `feature/experiment-runner`, `fix/<topic>`.
- **Pull requests / 合并请求:** Open a PR with a short summary, tests/checks, screenshots for UI changes, and any API-contract changes. Ask another teammate to review before merging. / PR 需说明修改内容、测试方法、界面截图（如适用）和接口变化，合并前请另一名组员审阅。
- **API first / 接口优先:** Agree on request/response schemas before implementing dependent modules. / 依赖模块开工前先明确输入输出结构。
- **Shared ownership / 共同负责:** Proposed roles A–E are starting points, not fixed ownership; testing, experiments and the report are everyone's responsibility. / A–E 只是起始分工建议，测试、实验和报告由全组共同承担。
- **No secrets / 不提交机密:** Keep API keys in local environment variables; publish only safe examples. No raw personal browsing data or participant identities. / 密钥仅保存在本地环境变量，不上传个人浏览记录及参与者身份数据。
- **Scientific integrity / 研究诚信:** Never fabricate study data, evaluations, citations or feature-completion claims. / 不伪造实验数据、评价、引用或功能完成状态。

## Suggested PR checklist / 建议 PR 检查清单

- [ ] Scope and purpose described / 已说明修改目的和范围
- [ ] Relevant tests or manual steps included / 已提供测试或手动验证步骤
- [ ] No API secrets or private data committed / 未提交密钥或私人数据
- [ ] Any API or experiment-protocol changes disclosed / 已说明接口或实验协议变化
- [ ] Another teammate reviewed / 已经其他组员审阅
