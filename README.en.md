Language / 语言：[简体中文](README.md) | **English**

# IntentAware-Agent

**The University of Hong Kong · COMP7607 Natural Language Processing · Group 14**  
**Project:** An Agent with Intent Awareness for Task Continuity and Asynchronous Delegation  
**Status:** Planning and initial setup; features are not implemented yet.

## Overview

We propose a browser-based focus companion that understands a user's current goal, interprets browsing activities in context, captures useful detours, and offers concrete steps to resume unfinished work. Users may also delegate side questions to a background agent and choose whether to see the results immediately or at a selected task checkpoint.

## Planned features

1. **Goal clarification and activity interpretation:** Confirm the goal and next action; classify activities as direct progress, necessary preparation, optional exploration, or unclear. Proposed API labels: `direct_progress`, `necessary_preparation`, `optional_exploration`, `unclear`.
2. **Detour capture and task resumption:** Save links and notes, record confirmed progress, and suggest actionable next steps.
3. **Asynchronous delegation:** Turn side questions into editable requests, retrieve up to two public sources, and draft brief source-linked answers with evidence checks.
4. **Deferred delivery:** Present answers at user-selected checkpoints, with options to view early or cancel.

## Proposed technical architecture

- **Browser extension:** React + TypeScript, Chrome Manifest V3 sidebar
- **Backend:** Python + FastAPI, separate asynchronous worker
- **NLP:** Replaceable pretrained language-model provider
- **State:** Browser session storage plus backend persistence where needed
- **Evaluation:** Reproducible scripts and event logging

> These are suggested implementation choices, not completed features or new course requirements. The submitted proposal defines the research scope.

## Repository structure

```text
apps/extension/       # Browser extension and sidebar
services/backend/     # API, NLP and agent modules
experiments/          # Study tasks, baselines and analysis
docs/                 # Architecture, API contracts and protocol
tests/                # Automated tests
TODO.md               # 中文任务清单
TODO.en.md            # English task list
CONTRIBUTING.md       # 中文协作规范
CONTRIBUTING.en.md    # English contribution guide
```

## Research plan

The proposal specifies four conditions:

| Condition | Features |
|---|---|
| **G** | Goal-aware reminders |
| **P** | G + detour capture and task resumption |
| **I** | P + delegation with immediate delivery when ready |
| **D** | P + delegation with checkpoint-based deferred delivery |

After a pilot, the plan includes a counterbalanced within-participant study with 12–18 adults, plus 60 task-context examples for activity classification and 40 held-out requests for delegation evaluation. See the proposal for the full measures and controls.

## Getting started

1. Read the [task list](TODO.en.md) and agree on owners and priorities.
2. Agree on data structures and API contracts before parallel implementation.
3. Follow the [contributing guide](CONTRIBUTING.en.md); implement features on separate branches and merge via Pull Requests.
4. **The repository currently contains documentation and a directory skeleton, not a runnable application.**

## Privacy and research integrity

Do not commit API keys, private browsing content, participant identities, or unconsented data. Never fabricate study results or citations.
