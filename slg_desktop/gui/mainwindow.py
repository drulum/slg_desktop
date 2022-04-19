from PySide6.QtWidgets import QMainWindow

from gui.MainWindow import Ui_MainWindow

from gui.brands import BrandsWindow
from gui.categories import CategoriesWindow
from gui.items import ItemsWindow
from gui.stores import StoresWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.stores_window = StoresWindow()
        self.categories_window = CategoriesWindow()
        self.brands_window = BrandsWindow()
        self.items_window = ItemsWindow()
        self.storesButton.clicked.connect(self.stores_button)
        self.categoriesButton.clicked.connect(self.categories_button)
        self.brandsButton.clicked.connect(self.brands_button)
        self.itemsButton.clicked.connect(self.items_button)

    def stores_button(self):
        self.stores_window.show()

    def categories_button(self):
        self.categories_window.show()

    def brands_button(self):
        self.brands_window.show()

    def items_button(self):
        self.items_window.show()

