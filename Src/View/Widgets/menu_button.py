"""
----------------------------------------------------------------------------------------
 file: media_paths.py

 ----------------------------------------------------------------------------------------

              - ALGORYTMOUSE -

 ----------------------------------------------------------------------------------------

 - Project: Finance-Tracker
 - Author: C.Ceylan
 - Date: 07.03.2025
 - Description: Media Path Manager

 ----------------------------------------------------------------------------------------
 """

from PySide6.QtWidgets import QPushButton, QHBoxLayout
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize

from Src.media_paths import ICONS
from Src.Controller.event_handler import EventHandler
from Src.View.menu_types import MenuTypes


class MenuButton(QPushButton):
    """
    Class: MenuButton
    Template Widget for a Menu Button

    Attributes:
    icon_type -> string
    """

    def __init__(self, icon_type: str) -> None:
        super().__init__()

        layout = QHBoxLayout()
        self.setLayout(layout)

        icon = QIcon(ICONS[icon_type])
        self.setIcon(icon)
        self.setIconSize(QSize(100, 100))

        self.clicked.connect(lambda: EventHandler().menu_btn_clicked(menu_type=MenuTypes.FINANCES))
