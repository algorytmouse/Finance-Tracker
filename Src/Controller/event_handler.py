"""
----------------------------------------------------------------------------------------
 file: event_handler.py

 ----------------------------------------------------------------------------------------

              - ALGORYTMOUSE -

 ----------------------------------------------------------------------------------------

 - Project: Finance-Tracker
 - Author: C.Ceylan
 - Date: 07.03.2025

 ----------------------------------------------------------------------------------------
 """

from Src.Model.database_handler import DatabaseHandler
from Src.singleton import Singleton
from Src.widget_types import WidgetTypes


class EventHandler(Singleton):
    """
    Class: MainWindow
    this class sets manages all events and communicates with the Model

    Attributes:
    None
    """

    app_widgets = {}

    def __init__(self) -> None:
        if not hasattr(self, "_initialized"):
            self.db = DatabaseHandler()
            EventHandler._initialized = True

    def menu_btn_clicked(self, menu_type: WidgetTypes) -> None:
        """
        Slot for Menu Button Clicked Event

        :return: None
        :rtype: None
        """

        if EventHandler.app_widgets.get(WidgetTypes.MAIN_LAYOUT, None) is None:
            print("Main Layout does not exist")
            return None

        # handle signal based on what button click triggered it
        match menu_type:
            case WidgetTypes.MAIN_MENU:
                EventHandler.app_widgets.get(WidgetTypes.MAIN_LAYOUT).setCurrentWidget(
                    EventHandler.app_widgets.get(menu_type))
            case WidgetTypes.FINANCES:
                EventHandler.app_widgets.get(WidgetTypes.MAIN_LAYOUT).setCurrentWidget(
                    EventHandler.app_widgets.get(menu_type))
            case _:
                print("Menu Type does not exist!")