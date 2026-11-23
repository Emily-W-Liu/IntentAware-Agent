"""A predictable local data location, with an explicit override for development."""

import os
import sys
from pathlib import Path


def default_data_dir() -> Path:
    override = os.environ.get("INTENTAWARE_DATA_DIR")
    if override:
        return Path(override).expanduser()
    if sys.platform == "win32":
        base = Path(os.environ.get("LOCALAPPDATA", Path.home() / "AppData" / "Local"))
    elif sys.platform == "darwin":
        base = Path.home() / "Library" / "Application Support"
    else:
        base = Path(os.environ.get("XDG_DATA_HOME", Path.home() / ".local" / "share"))
    return base / "IntentAware"
