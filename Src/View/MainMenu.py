from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtGui import Qt

from Src.View.Widgets.MenuButton import MenuButton


class MainMenu(QWidget):

    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        expenses_btn = MenuButton(icon_type="expenses_icon")
        self.layout.addWidget(expenses_btn, alignment=Qt.AlignmentFlag.AlignAbsolute)

        expenses_btn.setMaximumWidth(self.width() * 0.5)
