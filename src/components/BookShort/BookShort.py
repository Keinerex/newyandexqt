import sqlite3
import uuid

from PyQt5.QtWidgets import QFrame
from src.components.BookShort.book_style_short import Ui_Form

class BookShort(QFrame, Ui_Form):
    def __init__(self, id, title, authors, price, genre, rate, parent=None):
        super().__init__(parent)
        self.id = id
        con = sqlite3.connect("base.db")
        cur = con.cursor()
        if query := cur.execute(f'select count from Cart where book_id = "{self.id}"').fetchone():
            self.count = query[0]
        else:
            self.count = 0
        con.close()
        self.setupUi(self, title, authors, genre, price, rate)