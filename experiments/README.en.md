Language / 语言：[简体中文](README.md) | **English**

# Experiments

Retain the proposal's **G/P/I/D** conditions, **60 task-context examples** with two reviewers, **40 held-out delegation requests**, and planned within-participant study with **12–18 adults**. The research has not been completed. Begin preparation in week 1 and satisfy consent and ethics requirements before participant testing.

The desktop observes application names and window titles, then uses local rules to infer tasks and classify activities. `--demo` supplies simulated observations, and delegation remains an offline demonstration. Record the platform, observation mode, and rule or model version. Keep demo data separate from formal evaluation and keep development examples separate from held-out examples.

| Evaluation area | Planned measures or records |
| --- | --- |
| Activity classification | Keyword baseline, macro-F1, false-warning rate; examine uncertainty and human corrections |
| Task performance | Completion, output quality, and time to resume the main task |
| Delegation | Answer quality, source and citation support, and unresolved points |
| Burden and cost | Perceived burden, latency, and token usage; local rules and offline examples do not constitute live-model evaluation |

The experiment page exports JSONL for the current `run_id`. Use `job_id` to distinguish `delegation_completed` (ready in the background) from `delegation_delivered` (delivered). The resume button logs `resume_requested`. Resumption time must end at the **next meaningful main-task edit**. A return click, window switch, or title-based classification cannot substitute for that edit; observe it separately in the controlled study.

Raw ongoing window titles are not appended to event exports. Automatically seeded and user-edited task titles are saved in local task records. Avoid identifiable personal data in study records, and review explicitly saved task, progress, and detour content before sharing.

[Setup guide (Chinese)](../docs/GETTING_STARTED.md) · [Development and evaluation tasks](../TODO.en.md)
