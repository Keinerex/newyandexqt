import sqlite3
import uuid

from PyQt5.QtWidgets import QFrame

from src.components.Book.book_style import Ui_Form


# Книга
class Book(QFrame, Ui_Form):
    # Инициализация
    def __init__(self, book_id: str, title: str, authors: list, price: int, genre: str, rate: int, func,
                 target="market", parent=None):
        super().__init__(parent)
        # Сохраненение данных книги
        self.id = book_id
        self.func = func
        self.target = target
        # Получение количества книг в корзине из бд
        con = sqlite3.connect("base.db")
        cur = con.cursor()
        if query := cur.execute('select count from Cart where book_id = ?', (self.id,)).fetchone():
            self.count = query[0]
        else:
            self.count = 0
        con.close()
        # Инициализация стилей
        self.setupUi(self, title, authors, genre, price, rate, self.count)
        # Подключение функций к кнопкам
        self.book_btn.clicked.connect(func)
        self.increment.clicked.connect(self.increment_func)
        self.decrement.clicked.connect(self.decrement_func)

    # Ререндер
    def rerender(self) -> None:
        con = sqlite3.connect("base.db")
        cur = con.cursor()
        # Получение количества книг в корзине из бд
        if query := cur.execute('select count from Cart where book_id = ?', (self.id,)).fetchone():
            self.count = query[0]
        else:
            self.count = 0
        # Поместить данные на экран
        self.numberLabel.setText(str(self.count))
        con.close()

    # Уменьшение числа книг в корзине с сохранением в бд
    def decrement_func(self) -> None:
        con = sqlite3.connect("base.db")
        cur = con.cursor()
        if self.id in [i[0] for i in cur.execute("select book_id from Cart").fetchall()]:
            cur.execute('update Cart set count = ? where book_id = ?', (self.count - 1, self.id))
        cur.execute("delete from Cart where count = 0")
        con.commit()
        con.close()
        self.rerender()
        if self.target == "cart":
            self.func()

    # Увелечение числа книг в корзине с сохранением в бд
    def increment_func(self) -> None:
        con = sqlite3.connect("base.db")
        cur = con.cursor()
        if self.id in [i[0] for i in cur.execute("select book_id from Cart").fetchall()]:
            cur.execute('update Cart set count = ? where book_id = ?', ((self.count + 1), self.id))
        else:
            cur.execute('insert into Cart values (?, ?, 1)', (str(uuid.uuid4()), self.id))
        con.commit()
        con.close()
        self.rerender()
        if self.target == "cart":
            self.func()
