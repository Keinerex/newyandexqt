from PyQt5.QtWidgets import QWidget
from pyqt5_plugins.examplebuttonplugin import QtGui

from src.pages.CartPage.cartpage_style import Ui_Form


class CartPage(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def mouseMoveEvent(self, a0: QtGui.QMouseEvent) -> None:
        self.books_widget.rerender()
