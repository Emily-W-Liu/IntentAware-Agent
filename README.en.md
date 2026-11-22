Language / 语言：[简体中文](README.md) | **English**

# IntentAware-Agent

**HKU COMP7607 Natural Language Processing · Group 14**

> **Status: proposed four-week lightweight desktop MVP, pending team and supervisor approval.** The repository has documentation placeholders but no runnable app yet.

## Overview

A small desktop AI companion for writing, coding, reading and browsing. Users actively submit task context (or authorized text) to clarify goals, classify side activities, capture detours, resume work, and delegate side questions.

**Change from the submitted proposal:** The proposal specifies a browser extension, automatic activity interpretation on page changes, and browser-based experiments. The proposed pivot to **PySide6 desktop UI + user-supplied context** changes data collection and may affect evaluation, so **seek supervisor approval before replacing the proposed methodology**.

## Four MVP features

1. **Goal & Intent:** Confirm goal and next step; classify activities as direct progress, necessary preparation, optional exploration or unclear, with explanations.
2. **Detour & Resume:** Store side notes, links and confirmed progress; offer concrete resumption actions.
3. **Async Delegation:** After confirmation, retrieve up to two public sources in the background and draft an answer with verified citations and unresolved points.
4. **Deferred Delivery:** Condition I delivers when ready; D waits for a marked checkpoint, with early view/cancel options.

## Simplified stack and scope

| Layer | Choice |
|---|---|
| Desktop GUI | PySide6 (Python) |
| NLP | Replaceable pretrained LLM API with versioned prompt/model |
| Data | SQLite |
| Background jobs | Python worker/thread without blocking UI |
| Analysis | pandas + scikit-learn |

Out of scope for MVP: Electron, React, Chrome extension, automatically reading Word/VS Code/webpage bodies, continuous screenshots, keylogging, and cross-platform packaging. Optional Windows window title capture is not equivalent to understanding task content. Background work only needs to run while the app is open.

## Four-week plan

| Week | Milestone |
|---|---|
| 1 | Supervisor approval, role claims, PySide6 skeleton, shared data schema, LLM/SQLite and early study preparation |
| 2 | Demoable Goal/Intent + Detour/Resume MVP |
| 3 | Delegation, evidence checks, deferred delivery, G/P/I/D switching and pilot |
| 4 | Evaluation, integration, demo and report |

Recruitment, consent and ethics preparation must begin in week one; required approvals may exceed the schedule.

## Evaluation safeguards

Preserve **G** (goal reminders), **P** (+ detour capture/resumption), **I** (+ delegation, immediate delivery), and **D** (+ delegation, checkpoint delivery), with consistent shared controls. The submitted proposal plans 12–18 adults, 60 activity-context examples and 40 held-out delegation requests.

**Measurement gap:** The proposal measures resumption time until the next meaningful main-task edit. A desktop UI with manual context submission may not observe edits in external programs. Use an instrumented controlled editor/log, or explicitly approve a revised proxy with the supervisor. A “return” click is not a meaningful edit.

## Repo and claiming

```text
src/intentaware/       # Planned Python desktop app and modules
experiments/           # Study and metrics
docs/                  # Architecture, protocols and claiming guide
tests/                 # Automated tests
TODO.md                # Chinese four-week checklist
CONTRIBUTING.md        # Chinese contribution guide
```

[Claim GitHub Issues](https://github.com/Ir1svanquish/IntentAware-Agent/issues) · [English acceptance guide](docs/WORKSTREAMS.en.md) · [English TODO](TODO.en.md) · [Contribution rules](CONTRIBUTING.en.md)

A Desktop UI, B NLP, C Memory, D Delegation, E Evaluation, and shared F Contracts/Integration are open for claims. No person is preassigned.

## Privacy

Obtain user consent before sending content to external models. Do not commit secrets, private files, raw browsing data or identifiable participant information; never fabricate results.
