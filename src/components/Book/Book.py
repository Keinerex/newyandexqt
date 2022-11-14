import sqlite3
import uuid

from PyQt5.QtWidgets import QFrame

from src.components.Book.book_style import Ui_Form


class Book(QFrame, Ui_Form):
    def __init__(self, id, title, authors, price, genre, rate, func, target="market", parent=None):
        super().__init__(parent)
        self.id = id
        self.func = func
        self.target = target
        con = sqlite3.connect("base.db")
        cur = con.cursor()
        if query := cur.execute(f'select count from Cart where book_id = "{self.id}"').fetchone():
            self.count = query[0]
        else:
            self.count = 0
        con.close()
        self.setupUi(self, title, authors, genre, price, rate, self.count)
        self.book_btn.clicked.connect(func)
        self.increment.clicked.connect(self.increment_func)
        self.decrement.clicked.connect(self.decrement_func)

    def rerender(self):
        con = sqlite3.connect("base.db")
        cur = con.cursor()
        if query := cur.execute(f'select count from Cart where book_id = "{self.id}"').fetchone():
            self.count = query[0]
        else:
            self.count = 0
        self.numberLabel.setText(str(self.count))
        con.close()

    def decrement_func(self):
        con = sqlite3.connect("base.db")
        cur = con.cursor()
        if self.id in [i[0] for i in cur.execute("select book_id from Cart").fetchall()]:
            cur.execute(f'update Cart set count = {self.count - 1} where book_id = "{self.id}"')
        cur.execute("delete from Cart where count = 0")
        con.commit()
        con.close()
        self.rerender()
        if self.target == "cart":
            self.func()

    def increment_func(self):
        con = sqlite3.connect("base.db")
        cur = con.cursor()
        if self.id in [i[0] for i in cur.execute("select book_id from Cart").fetchall()]:
            cur.execute(f'update Cart set count = {self.count + 1} where book_id = "{self.id}"')
        else:
            cur.execute(f'insert into Cart values ("{uuid.uuid4()}", "{self.id}", 1)')
        con.commit()
        con.close()
        self.rerender()
        if self.target == "cart":
            self.func()
