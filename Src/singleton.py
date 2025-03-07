"""
----------------------------------------------------------------------------------------
 file: singleton.py

 ----------------------------------------------------------------------------------------

              - ALGORYTMOUSE -

 ----------------------------------------------------------------------------------------

 - Project: Finance-Tracker
 - Author: C.Ceylan
 - Date: 07.03.2025

 ----------------------------------------------------------------------------------------
 """

class Singleton():
    """
    Class: Singleton
    template to inherit Singleton pattern into other classes

     Attributes:
       None
       """

    _instance = None

    def __new__(cls, *args, **kwargs) -> object:
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance
