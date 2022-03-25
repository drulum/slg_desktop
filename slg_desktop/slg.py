import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow

from database import Database
from Brands import Ui_BrandsWindow
from Categories import Ui_CategoriesWindow
from MainWindow import Ui_MainWindow
from Stores import Ui_StoresWindow


class BrandsWindow(QMainWindow, Ui_BrandsWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.addButton.clicked.connect(self.add_button)
        self.deleteButton.clicked.connect(self.delete_button)
        self.nameEdit.editingFinished.connect(self.name_edit)
        
    def add_button(self):
        print('Add')

    def delete_button(self):
        print('Delete')

    def name_edit(self):
        print('Name edit')


class CategoriesWindow(QMainWindow, Ui_CategoriesWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.addButton.clicked.connect(self.add_button)
        self.deleteButton.clicked.connect(self.delete_button)
        self.nameEdit.editingFinished.connect(self.name_edit)
        
    def add_button(self):
        print('Add')

    def delete_button(self):
        print('Delete')

    def name_edit(self):
        print('Name edit')


class StoresWindow(QMainWindow, Ui_StoresWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.addButton.clicked.connect(self.add_button)
        self.deleteButton.clicked.connect(self.delete_button)
        self.nameEdit.editingFinished.connect(self.name_edit)
        self.locationEdit.editingFinished.connect(self.location_edit)
        
    def add_button(self):
        print('Add')

    def delete_button(self):
        print('Delete')

    def name_edit(self):
        print('Name edit')

    def location_edit(self):
        print('Location edit')


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.stores_window = StoresWindow()
        self.categories_window = CategoriesWindow()
        self.brands_window = BrandsWindow()
        self.storesButton.clicked.connect(self.stores_button)
        self.categoriesButton.clicked.connect(self.categories_button)
        self.brandsButton.clicked.connect(self.brands_button)

    def stores_button(self):
        self.stores_window.show()

    def categories_button(self):
        self.categories_window.show()

    def brands_button(self):
        self.brands_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

