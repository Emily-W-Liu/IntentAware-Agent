Language / 语言：[简体中文](README.md) | **English**

# IntentAware-Agent

**HKU COMP7607 · Natural Language Processing · Group 14**

## Overview

**IntentAware-Agent** is a desktop AI task companion for studying, writing, and coding. It interprets side activities in the context of a user's primary goal, captures useful detours and progress, and helps users resume work after interruptions. Users can delegate non-urgent questions to a background agent and choose when to view the results.

### Typical workflow

1. **Set a goal:** Enter the current task and next action, such as “Finish the Related Work section of my paper.”
2. **Provide context:** Describe the current activity, ask a side question, or paste text for analysis.
3. **Interpret activity:** The agent classifies it as direct progress, necessary preparation, optional exploration, or unclear, with an explanation.
4. **Capture or delegate:** Save detours or let the agent research a side question in the background.
5. **Resume work:** Get an actionable next step based on confirmed progress; view delegated answers immediately or at a task checkpoint.

## Core features

| Module | Responsibilities |
| --- | --- |
| **Goal & Intent** | Clarify the main goal and next step; classify activities in context with explanations |
| **Detour & Resume** | Store links, notes, and confirmed progress; suggest concrete resumption actions |
| **Async Delegation** | Turn questions into editable requests; retrieve up to two public sources and draft cited answers |
| **Deferred Delivery** | Control when results appear; support checkpoints, early viewing, and cancellation |
| **Experiment & Evaluation** | Log task events, switch study conditions, and evaluate classification and task continuity |

## Tech stack

| Component | Technology |
| --- | --- |
| Desktop GUI | **Python + PySide6** |
| NLP inference | Replaceable pretrained LLM API |
| Local persistence | SQLite |
| Background processing | Python worker / thread |
| Experiment analysis | pandas + scikit-learn |
| Automated tests | pytest |

The application uses modular Python components. Users provide the context they want analyzed, while task state is stored locally. Long-running retrieval jobs execute in the background so the UI remains responsive.

## Research and evaluation

Four feature conditions are compared:

| Condition | Capabilities |
| --- | --- |
| **G** | Goal-aware reminders |
| **P** | G + detour capture and task resumption |
| **I** | P + asynchronous delegation, with results shown when ready |
| **D** | P + asynchronous delegation, with checkpoint-based delivery (early viewing allowed) |

The evaluation plan includes a pilot, a within-participant study with **12–18 adults**, **60 task-context examples**, and **40 held-out delegation requests**.

Key measures include macro-F1 and false-warning rates for activity classification, task completion and output quality, resumption time, source support, perceived burden, latency, and token usage. Resumption time ends at the next observable meaningful main-task edit.

## Four-week development plan

| Week | Main deliverables |
| --- | --- |
| **1** | Project foundation, PySide6 UI, shared schemas, SQLite and LLM adapters; begin study preparation |
| **2** | End-to-end Goal & Intent and Detour & Resume flow |
| **3** | Async Delegation, Deferred Delivery, study-condition switches, and integration tests |
| **4** | Pilot and evaluation, analysis, demo, and final report |

## Project layout

```text
src/intentaware/
├── ui/             # Desktop interface
├── nlp/            # Goal understanding and activity classification
├── memory/         # Progress, detours, and resumption
├── delegation/     # Background requests and result delivery
└── contracts/      # Shared schemas and interfaces

experiments/        # Study tasks, logs, and analysis
tests/              # Automated tests
docs/               # Technical documentation and workstream guides
TODO.md             # Development checklist
CONTRIBUTING.md     # Team workflow
```

## Team collaboration

Team members can claim an entire workstream or specific subtasks through GitHub Issues:

**[A Desktop UI](../../issues/1)** · **[B NLP](../../issues/2)** · **[C Task Memory](../../issues/3)** · **[D Delegation](../../issues/4)** · **[E Evaluation](../../issues/5)** · **[F Contracts & Integration](../../issues/6)**

[All open tasks](https://github.com/Ir1svanquish/IntentAware-Agent/issues) · [Claiming & acceptance guide](docs/WORKSTREAMS.en.md) · [Development TODO](TODO.en.md) · [Contributing guide](CONTRIBUTING.en.md)

## Data and privacy

Only use user-supplied or explicitly approved context. Keep API keys in local environment variables and avoid identifiable personal data in study records.
