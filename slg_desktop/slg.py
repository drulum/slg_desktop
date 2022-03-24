import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow

from database import Database
from MainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.storesButton.clicked.connect(self.stores)
        self.categoriesButton.clicked.connect(self.categories)
        self.brandsButton.clicked.connect(self.brands)

    def stores(self):
        print('Stores')

    def categories(self):
        print('Categories')

    def brands(self):
        print('Brands')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

