"""
----------------------------------------------------------------------------------------
 file: finances_site.py

 ----------------------------------------------------------------------------------------

              - ALGORYTMOUSE -

 ----------------------------------------------------------------------------------------

 - Project: Finance-Tracker
 - Author: C.Ceylan
 - Date: 07.03.2025

 ----------------------------------------------------------------------------------------
 """

from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PySide6.QtGui import QIcon, Qt
from PySide6.QtCore import QSize

from Src.media_paths import ICONS
from Src.Controller.event_handler import EventHandler
from Src.widget_types import WidgetTypes

class FinancesSite(QWidget):
    """
    Class: FinancesSite
    Site for managing and calculating your Finances

    Attributes:
    None
    """

    def __init__(self) -> None:
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        back_btn = QPushButton()
        back_btn.setIcon(QIcon(ICONS.get("back_arrow_icon")))
        back_btn.setIconSize(QSize(50,50))
        layout.addWidget(back_btn, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        back_btn.clicked.connect(lambda: EventHandler().menu_btn_clicked(WidgetTypes.MAIN_MENU))

        #create Vertical Layout where finance input fields are added dynamically
        finances_input_widgets = QWidget()
        finances_input_layout = QVBoxLayout()
        finances_input_widgets.setLayout(finances_input_layout)
        layout.addWidget(finances_input_widgets)

        add_btn = QPushButton()
        add_btn.setIcon(QIcon(ICONS.get("add_icon")))
        add_btn.setIconSize(QSize(50,50))
        layout.addWidget(add_btn)
