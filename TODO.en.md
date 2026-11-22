Language / 语言：[简体中文](TODO.md) | **English**

# Project TODO

**COMP7607 NLP · Group 14**  
**Status:** Initial planning; only documentation and the directory skeleton have been initialized.

> Check a box only after actual completion and verification. Proposed roles: A (Extension), B (NLP), C (Task Memory), D (Delegation), E (Evaluation & Integration). **No students have been assigned yet.**

## P0 — Setup & shared contracts

- [ ] Confirm responsibilities for all five members
- [ ] Review the submitted proposal together
- [ ] Agree on core data models and OpenAPI endpoints
- [ ] Decide the model provider, budget, test credentials, and privacy rules
- [ ] Set up extension and backend development environments
- [ ] Configure basic lint checks, automated tests, and smoke tests

## P1 — Core MVP (priority)

- [ ] [A] Build React sidebar and page-event integration
- [ ] [B] Implement goal clarification and confirmed next-step extraction
- [ ] [B] Implement four-category contextual activity classification with reasons
- [ ] [C] Save detours (links/notes) and confirmed task progress
- [ ] [C] Generate concrete task-resumption suggestions
- [ ] [A+B+C] Demo a full goal → detour → resume flow

## P2 — Asynchronous delegation

- [ ] [D] Convert side questions into editable, scoped requests
- [ ] [D] Implement background retrieval from up to two public sources
- [ ] [D] Validate source links and supporting evidence
- [ ] [D] Implement job states, error handling, edits, and cancellation
- [ ] [D+A] Implement I (immediate delivery) and D (checkpoint delivery), including early viewing

## P3 — Evaluation

- [ ] [E] Implement G/P/I/D feature flags and consistent event logging
- [ ] Prepare four comparable browser tasks and counterbalanced condition orders
- [ ] Prepare 60 task-context examples and have two reviewers check them
- [ ] Reserve 40 delegation requests excluded from prompt development
- [ ] Implement a keyword baseline; compute macro-F1 and false-warning rates
- [ ] Record resumption time, completion, output quality, source support, perceived burden, latency, and token usage
- [ ] Confirm participant consent and research-ethics requirements; run a pilot
- [ ] Conduct the planned within-participant study with 12–18 adults

## P4 — Integration & submission

- [ ] Review PRs and run cross-module integration tests
- [ ] Document errors, limitations, and unfinished work
- [ ] Prepare a demo and reproducible run instructions
- [ ] Write results, discussion, and final report
- [ ] Verify final submission materials


## Claim a workstream

[GitHub Issues: open workstreams](https://github.com/Ir1svanquish/IntentAware-Agent/issues) · [English claiming and acceptance guide](docs/WORKSTREAMS.en.md) · [中文说明](docs/WORKSTREAMS.md)

Members may claim modules or subtasks by commenting on an Issue. A maintainer can then assign the owner. Deliverables must satisfy the Issue's acceptance checklist.

## Definition of done

- A task is done only with committed code/docs and a reproducible test or demonstration.
- Keep prompt-development examples separate from final evaluation items to avoid leakage.
- Do not change G/P/I/D controls without team agreement.
