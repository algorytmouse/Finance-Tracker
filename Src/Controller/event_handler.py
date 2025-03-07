"""
----------------------------------------------------------------------------------------
 file: event_handler.py

 ----------------------------------------------------------------------------------------

              - ALGORYTMOUSE -

 ----------------------------------------------------------------------------------------

 - Project: Finance-Tracker
 - Author: C.Ceylan
 - Date: 07.03.2025
 - Description: Media Path Manager

 ----------------------------------------------------------------------------------------
 """

from typing import Optional

from PySide6.QtWidgets import QStackedWidget

from Src.Model.database_handler import DatabaseHandler
from Src.singleton import Singleton
from Src.View.menu_types import MenuTypes


class EventHandler(Singleton):
    """
    Class: MainWindow
    this class sets manages all events and communicates with the Model

    Attributes:
    None
    """

    def __init__(self) -> None:
        if not hasattr(self, "_initialized"):
            self.db = DatabaseHandler()
            self.main_layout: Optional[QStackedWidget] = None
            EventHandler._initialized = True

    def menu_btn_clicked(self, menu_type: MenuTypes) -> None:
        """
        Slot for Menu Button Clicked Event

        :return: None
        :rtype: None
        """

        if self.main_layout is None:
            print("Main Layout does not exist")
            return None

        match menu_type:
            case MenuTypes.FINANCES:
                self.main_layout.setCurrentIndex(1)
            case _:
                print("Menu Type does not exist!")
