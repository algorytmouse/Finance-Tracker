"""
----------------------------------------------------------------------------------------
 file: finances_widget.py

 ----------------------------------------------------------------------------------------

              - ALGORYTMOUSE -

 ----------------------------------------------------------------------------------------

 - Project: Finance-Tracker
 - Author: C.Ceylan
 - Date: 07.03.2025

 ----------------------------------------------------------------------------------------
 """

from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel


class FinanceWidget(QWidget):
    """
    Class: FinancesWidget
    Field to Add Finance information

    Attributes:
    None
    """

    def __init__(self, finance_type) -> None:
        super().__init__()

        layout = QHBoxLayout()
        self.setLayout(layout)
