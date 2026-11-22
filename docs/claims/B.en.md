# B — Goal & Intent NLP

[简体中文（GitHub Issue）](https://github.com/Ir1svanquish/IntentAware-Agent/issues/2) | **English**

## Scope
Clarify the user's goal and next action; interpret activities from the goal, confirmed progress, user-approved page excerpts, and task dependencies. This is the central NLP module.

## Implementation guide
1. Define structured goal clarification with concrete outcome, next action, and at most one clarification.
2. Agree on input schema: goal, confirmed progress, page title, approved excerpt, and user-specified dependencies.
3. Output one of `direct_progress`, `necessary_preparation`, `optional_exploration`, or `unclear` with a brief reason.
4. Do not automatically trigger warnings for uncertain cases; allow silence or optional clarification.
5. Version prompts, model and generation settings. Work with E on keyword baseline and ensure held-out evaluation data never leaks into prompt development.

## Deliverables
Modules under `services/backend/app/modules/goals/` and `intent/`, prompt/configuration records, schemas, sample JSON, tests and error analysis.

## Acceptance checklist
- [ ] Valid structured goal and next-action output without inventing completed work.
- [ ] Reproducible examples for all four activity categories, each with reasons.
- [ ] The same CV page yields context-sensitive decisions for different goals/dependencies.
- [ ] Uncertainty is handled conservatively and false prompts can be measured.
- [ ] Reproducible batch evaluation with fixed settings and a keyword baseline.

**Dependencies:** F schemas, E evaluation protocol. **Branch:** `feature/intent-classifier`.
