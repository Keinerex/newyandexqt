from PyQt5.QtWidgets import QWidget

from src.components.Star.star_style import Ui_Form


# Кружок рейтинга
class Star(QWidget, Ui_Form):
    # Инициализация
    def __init__(self, parent, star_type=""):
        super().__init__(parent)
        # Инициализация стилей
        self.setupUi(self, type=star_type)
