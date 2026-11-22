Language / 语言：[简体中文（GitHub Issue）](https://github.com/Ir1svanquish/IntentAware-Agent/issues/5) | **English**

# E — Evaluation & Experiment Runner

> Four-week **PySide6 + Python + SQLite** desktop MVP. Replacing the browser-extension approach from the submitted proposal requires supervisor approval. No role is assigned by default.

## Scope

Preserve G/P/I/D comparisons, logging, annotation, held-out requests, baselines and research analysis.

## Implementation guidance

Create feature flags and counterbalanced tasks; prepare 60 task-context examples reviewed by two reviewers and 40 held-out requests; compute keyword baseline, macro-F1, false-warning, resumption, quality, citation support, latency/tokens; begin consent/ethics planning immediately.

## Deliverables

Code and documentation under `experiments/` (planned), with setup steps, mock fixtures and runnable tests. Record dependencies and any limitations.

## Acceptance criteria

Reproducible analysis with labeled synthetic fixtures; experimental controls held fixed; meaningful main-task edit measured rather than a return-button proxy; consent/ethics checks before study; no invented results.

**Every contribution also requires** a reproducible normal and failure test, compatible shared interfaces, no unapproved data or secrets, and PR review by another member.

## How to claim

Comment on the [corresponding Issue](https://github.com/Ir1svanquish/IntentAware-Agent/issues/5) with your chosen module or subtask, scope, deliverable and dependencies. A maintainer confirms assignment; multiple contributors can split the task.

**Suggested branch:** `feature/evaluation`

[English overview](../WORKSTREAMS.en.md) · [中文总指南](../WORKSTREAMS.md)
