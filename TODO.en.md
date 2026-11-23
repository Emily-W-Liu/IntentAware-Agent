Language / 语言：[简体中文](TODO.md) | **English**

# Four-week Sprint Checklist

> A runnable offline desktop starter is available. Real NLP, retrieval and research evaluation remain to be implemented. Claim modules in [GitHub Issues](https://github.com/Ir1svanquish/IntentAware-Agent/issues).

## Week 1 — Foundation and early study preparation

- [ ] [Team] Claim five roles and an F contract coordinator (may overlap)
- [x] [F] Define Goal, ActivityContext, Classification, Progress, Detour, DelegationJob, Checkpoint and ExperimentEvent contracts
- [x] [A/F] Initialize runnable PySide6 UI with goal, progress and context input
- [x] [C/F] Set up SQLite storage for goals, progress, detours and events
- [x] [F] Provide replaceable classifier/delegator interfaces and offline demo implementations
- [ ] [B] Connect a real LLM API and versioned prompts
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

## Starter entry points

- [Getting started and module integration (Chinese)](docs/GETTING_STARTED.md): installation, demo, module replacement and tests.
- `src/intentaware/session.py`: connects the UI, NLP, persistence and background delegation.
- Classification currently uses keyword demo rules; delegation returns an offline example. Research evaluation requires the real modules.
- Context is supplied by the user; G/P/I/D feature conditions are preserved.

## Definition of done

Reproducible code/docs, setup steps, happy/error tests, and review by another teammate. [Workstream guide (Chinese)](docs/WORKSTREAMS.md).
