"""Start with `python -m intentaware` or the installed `intentaware` command."""

import argparse
import sys
from pathlib import Path

from intentaware import __version__
from intentaware.config import default_data_dir


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="IntentAware 桌面任务助手（离线演示框架）")
    parser.add_argument("--version", action="version", version=f"IntentAware {__version__}")
    parser.add_argument("--demo", action="store_true", help="使用离线演示模块（当前默认模式）")
    parser.add_argument("--data-dir", type=Path, default=default_data_dir(), help="本地数据目录")
    parser.add_argument("--condition", choices=("G", "P", "I", "D"), default="D", help="实验条件，默认 D")
    args = parser.parse_args(argv)

    from PySide6.QtWidgets import QApplication, QMessageBox

    from intentaware.contracts import Condition
    from intentaware.memory.store import SQLiteStore
    from intentaware.session import DesktopSession
    from intentaware.ui.window import MainWindow

    app = QApplication([sys.argv[0]])
    app.setApplicationName("IntentAware")
    app.setOrganizationName("COMP7607-Group14")
    try:
        args.data_dir.mkdir(parents=True, exist_ok=True)
        store = SQLiteStore(args.data_dir / "intentaware.sqlite3")
        session = DesktopSession(store, condition=Condition(args.condition))
    except Exception as exc:
        QMessageBox.critical(None, "无法启动", f"无法打开本地数据目录：\n{args.data_dir}\n\n{exc}")
        return 1
    window = MainWindow(session)
    app.aboutToQuit.connect(session.close)
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
