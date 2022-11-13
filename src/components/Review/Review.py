from PyQt5.QtWidgets import QFrame

from src.components.Review.review_style import Ui_Form


class Review(QFrame, Ui_Form):
    def __init__(self, user, text, rate, parent=None):
        super().__init__(parent)
        self.setupUi(self, user, text, rate)
