from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from Src.View.MainMenu import MainMenu
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(600, 480)

        self.main_layout = QStackedWidget()
        self.setCentralWidget(self.main_layout)

        self.main_menu = MainMenu()
        self.main_layout.addWidget(self.main_menu)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
