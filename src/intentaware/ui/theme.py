"""Desktop typography and colors, using fonts available on the system."""

from PySide6.QtGui import QFontDatabase
from PySide6.QtWidgets import QWidget


def apply_theme(window: QWidget) -> None:
    font = window.font()
    available = set(QFontDatabase.families())
    for family in ("PingFang SC", "Microsoft YaHei UI", "Microsoft YaHei", "Noto Sans CJK SC"):
        if family in available:
            font.setFamily(family)
            break
    font.setPointSize(10)
    window.setFont(font)
    window.setStyleSheet("""
        QWidget { color: #1E293B; }
        QWidget#workbench, QScrollArea { background: #F1F5F9; }
        QFrame#header, QFrame#panel, QFrame#footer { background: #FFFFFF; }
        QFrame#header { border-bottom: 1px solid #DCE4ED; }
        QFrame#panel { border: 1px solid #DCE4ED; border-radius: 9px; }
        QFrame#footer { border-top: 1px solid #DCE4ED; }
        QLabel#brand { font-size: 21px; font-weight: 700; color: #0F766E; }
        QLabel#workbenchTitle { font-size: 16px; font-weight: 600; }
        QLabel#offlineMode {
            background: #E6F4F1; color: #115E59; border-radius: 5px; padding: 4px 9px;
        }
        QLabel[role="heading"] { font-size: 16px; font-weight: 700; }
        QLabel[role="muted"] { color: #475569; }
        QLabel[role="feedback"] {
            background: #F1F5F9; color: #334155; border-radius: 5px; padding: 8px 10px;
        }
        QLabel#status_label { color: #334155; }
        QLabel#status_label[error="true"] { color: #9F1239; }
        QLineEdit, QPlainTextEdit, QListWidget, QComboBox {
            background: #FFFFFF; color: #1E293B; border: 1px solid #CBD5E1; border-radius: 5px;
            selection-background-color: #CCFBF1; selection-color: #134E4A;
        }
        QLineEdit, QComboBox { min-height: 24px; padding: 4px 8px; }
        QPlainTextEdit { padding: 4px; }
        QListWidget::item { padding: 5px 7px; }
        QLineEdit:focus, QPlainTextEdit:focus, QListWidget:focus, QComboBox:focus {
            border: 1px solid #0F766E;
        }
        QLineEdit:disabled, QPlainTextEdit:disabled, QListWidget:disabled {
            background: #F1F5F9; color: #64748B;
        }
        QPushButton {
            min-height: 24px; padding: 4px 12px; border-radius: 5px; border: 1px solid #CBD5E1;
            background: #FFFFFF; color: #334155; font-weight: 600;
        }
        QPushButton:hover { background: #F0FDFA; border-color: #0F766E; }
        QPushButton[primary="true"] { background: #0F766E; border-color: #0F766E; color: #FFFFFF; }
        QPushButton[primary="true"]:hover, QPushButton[primary="true"]:pressed { background: #115E59; }
        QPushButton:focus, QPushButton[primary="true"]:focus { border: 2px solid #134E4A; padding: 3px 11px; }
        QPushButton:disabled, QPushButton[primary="true"]:disabled {
            background: #F1F5F9; border-color: #E2E8F0; color: #64748B;
        }
        QTabWidget::pane { background: #FFFFFF; border: 1px solid #DCE4ED; border-radius: 5px; }
        QTabBar::tab {
            background: #E8EEF4; color: #475569; border: 1px solid #DCE4ED;
            border-top-left-radius: 5px; border-top-right-radius: 5px; padding: 8px 13px; margin-right: 3px;
        }
        QTabBar::tab:selected { background: #FFFFFF; color: #115E59; font-weight: 700; }
        QTabBar::tab:focus { border-color: #0F766E; }
    """)
