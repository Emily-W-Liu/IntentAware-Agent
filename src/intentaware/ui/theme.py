"""A quiet desktop palette with native CJK fonts and visible focus states."""

from PySide6.QtGui import QFontDatabase
from PySide6.QtWidgets import QWidget


COLORS = {
    "canvas": "#F5F6F8", "surface": "#FFFFFF", "sidebar": "#192338",
    "sidebar_hover": "#263249", "sidebar_selected": "#34436A",
    "text": "#20283D", "muted": "#606B80", "border": "#E1E5ED",
    "input_border": "#B9C3D3", "accent": "#4D5DC6", "accent_hover": "#3E4EAF",
    "accent_light": "#F0F2FE", "positive": "#277364", "positive_light": "#EDF7F3",
    "warning": "#845C23", "warning_light": "#FBF4E7", "error": "#A1394A",
}


def apply_theme(window: QWidget) -> None:
    font = window.font()
    available = set(QFontDatabase.families())
    for family in ("Microsoft YaHei UI", "PingFang SC", "Noto Sans CJK SC", "Microsoft YaHei"):
        if family in available:
            font.setFamily(family)
            break
    font.setPointSize(10)
    window.setFont(font)
    window.setStyleSheet("""
        QWidget { color: %(text)s; }
        QMainWindow, QWidget#workbench, QWidget#canvas, QScrollArea, QStackedWidget {
            background: %(canvas)s;
        }
        QScrollArea { border: none; }
        QFrame#sidebar { background: %(sidebar)s; border: none; }
        QLabel#brand { color: #F6F8FF; font-size: 19px; font-weight: 700; }
        QLabel#brandCaption { color: #B4BFD4; font-size: 12px; }
        QLabel#sidebarSection { color: #A9B6CD; font-size: 11px; }
        QLabel#sidebarFootnote { color: #B4BFD4; font-size: 12px; }
        QLabel#sidebarMode { color: #E2E7F3; font-size: 13px; font-weight: 600; }
        QPushButton[nav="true"] {
            text-align: left; color: #C8D1E3; border: 1px solid transparent;
            background: transparent; padding: 11px 14px; border-radius: 8px;
            min-height: 22px; font-size: 14px; font-weight: 500;
        }
        QPushButton[nav="true"]:hover { background: %(sidebar_hover)s; color: #FFFFFF; }
        QPushButton[nav="true"]:checked {
            background: %(sidebar_selected)s; color: #FFFFFF; font-weight: 600;
        }
        QPushButton[nav="true"]:focus { border-color: #B6C4FF; }
        QFrame#pageHeader { background: %(canvas)s; }
        QLabel#pageTitle { font-size: 25px; font-weight: 700; }
        QLabel#pageSubtitle { color: %(muted)s; font-size: 12px; }
        QFrame#card, QFrame#taskCard {
            background: %(surface)s; border: 1px solid %(border)s; border-radius: 12px;
        }
        QFrame#suggestionCard {
            background: %(accent_light)s; border: 1px solid #DCE1FA; border-radius: 10px;
        }
        QFrame#nextStep { background: #F6F7FC; border: none; border-radius: 9px; }
        QFrame#line { background: %(border)s; border: none; max-height: 1px; }
        QLabel { background: transparent; }
        QLabel[role="heading"] { font-size: 15px; font-weight: 600; }
        QLabel[role="eyebrow"] { color: %(muted)s; font-size: 12px; font-weight: 600; }
        QLabel[role="muted"] { color: %(muted)s; font-size: 12px; }
        QLabel[role="body"] { color: #434E64; font-size: 13px; }
        QLabel[role="field"] { color: #46516A; font-size: 12px; font-weight: 600; }
        QLabel[role="error"] { color: %(error)s; font-size: 12px; }
        QLabel[role="notice"] {
            color: %(warning)s; background: %(warning_light)s; padding: 12px 14px; border-radius: 8px;
        }
        QLabel#taskTitle { font-size: 28px; font-weight: 700; color: #1E2941; }
        QLabel#taskNextStep { font-size: 15px; font-weight: 500; color: #334164; }
        QLabel#activityTitle { font-size: 17px; font-weight: 600; }
        QLabel#classificationTitle { font-size: 19px; font-weight: 600; color: %(accent)s; }
        QLabel#suggestionTitle { font-size: 15px; font-weight: 600; }
        QLabel#emptyTitle { font-size: 18px; font-weight: 600; }
        QLabel[role="badge"] {
            color: %(muted)s; background: #EEF1F6; border-radius: 5px;
            padding: 4px 8px; font-size: 11px; font-weight: 500;
        }
        QLabel[role="badge"][tone="active"] { color: %(positive)s; background: %(positive_light)s; }
        QLabel[role="badge"][tone="accent"] { color: %(accent)s; background: %(accent_light)s; }
        QLabel[role="badge"][tone="warning"] { color: %(warning)s; background: %(warning_light)s; }
        QLineEdit, QPlainTextEdit, QListWidget, QComboBox {
            background: %(surface)s; color: %(text)s; border: 1px solid %(input_border)s;
            border-radius: 7px; selection-background-color: #DFE4FF; selection-color: #293C82;
        }
        QLineEdit, QComboBox { min-height: 24px; padding: 7px 10px; }
        QPlainTextEdit { padding: 8px; }
        QListWidget { border-color: %(border)s; padding: 4px; outline: none; }
        QListWidget::item { padding: 12px 10px; border-bottom: 1px solid #EFF1F5; }
        QListWidget::item:selected { background: %(accent_light)s; color: #34459A; border-radius: 5px; }
        QLineEdit:focus, QPlainTextEdit:focus, QListWidget:focus, QComboBox:focus {
            border: 1px solid %(accent)s;
        }
        QLineEdit:disabled, QPlainTextEdit:disabled, QListWidget:disabled, QComboBox:disabled {
            background: #F1F3F7; color: #717C90; border-color: %(border)s;
        }
        QPushButton {
            min-height: 22px; padding: 8px 13px; border-radius: 7px; border: 1px solid %(input_border)s;
            background: %(surface)s; color: #43506B; font-weight: 500;
        }
        QPushButton:hover { background: #F4F6FE; border-color: #8290CC; }
        QPushButton:pressed { background: #E8ECFC; }
        QPushButton[primary="true"] {
            background: %(accent)s; border-color: %(accent)s; color: #FFFFFF; font-weight: 600;
        }
        QPushButton[primary="true"]:hover { background: %(accent_hover)s; border-color: %(accent_hover)s; }
        QPushButton[primary="true"]:pressed { background: #33439B; }
        QPushButton[quiet="true"] { border-color: transparent; color: %(accent)s; background: transparent; }
        QPushButton[quiet="true"]:hover { background: %(accent_light)s; }
        QPushButton:focus { border: 2px solid #5368BB; padding: 7px 12px; }
        QPushButton[primary="true"]:focus { border-color: #1F2F77; }
        QPushButton:disabled, QPushButton[primary="true"]:disabled {
            color: #798499; background: #F1F3F7; border-color: %(border)s;
        }
        QPushButton#manualToggle { text-align: left; padding-left: 0; color: %(muted)s; }
        QFrame#footer { background: %(canvas)s; border-top: 1px solid %(border)s; }
        QLabel#status_label { color: %(muted)s; font-size: 11px; }
        QLabel#status_label[error="true"] { color: %(error)s; }
        QScrollBar:vertical { width: 8px; background: transparent; margin: 2px; }
        QScrollBar::handle:vertical { background: #C5CDDB; border-radius: 3px; min-height: 24px; }
        QScrollBar::handle:vertical:hover { background: #9EAAC0; }
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { height: 0; }
        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical { background: transparent; }
        QToolTip { color: %(text)s; background: %(surface)s; border: 1px solid %(border)s; padding: 6px; }
    """ % COLORS)
