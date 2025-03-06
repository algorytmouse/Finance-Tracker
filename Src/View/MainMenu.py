from PySide6.QtWidgets import QWidget, QVBoxLayout


class MainMenu(QWidget):

    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
