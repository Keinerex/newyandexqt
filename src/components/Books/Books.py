import sqlite3

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QScrollArea

from src.components.Book.Book import Book


# Прокручивыемый контейнер для книг
class Books(QScrollArea):
    # Инициализация
    def __init__(self, category_id, book_func, parent=None):
        super().__init__(parent)
        # Инициализация стилей
        self.setupUi()
        self.setWidget(self.scrollAreaWidgetContents_2)
        self.rerender(category_id, book_func)

    # Вызов ререндера у всех книг
    def rerender_books(self) -> None:
        for i in range(self.verticalLayout_2.count()):
            self.verticalLayout_2.itemAt(i).widget().rerender()

    # Стили
    def setupUi(self) -> None:
        self.setStyleSheet("border: 0px")
        self.setGeometry(QtCore.QRect(370, 50, 870, 660))
        self.setMinimumSize(QtCore.QSize(870, 660))
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setWidgetResizable(True)
        self.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 859, 700))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_2.setContentsMargins(0, 0, -1, 0)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

    # Ререндер
    def rerender(self, category_id: str, func) -> None:
        # Отчистка книг
        for i in reversed(range(self.verticalLayout_2.count())):
            self.verticalLayout_2.itemAt(i).widget().setParent(None)
        # Заполнение из бд
        con = sqlite3.connect("base.db")
        cur = con.cursor()
        result = cur.execute(
            'select id, title, price, genre_id, rate from Books where categories_id = ?', (category_id,)).fetchall()

        for id, title, price, genre_id, rate in result:
            genre = cur.execute("select genre from Genres where id = ?", (genre_id,)).fetchone()[0]
            authors = [i[0] for i in cur.execute("""select name from Authors where id in 
                (select author_id from AuthorBooks where book_id = ?)""", (id,)).fetchall()]
            self.verticalLayout_2.addWidget(Book(id, title, authors, price, genre, rate, func))
        con.close()
