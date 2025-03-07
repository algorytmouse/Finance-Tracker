from PySide6.QtWidgets import QPushButton, QHBoxLayout
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import QSize

from Src.MediaPaths import ICONS


class MenuButton(QPushButton):

    def __init__(self, icon_type):
        super().__init__()

        layout = QHBoxLayout()
        self.setLayout(layout)

        icon = QIcon(ICONS[icon_type])
        self.setIcon(icon)
        self.setIconSize(QSize(100, 100))
