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

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QLineEdit, QPushButton

from Src.media_paths import ICONS


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

        label = QLabel()
        layout.addWidget(label)

        user_input = QLineEdit()
        layout.addWidget(user_input)

        delete_btn = QPushButton()
        delete_btn.setIcon(QIcon(ICONS.get("delete_icon")))
        delete_btn.setIconSize(QSize(100, 100))
        layout.addWidget(delete_btn)
