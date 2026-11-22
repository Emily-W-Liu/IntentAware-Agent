Language / 语言：[简体中文](CONTRIBUTING.md) | **English**

# Contributing Guide

## Working agreement

- **Shared repository:** `main` is the integration branch; use a separate branch for each change.
- **Suggested branch names:** `feature/extension-sidebar`, `feature/intent-classifier`, `feature/task-memory`, `feature/delegation-agent`, `feature/experiment-runner`, `fix/<topic>`.
- **Pull requests:** Describe the purpose, testing steps, UI screenshots (if applicable), and any API changes. Request review by at least one teammate before merging.
- **API first:** Agree on request/response schemas before implementing dependent modules.
- **Shared ownership:** A–E are proposed roles, not assigned members. Testing, research experiments, and the report are shared responsibilities.
- **Privacy:** Keep API keys in local environment variables; do not upload private browsing data, participant identities, or unconsented data.
- **Research integrity:** Do not fabricate study results, evaluations, citations, or completion claims.

## PR checklist

- [ ] Scope and purpose are described
- [ ] Tests or manual verification steps are provided
- [ ] No API secrets or private data are committed
- [ ] Any API or experiment-protocol changes are documented
- [ ] Another teammate has reviewed
