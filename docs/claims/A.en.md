Language / 语言：[简体中文（GitHub Issue）](https://github.com/Ir1svanquish/IntentAware-Agent/issues/1) | **English**

# A — Desktop UI & UX

> Four-week **PySide6 + Python + SQLite** desktop MVP. Replacing the browser-extension approach from the submitted proposal requires supervisor approval. No role is assigned by default.

## Scope

PySide6 main window with manually entered/approved goal and context, four-class explanation, detour management, resumption, delegation and checkpoint controls.

## Implementation guidance

Bootstrap a runnable Python desktop entry point; implement context/goal forms; show output and error/loading states; use shared F contracts/mock fixtures; never automatically read Word/VS Code/browser content.

## Deliverables

Code and documentation under `src/intentaware/ui/` (planned), with setup steps, mock fixtures and runnable tests. Record dependencies and any limitations.

## Acceptance criteria

A new developer can run the app; mock goal→classification→detour→resume works; background jobs do not freeze UI; consent and G/P/I/D controls work.

**Every contribution also requires** a reproducible normal and failure test, compatible shared interfaces, no unapproved data or secrets, and PR review by another member.

## How to claim

Comment on the [corresponding Issue](https://github.com/Ir1svanquish/IntentAware-Agent/issues/1) with your chosen module or subtask, scope, deliverable and dependencies. A maintainer confirms assignment; multiple contributors can split the task.

**Suggested branch:** `feature/desktop-ui`

[English overview](../WORKSTREAMS.en.md) · [中文总指南](../WORKSTREAMS.md)
