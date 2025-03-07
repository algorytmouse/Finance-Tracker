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

from Src.Model.database_handler import DatabaseHandler
from Src.singleton import Singleton


class EventHandler(Singleton):
    """
    Class: MainWindow
    this class sets manages all events and communicates with the Model

    Attributes:
    None
    """

    def __init__(self) -> None:
        self.db = DatabaseHandler()
