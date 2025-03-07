"""
----------------------------------------------------------------------------------------
 file: app.py

 ----------------------------------------------------------------------------------------

              - ALGORYTMOUSE -

 ----------------------------------------------------------------------------------------

 - Project: Finance-Tracker
 - Author: C.Ceylan
 - Date: 07.03.2025

 ----------------------------------------------------------------------------------------
 """

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget

from Src.Controller.event_handler import EventHandler
from Src.View.main_menu import MainMenu
from Src.View.finances_site import FinancesSite
from Src.widget_types import WidgetTypes


class MainWindow(QMainWindow):
    """
    Class: MainWindow
    this class sets up the user interface and initializes the Event Handling

    Attributes:
    None
    """

    def __init__(self) -> None:
        super().__init__()

        self.setMinimumSize(600, 480)

        main_layout = QStackedWidget()
        EventHandler().app_widgets[WidgetTypes.MAIN_LAYOUT] = main_layout
        self.setCentralWidget(main_layout)

        main_menu = MainMenu()
        EventHandler().app_widgets[WidgetTypes.MAIN_MENU] = main_menu
        main_layout.addWidget(main_menu)

        finances_site = FinancesSite()
        EventHandler().app_widgets[WidgetTypes.FINANCES] = finances_site
        main_layout.addWidget(finances_site)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
