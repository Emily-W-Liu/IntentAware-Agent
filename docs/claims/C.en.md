Language / 语言：[简体中文（GitHub Issue）](https://github.com/Ir1svanquish/IntentAware-Agent/issues/3) | **English**

# C — SQLite Memory & Resumption

> Four-week **PySide6 + Python + SQLite** desktop MVP. Replacing the browser-extension approach from the submitted proposal requires supervisor approval. No role is assigned by default.

## Scope

Detour capture and persisted user-confirmed task progress, with concrete resumption advice.

## Implementation guidance

Define SQLite schema and CRUD for links, notes and purposes; store confirmed progress/unfinished steps; implement suggestion, pause and dismiss; handle restart and invalid data.

## Deliverables

Code and documentation under `src/intentaware/memory/` (planned), with setup steps, mock fixtures and runnable tests. Record dependencies and any limitations.

## Acceptance criteria

CRUD and restart behavior demonstrated; suggestions grounded in confirmed data; normal/error tests; no automatic claim that external work was edited.

**Every contribution also requires** a reproducible normal and failure test, compatible shared interfaces, no unapproved data or secrets, and PR review by another member.

## How to claim

Comment on the [corresponding Issue](https://github.com/Ir1svanquish/IntentAware-Agent/issues/3) with your chosen module or subtask, scope, deliverable and dependencies. A maintainer confirms assignment; multiple contributors can split the task.

**Suggested branch:** `feature/task-memory`

[English overview](../WORKSTREAMS.en.md) · [中文总指南](../WORKSTREAMS.md)
