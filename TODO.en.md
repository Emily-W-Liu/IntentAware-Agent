Language / 语言：[简体中文](TODO.md) | **English**

# Four-week Sprint Checklist

> **Desktop pivot pending supervisor approval.** Unchecked items are not completed. Claim modules in [GitHub Issues](https://github.com/Ir1svanquish/IntentAware-Agent/issues).

## Week 1 — Foundation and early study preparation

- [ ] [Team] Confirm supervisor approval for replacing browser extension/automatic page interpretation with desktop app/manual context
- [ ] [Team] Claim five roles and an F contract coordinator (may overlap)
- [ ] [F] Define Goal, Activity, Detour, DelegationJob, Checkpoint, ExperimentEvent contracts
- [ ] [A] Initialize runnable PySide6 UI with goal/context input
- [ ] [C/F] Set up SQLite storage interface
- [ ] [B] Implement replaceable LLM adapter, versioned prompts and mock outputs
- [ ] [E] Begin controlled study task/log design, recruitment and consent/ethics preparation

## Week 2 — Core MVP

- [ ] [B] Goal clarification, next-action extraction, four-class interpretation and reasons
- [ ] [C] Detour/progress CRUD, resumption suggestions and pause/dismiss
- [ ] [A+B+C] Demo goal → manually supplied context → classification → detour → resumption
- [ ] [E] Prepare and separate prompt-development and held-out evaluation examples

## Week 3 — Delegation and pilot

- [ ] [D] Editable delegation draft with at most one clarification
- [ ] [D] In-app background retrieval of at most two public sources; verify citations and unresolved points
- [ ] [D+A] I immediate, D manual-checkpoint delivery, early view and cancellation
- [ ] [E/F] G/P/I/D condition switches, event logs and integration checks
- [ ] [Team] Pilot and major fixes

## Week 4 — Evaluation and submission

- [ ] [E+Team] Evaluate 60 task-context examples (two reviewers) and 40 held-out requests as proposed
- [ ] [E] Keyword baseline, macro-F1, false-warning rate, output quality, source support, latency and token usage
- [ ] [Team] Subject to approvals/consent, conduct planned 12–18-person study; honestly report unfinished tasks
- [ ] [E] Log next meaningful main-task edit, not merely a “return” button, for resumption time
- [ ] [Team] Demo, tests, analysis and final report

## Out of MVP scope (decisions, not implemented features)

No Electron/React/browser extension, continuous screenshots, automatic reading of arbitrary external apps, keylogging, or multi-platform distribution. User-supplied context; retain G/P/I/D core comparisons.

## Definition of done

Reproducible code/docs, setup steps, happy/error tests, and review by another teammate. [English claiming guide](docs/WORKSTREAMS.en.md) / [中文指南](docs/WORKSTREAMS.md).
