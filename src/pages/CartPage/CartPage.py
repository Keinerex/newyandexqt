from PyQt5.QtWidgets import QWidget

from src.pages.CartPage.cartpage_style import Ui_Form


# Страницы корзины
class CartPage(QWidget, Ui_Form):
    # Инициализация
    def __init__(self, parent=None):
        super().__init__(parent)
        # Инициализация стилей
        self.setupUi(self)
