from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QWidget, QPushButton
from sqlite3 import connect
from src.components.Navigation.navigation_style import Ui_Form

class Navigation(QWidget, Ui_Form):
    def __init__(self, parent, active_category):
        super().__init__(parent)
        self.setupUi(self)
        con = connect("base.db")
        cur = con.cursor()
        self.active = active_category

        self.categories = cur.execute("select * from Categories").fetchall()
        self.links = []
        con.close()

        for count, (id, title) in enumerate(self.categories):
            btn = QPushButton(self)
            btn.setText(title)
            btn.setStyleSheet("background: #ffffff; text-align: left; border: 0px")
            btn.setFont(self.order_font)
            btn.setGeometry(QRect(20, count * 50 + 20, 270, 20))
            self.links.append(btn)
        self.links[self.active[0]].setFont(self.active_font)




