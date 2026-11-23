Language / 语言：[简体中文](README.md) | **English**

# Tests

Install the development dependencies, then run `python -m pytest` from the repository root.

The suite exercises offline classification, SQLite persistence across restarts, background classification and delegation, cancellation, G/P/I/D feature gates, completion/delivery events, and real Qt widget interactions. Tests use temporary databases and do not call a model or access the internet.

| File | Coverage |
| --- | --- |
| `test_classifier.py` | Classification rules and context |
| `test_storage.py` | Persistence, updates, deletion and export |
| `test_session.py` | Integrated workflow, background jobs, conditions and errors |
| `test_ui.py` | Widget interactions, responsiveness, delivery and layout |

For headless Linux, set `QT_QPA_PLATFORM=offscreen`. [Setup and development guide (Chinese)](../docs/GETTING_STARTED.md)
