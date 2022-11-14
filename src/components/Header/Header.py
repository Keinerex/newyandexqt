from PyQt5.QtWidgets import QWidget

from src.components.Header.header_style import Ui_Form


# Верхняя панель навигации
class Header(QWidget, Ui_Form):
    # Инициализация
    def __init__(self, parent):
        super().__init__(parent)
        # Инициализация стилей
        self.setupUi(self)
