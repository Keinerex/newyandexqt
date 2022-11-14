import sqlite3

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QScrollArea

from src.components.Book.Book import Book


# Прокручиваемая область книг корзины
class CartBooks(QScrollArea):
    # Инициализация
    def __init__(self, parent=None):
        super().__init__(parent)
        # Инициализация стилей
        self.setup_ui()
        self.setWidget(self.scrollAreaWidgetContents_2)
        self.rerender()

    # Стили
    def setup_ui(self) -> None:
        self.setStyleSheet("border: 0px")
        self.setGeometry(QtCore.QRect(400, 50, 870, 630))
        self.setMinimumSize(QtCore.QSize(870, 630))
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setWidgetResizable(True)
        self.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 870, 630))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_2.setContentsMargins(0, 0, -1, 0)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

    # Ререндер
    def rerender(self) -> None:
        # Очищение кнги
        for i in reversed(range(self.verticalLayout_2.count())):
            self.verticalLayout_2.itemAt(i).widget().setParent(None)
        # Заполнение из бд
        con = sqlite3.connect("base.db")
        cur = con.cursor()
        result = cur.execute(
            f'select id, title, price, genre_id, rate from Books where id in (select book_id from Cart)').fetchall()

        for book_id, title, price, genre_id, rate in result:
            genre = cur.execute('select genre from Genres where id = ?', (genre_id,)).fetchone()[0]
            authors = [i[0] for i in cur.execute("""select name from Authors where id in 
                (select author_id from AuthorBooks where book_id = ?)""", (book_id,)).fetchall()]
            self.verticalLayout_2.addWidget(
                Book(book_id, title, authors, price, genre, rate, self.rerender, target="cart"))
        con.commit()
        con.close()
        # Ререндера счёта
        self.parent().bill_widget.rerender()
