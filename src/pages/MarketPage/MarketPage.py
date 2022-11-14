from PyQt5.QtWidgets import QWidget

from src.pages.MarketPage.marketpage_style import Ui_Form


# Страница магазина
class MarketPage(QWidget, Ui_Form):
    # Инициализация
    def __init__(self, book_func, parent=None):
        super().__init__(parent)
        # Инициализация стилей
        self.setupUi(self, book_func)
