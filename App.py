from PyQt5.QtWidgets import QMainWindow

from src.pages.BookPage.BookPage import BookPage
from src.pages.CartPage.CartPage import CartPage
from src.pages.MarketPage.MarketPage import MarketPage
from style import Ui_MainWindow


# Приложение
class App(QMainWindow, Ui_MainWindow):
    # Инициализация
    def __init__(self):
        super().__init__()
        # Инициализация стилей
        self.setupUi(self)
        # Инициализация страниц
        self.market_page = MarketPage(self.book_click)
        self.book_page = BookPage()
        self.cart_page = CartPage()
        # Первая страница - магазин
        self.init_page("market")
        # Подключение кнопок Header для переключения страниц
        self.header_widget.shopBtn.clicked.connect(self.shop_click)
        self.header_widget.cartBtn.clicked.connect(self.cart_click)
        # Подключение функционала Navigation
        for link in self.market_page.nav_widget.links:
            link.clicked.connect(self.nav_link_click)

    # Выбор активной категорий
    def nav_link_click(self) -> None:
        self.market_page.nav_widget.active[0] = self.market_page.nav_widget.links.index(
            self.sender())
        for link in self.market_page.nav_widget.links:
            link.setFont(self.market_page.nav_widget.order_font)
        self.market_page.nav_widget.sender().setFont(self.market_page.nav_widget.active_font)
        self.market_page.scrollArea.rerender(
            self.market_page.nav_widget.categories[self.market_page.nav_widget.active[0]][0], self.book_click)

    # Выбор страницы книг при нажатии на её название
    def book_click(self) -> None:
        self.init_page("book", self.sender().parent().id)

    # Выбор страницы магазина при нажатии на соответсвующую кнопку
    def shop_click(self) -> None:
        self.init_page("market")

    # Выбор страницы корзины при нажати на соответсвующую кнопку
    def cart_click(self) -> None:
        self.init_page("cart")

    # Выбор и отображение активной страницы
    def init_page(self, page, book_id="") -> None:
        self.market_page.setParent(None)
        self.cart_page.setParent(None)
        self.book_page.setParent(None)
        if page == "market":
            self.market_page.setParent(self.centralwidget)
            self.market_page.scrollArea.rerender_books()
            self.market_page.show()
        elif page == "cart":
            self.cart_page.setParent(self.centralwidget)
            self.cart_page.books_widget.rerender()
            self.cart_page.show()
        elif page == "book":
            self.book_page.setParent(self.centralwidget)
            self.book_page.set_id(book_id)
            self.book_page.show()
