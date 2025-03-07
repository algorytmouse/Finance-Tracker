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

        self.main_layout = QStackedWidget()
        self.setCentralWidget(self.main_layout)

        # initialize EventHandler -> also Loads DatabaseHandler
        EventHandler()

        self.main_menu = MainMenu()
        self.main_layout.addWidget(self.main_menu)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
