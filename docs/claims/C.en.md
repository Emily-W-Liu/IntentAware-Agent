# C — Detour Memory & Task Resumption

[简体中文（GitHub Issue）](https://github.com/Ir1svanquish/IntentAware-Agent/issues/3) | **English**

## Scope
Save approved detours, their purposes, user-confirmed progress, and unfinished steps; offer actionable guidance when the user returns to the main task.

## Implementation guide
1. Agree with F on Goal, Detour, Progress and ResumeSuggestion schemas.
2. Implement add/edit/read/delete for saved links, notes and the reason for capturing each item.
3. Store confirmed progress rather than inferring completion merely from page navigation.
4. Derive concrete next steps (for example, “write the closing paragraph”) from known state.
5. Support edit, dismiss, pause, throttled reminders, and cases where exploration is necessary to the goal.
6. Test empty/error states and behavior after the agreed session restart lifecycle.

## Deliverables
`services/backend/app/modules/memory/`, persistence adapter, API examples, unit tests, state-transition notes, and privacy explanation.

## Acceptance checklist
- [ ] Detour create/read/update/delete flows are reproducible.
- [ ] Progress can be recovered across the agreed session lifecycle.
- [ ] Resumption suggestions are grounded in confirmed goal, progress and remaining steps.
- [ ] Pause/dismiss works without interfering with necessary preparation.
- [ ] Happy path and error tests plus a data-privacy note are included.

**Dependencies:** F persistence/API contract, B goal model, A UI. **Branch:** `feature/task-memory`.
