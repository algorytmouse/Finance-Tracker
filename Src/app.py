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
        self.setCentralWidget(main_layout)

        # initialize EventHandler -> also Loads DatabaseHandler and passes in main_layout
        EventHandler().main_layout = main_layout

        main_menu = MainMenu()
        main_layout.addWidget(main_menu)
        finances_site = FinancesSite()
        main_layout.addWidget(finances_site)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
