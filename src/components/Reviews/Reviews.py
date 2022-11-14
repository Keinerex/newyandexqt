import sqlite3

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QScrollArea

from src.components.Review.Review import Review


# Прокручиваемая область для отзывов
class Reviews(QScrollArea):
    # Инициализация
    def __init__(self, parent=None):
        super().__init__(parent)
        # Инициализация стилей
        self.setup_ui()
        self.setWidget(self.scrollAreaWidgetContents_2)
        self.rerender("")

    # Стили
    def setup_ui(self) -> None:
        self.setStyleSheet("border: 0px;")
        self.setMinimumSize(QtCore.QSize(870, 440))
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setWidgetResizable(True)
        self.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 859, 440))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_2.setContentsMargins(0, 0, -1, 0)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

    # Ререндер
    def rerender(self, book_id) -> None:
        # Очистить отзывы
        for i in reversed(range(self.verticalLayout_2.count())):
            self.verticalLayout_2.itemAt(i).widget().setParent(None)
        # Заполнить из бд
        con = sqlite3.connect("base.db")
        cur = con.cursor()

        for id_, rate, user_id, text in cur.execute(
                'select id, rate, user_id, text from Reviews where book_id = ?', (book_id,)).fetchall():
            user, = cur.execute('select name from Users where id = ?', (user_id,)).fetchone()
            try:
                self.verticalLayout_2.addWidget(Review(user, text, rate))
            except Exception as e:
                print(e)
