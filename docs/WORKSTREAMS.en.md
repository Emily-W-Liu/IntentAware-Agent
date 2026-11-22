Language / 语言：[简体中文](WORKSTREAMS.md) | **English**

# Four-week Desktop MVP · Open Workstreams

> **Proposed stack: PySide6 + Python + SQLite + LLM API, pending supervisor approval of deviation from the submitted proposal.** No required Chrome extension or automatic cross-app text capture. Five students claim A–E; F is a shared coordination role that may overlap.

## How to claim

1. Browse [Issues](https://github.com/Ir1svanquish/IntentAware-Agent/issues); read scope, dependencies, deliverables and acceptance criteria.
2. Comment with your chosen module/subtask, proposed deliverable and dependencies. Co-ownership is allowed, but avoid simultaneous conflicting edits.
3. Maintainer confirms Assignee or assignment in comments. Branch from `main`.
4. Open PR with setup, tests, limitations, and changes; obtain review by at least one teammate.
5. Close the Issue only after meeting its acceptance criteria; document any unresolved items.

## Six workstreams

| Issue | Focus | Deliverable |
|---|---|---|
| [A Desktop UI](https://github.com/Ir1svanquish/IntentAware-Agent/issues/1) | PySide6, manual goal/context, controls | Runnable UI and state/error handling |
| [B NLP](https://github.com/Ir1svanquish/IntentAware-Agent/issues/2) | Goal clarification, four-way interpretation | LLM adapter, prompts, structured outputs, tests |
| [C Memory](https://github.com/Ir1svanquish/IntentAware-Agent/issues/3) | Detours, SQLite, confirmed progress | CRUD, resumption and persistence tests |
| [D Delegation](https://github.com/Ir1svanquish/IntentAware-Agent/issues/4) | Worker, ≤2 public sources, verified citations, I/D delivery | Non-blocking job lifecycle and checkpoints |
| [E Evaluation](https://github.com/Ir1svanquish/IntentAware-Agent/issues/5) | G/P/I/D, logging, annotations, baseline, pilot | Reproducible metrics and analysis |
| [F Integration](https://github.com/Ir1svanquish/IntentAware-Agent/issues/6) | Python schemas, SQLite/LLM interface, integration | Contracts, fixtures and smoke tests, team review |

## Shared contracts (proposed)

`Goal`, `ActivityContext`, `Classification`, `Detour`, `Progress`, `DelegationJob`, `Checkpoint`, `ExperimentEvent`. Agree on typed interfaces and mocks before coding dependent modules.

**Research controls retained:** Four activity categories; G/P/I/D comparisons; D permits early view; delegation has at most one clarification and two public sources; hold-out evaluation data remains separate from prompt development.

**Supervisor decision required:** The submitted proposal's automatic page observation and resumption-time endpoint (“next meaningful main-task edit”) cannot be assumed equivalent to a manually supplied context/“return” button. An instrumented task editor is one possible controlled study approach.

## Definition of done

- [ ] New developers can run/reproduce the result; unfinished modules are explicitly described
- [ ] Happy/error or boundary test cases are present
- [ ] Inputs/outputs follow shared Python contracts
- [ ] No secrets or unconsented personal context
- [ ] Prompt/model versions recorded; held-out examples protected
- [ ] G/P/I/D experimental controls preserved
- [ ] Another teammate reviews the PR; no premature Issue closure

## Timeline

**Week 1:** approval, contracts, runnable UI skeleton and early study preparation; **Week 2:** NLP/Memory MVP; **Week 3:** Delegation and pilot; **Week 4:** evaluation, analysis and report. Recruitment and ethics preparation start in week one.

[Detailed TODO](../TODO.en.md) · [Contributing](../CONTRIBUTING.en.md)
