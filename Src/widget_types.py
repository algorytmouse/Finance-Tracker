"""
----------------------------------------------------------------------------------------
 file: widget_types.py

 ----------------------------------------------------------------------------------------

              - ALGORYTMOUSE -

 ----------------------------------------------------------------------------------------

 - Project: Finance-Tracker
 - Author: C.Ceylan
 - Date: 07.03.2025

 ----------------------------------------------------------------------------------------
 """

from enum import Enum


class WidgetTypes(Enum):
    """
    Class: WidgetTypes
    Provides Enum for different Widget Types (Main Pages) within the application

    Attributes:
    None
    """

    MAIN_LAYOUT: str = "main layout as stacked widget"
    MAIN_MENU: str = "main menu"
    FINANCES: str = "finances submenu"
