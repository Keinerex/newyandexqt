
from PyQt5.QtWidgets import QWidget

from src.components.Star.star_style import Ui_Form


class Star(QWidget, Ui_Form):
    def __init__(self, parent, type=""):
        super().__init__(parent)
        self.setupUi(self, type=type)