Language / 语言：[简体中文（GitHub Issue）](https://github.com/Ir1svanquish/IntentAware-Agent/issues/2) | **English**

# B — Goal & Intent NLP

> Four-week **PySide6 + Python + SQLite** desktop MVP. Replacing the browser-extension approach from the submitted proposal requires supervisor approval. No role is assigned by default.

## Scope

Structured goal clarification and contextual four-category activity inference with reasons using a replaceable LLM adapter.

## Implementation guidance

Agree on Goal/ActivityContext/Classification types; version prompts and model settings; implement direct_progress, necessary_preparation, optional_exploration, unclear; avoid false prompts; coordinate keyword baseline.

## Deliverables

Code and documentation under `src/intentaware/nlp/` (planned), with setup steps, mock fixtures and runnable tests. Record dependencies and any limitations.

## Acceptance criteria

Valid structured output and cases for each label; context-sensitive results across different goals; uncertainty handled; batch tests and held-out split are reproducible.

**Every contribution also requires** a reproducible normal and failure test, compatible shared interfaces, no unapproved data or secrets, and PR review by another member.

## How to claim

Comment on the [corresponding Issue](https://github.com/Ir1svanquish/IntentAware-Agent/issues/2) with your chosen module or subtask, scope, deliverable and dependencies. A maintainer confirms assignment; multiple contributors can split the task.

**Suggested branch:** `feature/intent-nlp`

[English overview](../WORKSTREAMS.en.md) · [中文总指南](../WORKSTREAMS.md)
