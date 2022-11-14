from sqlite3 import connect

from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QWidget, QPushButton

from src.components.Navigation.navigation_style import Ui_Form


# Панель навигации категорий товаров
class Navigation(QWidget, Ui_Form):
    # Инициализация
    def __init__(self, parent, active_category):
        super().__init__(parent)
        # Инициализация стилей
        self.setupUi(self)
        # Получение категорий из базы
        con = connect("base.db")
        cur = con.cursor()
        self.active = active_category

        self.categories = cur.execute("select * from Categories").fetchall()
        self.links = []
        con.close()

        # Заполнение панели
        for count, (category_id, title) in enumerate(self.categories):
            btn = QPushButton(self)
            btn.setText(title)
            btn.setStyleSheet("background: #ffffff; text-align: left; border: 0px")
            btn.setFont(self.order_font)
            btn.setGeometry(QRect(20, count * 50 + 20, 270, 20))
            self.links.append(btn)
        self.links[self.active[0]].setFont(self.active_font)
