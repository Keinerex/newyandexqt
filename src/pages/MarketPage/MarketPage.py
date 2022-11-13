from PyQt5.QtWidgets import QWidget
from src.pages.MarketPage.marketpage_style import Ui_Form

class MarketPage(QWidget, Ui_Form):
    def __init__(self, book_func, parent=None):
        super().__init__(parent)
        self.setupUi(self, book_func)

