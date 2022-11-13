import sqlite3

from PyQt5.QtWidgets import QWidget

from src.pages.BookPage.bookpage_style import Ui_Form


class BookPage(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.book_id = ""
        self.setupUi(self)

    def setId(self, id):
        self.book_id = id
        self.rerender()

    def rerender(self):
        con = sqlite3.connect("base.db")
        cur = con.cursor()
        result = cur.execute(
            f'select id, title, price, genre_id, rate, annotation from Books where id = "{self.book_id}"').fetchall()

        for id, title, price, genre_id, rate, annotation in result:
            genre = cur.execute(f'select genre from Genres where id="{genre_id}"').fetchone()[0]
            authors = [i[0] for i in cur.execute(f"""select name from Authors where id in 
                        (select author_id from AuthorBooks where book_id = "{id}")""").fetchall()]
            con = sqlite3.connect("base.db")
            cur = con.cursor()
            if query := cur.execute(f'select count from Cart where book_id = "{self.book_id}"').fetchone():
                self.count = query[0]
            else:
                self.count = 0
            con.close()
            self.book_widget.retranslateUi(self, title, authors, genre, price, rate)
            self.annotation_widget.setAnnotation(annotation)

            self.reviews_widget.rerender(self.book_id)
        con.close()
