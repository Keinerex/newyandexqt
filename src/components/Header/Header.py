from PyQt5.QtWidgets import QWidget

from src.components.Header.header_style import Ui_Form

class Header(QWidget, Ui_Form):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)

