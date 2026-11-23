Language / 语言：[简体中文](README.md) | **English**

# PySide6 desktop source

After installing the project from the repository root, run `python -m intentaware --demo` to open the Chinese-language app. The default classifier and delegator work offline. SQLite stores goals, progress, and detours. Delegation jobs live for the current app session.

- A [Desktop UI](ui/README.md) uses `ui/window.py` to handle input and display results.
- B [Goal and activity classification](nlp/README.md) uses `nlp/demo.py` to classify activities into four categories offline.
- C [Task memory](memory/README.md) uses `memory/store.py` for SQLite storage.
- D [Asynchronous delegation](delegation/README.md) uses `delegation/demo.py` as the offline background provider.
- E [Evaluation](../../experiments/) uses JSONL event exports for each G/P/I/D run.
- F [Contracts and integration](contracts/README.md) maintains `contracts/`, `session.py`, and `__main__.py` for shared types, feature gates, and application setup.

[Run, extend, and test the app (Chinese)](../../docs/GETTING_STARTED.md) · [Home](../../README.en.md) · [Claim work](../../docs/WORKSTREAMS.md)
