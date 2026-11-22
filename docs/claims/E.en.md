# E — Evaluation & Experiment Runner

[简体中文（GitHub Issue）](https://github.com/Ir1svanquish/IntentAware-Agent/issues/5) | **English**

## Scope
Implement the proposal's controlled G/P/I/D conditions, reproducible logging, task materials, baselines and analysis. Participant recruitment, review and reporting remain shared group work.

## Implementation guide
1. Implement G goal reminders; P adds detour/resumption; I adds immediate delegation; D changes delivery to a checkpoint while allowing early view. Preserve fixed goal interpretation/reminder rules and I/D model/source/format parity.
2. Prepare four comparable browser tasks, matched side questions and a counterbalanced order.
3. Define event logs for interruptions, the next meaningful main-task edit, non-resumption, early view and cancellations.
4. Prepare 60 task-context examples for review by two reviewers and 40 held-out delegation requests excluded from prompt development.
5. Implement keyword baseline, macro-F1, false-warning rate, outcome quality, evidence checks, perceived burden, latency and token usage metrics.
6. Check research ethics/consent, run a pilot and support the planned 12–18-adult within-participant study.

## Deliverables
Experiment protocol, stimuli, de-identified data schema, event logging, evaluation scripts, reproducible analysis instructions, report templates.

## Acceptance checklist
- [ ] All four conditions run in one system according to the proposal.
- [ ] Every metric has a precise computation, particularly resumption time and non-resumption.
- [ ] Clearly labeled synthetic fixtures run the entire analysis pipeline; no experimental results are fabricated.
- [ ] Prompt-development and held-out samples are separated and documented.
- [ ] Pilot, consent and data-protection checks are completed before the participant study.

**Dependencies:** A–D, F event contracts. **Branch:** `feature/experiment-runner`.
