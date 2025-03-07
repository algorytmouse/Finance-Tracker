"""
----------------------------------------------------------------------------------------
 file: main_menu.py

 ----------------------------------------------------------------------------------------

              - ALGORYTMOUSE -

 ----------------------------------------------------------------------------------------

 - Project: Finance-Tracker
 - Author: C.Ceylan
 - Date: 07.03.2025

 ----------------------------------------------------------------------------------------
 """

from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtGui import Qt

from Src.View.Widgets.menu_button import MenuButton

class MainMenu(QWidget):
    """
    Class: MainMenu
    Initializes the Main Menu

    Attributes:
    None
    """

    def __init__(self) -> None:
        super().__init__()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        finances_btn = MenuButton(icon_type="finances_icon")
        self.layout.addWidget(finances_btn, alignment=Qt.AlignmentFlag.AlignAbsolute)

        #finances_btn.setMaximumWidth(self.width() * 0.5)
