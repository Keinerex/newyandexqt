import sqlite3

from PyQt5.QtWidgets import QWidget

from src.components.Bill.bill_style import Ui_Form


# Cчёт
class Bill(QWidget, Ui_Form):
    # Инициализация
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        # Инициализация стилей
        self.setupUi(self)
        self.rerender()

    # Ререндер
    def rerender(self) -> None:
        # Получение и заполнение данных из бд
        con = sqlite3.connect("base.db")
        cur = con.cursor()
        self.textBrowser.setText("a")
        string = ""
        result = 0
        for book_id, count in cur.execute("select book_id, count from Cart").fetchall():
            name, price = cur.execute(f'select title, price from Books where id = ?', (book_id,)).fetchone()
            string += f"{name}: {price * count}\n\n"
            result += price * count
        self.textBrowser.setText(string)
        self.result.setText(f"Итого: {result}Р")
        con.close()
