Language / 语言：[简体中文](WORKSTREAMS.md) | **English**

# Open Workstream Claiming Guide

**HKU COMP7607 NLP · Group 14 · IntentAware-Agent**

This page organizes work based on the submitted proposal. Technical implementation details and acceptance examples are team suggestions, **not yet approved by every member**. The repository currently has documentation and placeholder directories only.

## How to claim a workstream

1. Browse the [GitHub Issues](https://github.com/Ir1svanquish/IntentAware-Agent/issues) and choose a workstream.
2. Read the Issue scope, dependencies, deliverables, and acceptance checklist; check existing claims.
3. Comment: `I'd like to claim [module/subtask]; my scope is [scope]; I need coordination on [API/teammate]`. **You do not have to own an entire module**; workstreams can be split among collaborators.
4. A maintainer can add you as an Assignee, or you can self-assign if permitted. Until permissions are set, the Issue comment is the agreed claim record.
5. Agree on API/data contracts first. Create a `feature/<topic>` branch from `main`, then submit a Pull Request. Use `Closes #number` only once all acceptance items are actually met.
6. Have another teammate reproduce the checks before merge; keep unmet requirements open and documented.

**Avoid conflicts:** Multiple people may share an Issue with one coordinator; split work into clear subtasks in the comments. Creating Issues does not automatically assign them.

## Recommended workstreams

| Stream | Focus | Key dependency | Proposed location |
| --- | --- | --- | --- |
| A Extension & UX | React sidebar, approved page context, reminders and controls | F API contract | `apps/extension/` |
| B NLP Intent | Goal clarification, four-category context classification, rationale, prompts and baseline | F schema | `services/backend/app/modules/goals/`, `intent/` |
| C Task Memory | Detour capture, progress records, concrete resumption advice | Goal model and F contract | `services/backend/app/modules/memory/` |
| D Delegation | Editable request, source checking, worker, delivery timing | F contract and extension controls | `services/backend/app/modules/delegation/`, `delivery/` |
| E Evaluation | G/P/I/D, annotations, baseline, event logging, pilot and analysis | All modules; define logs early | `experiments/`, `tests/` |

There is also **F Shared Contracts & Integration**. All members should review it, with a volunteer coordinator. Locations are proposed and may change by team agreement.

## Contracts to agree on first

At minimum define `Goal`, `ActivityContext`, `ActivityClassification`, `Detour`, `DelegationRequest`, `DelegationJob`, `Checkpoint` and `ExperimentEvent`. Supply mock JSON fixtures before APIs are implemented.

- **Classification:** `direct_progress` / `necessary_preparation` / `optional_exploration` / `unclear` with rationale.
- **Delegation:** editable draft → user confirmation (at most one clarification) → background retrieval of up to two public sources → checked answer with sources and unresolved points → immediate or checkpoint delivery; support early view, edit and cancel.
- **Conditions:** G=goal-aware reminders; P=G+detour capture/resumption; I=P+delegation with immediate result; D=P+delegation with checkpoint delivery (early view allowed).
- **Privacy & reliability:** Only use user-approved page excerpts; never commit secrets/private data. Record model/prompt version, latency, token usage and failures; keep participant identities private.

## Definition of Done

- [ ] Code, documentation and tests or reproducible manual checks are included in the PR.
- [ ] Document startup, inputs/outputs and dependencies; label unimplemented features accurately.
- [ ] Verify a happy path and a failure/boundary case, not screenshots alone.
- [ ] Update contracts and notify dependent owners when an API changes.
- [ ] Keep NLP prompt development data separate from held-out evaluation data and preserve reproducible settings.
- [ ] Preserve G/P/I/D controls and hold model/reminder settings constant where required.
- [ ] Another teammate reviews against acceptance criteria; do not close an Issue with unmet criteria.

## Claim comment template

```text
I'd like to claim: module __ / subtask __
My scope:
Expected deliverable:
Dependencies or coordination needed:
```

See the [master TODO](../TODO.en.md) and [contribution guide](../CONTRIBUTING.en.md).
