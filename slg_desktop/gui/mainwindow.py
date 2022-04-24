from PySide6.QtCore import Qt
from PySide6.QtSql import QSqlDatabase, QSqlRelation, QSqlRelationalDelegate, QSqlRelationalTableModel, QSqlTableModel
from PySide6.QtWidgets import QHeaderView, QMainWindow, QTableView

from gui.MainWindow import Ui_MainWindow

from gui.brands import BrandsWindow
from gui.categories import CategoriesWindow
from gui.items import ItemsWindow
from gui.shoppinglist import ShoppingListWindow
from gui.stores import StoresWindow

db = QSqlDatabase('QSQLITE')
db.setDatabaseName('slg.sqlite3')
db.open()


class MainWindow(QMainWindow, Ui_MainWindow):

    column_titles = {
        'item_id': 'Item',
        'quantity': 'Quantity',
        'store_id': 'Store'
    }

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.shopping_list_window = ShoppingListWindow()
        self.stores_window = StoresWindow()
        self.categories_window = CategoriesWindow()
        self.brands_window = BrandsWindow()
        self.items_window = ItemsWindow()
        self.shoppinglistsButton.clicked.connect(self.shopping_list_button)
        self.storesButton.clicked.connect(self.stores_button)
        self.categoriesButton.clicked.connect(self.categories_button)
        self.brandsButton.clicked.connect(self.brands_button)
        self.itemsButton.clicked.connect(self.items_button)
        self.refreshButton.clicked.connect(self.refresh_data)

        self.model = QSqlRelationalTableModel(db=db)
        self.model.setJoinMode(QSqlRelationalTableModel.LeftJoin)
        self.model.setTable('shopping_list_item')
        self.model.setRelation(0, QSqlRelation('shopping_list', 'id', 'for_date'))
        self.model.setRelation(1, QSqlRelation('item', 'id', 'name'))
        self.model.setRelation(3, QSqlRelation('store', 'id', 'name'))
        self.model.setSort(1, Qt.AscendingOrder)
        for original, replacement in self.column_titles.items():
            index = self.model.fieldIndex(original)
            self.model.setHeaderData(index, Qt.Horizontal, replacement)
        self.itemlistView.setModel(self.model)
        self.itemlistView.setItemDelegate(QSqlRelationalDelegate(self.itemlistView))
        self.itemlistView.hideColumn(0)
        header = self.itemlistView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

        self.dates_model = QSqlTableModel(db=db)
        self.dates_model.setTable('shopping_list')
        self.dates_model.setSort(1, Qt.AscendingOrder)
        self.shoppinglistBox.setModel(self.dates_model)
        self.shoppinglistBox.setModelColumn(1)

        self.items_model = QSqlTableModel(db=db)
        self.items_model.setTable('item')
        self.items_model.setSort(3, Qt.AscendingOrder)
        self.itemBox.setModel(self.items_model)
        self.itemBox.setModelColumn(3)

        self.stores_model = QSqlTableModel(db=db)
        self.stores_model.setTable('store')
        self.stores_model.setSort(1, Qt.AscendingOrder)
        stores_tableview = QTableView()
        stores_tableview.setModel(self.stores_model)
        stores_tableview.hideColumn(0)
        stores_tableview.horizontalHeader().setVisible(False)
        stores_tableview.verticalHeader().setVisible(False)
        stores_tableview.resizeColumnsToContents()
        self.storeBox.setModel(self.stores_model)
        self.storeBox.setView(stores_tableview)
        self.storeBox.setModelColumn(1)

    def refresh_data(self):
        self.model.select()
        self.dates_model.select()
        self.items_model.select()
        self.stores_model.select()

    def date_changed(self):
        self.model.setFilter('shopping_list_id = 1')

    def shopping_list_button(self):
        self.shopping_list_window.show()

    def stores_button(self):
        self.stores_window.show()

    def categories_button(self):
        self.categories_window.show()

    def brands_button(self):
        self.brands_window.show()

    def items_button(self):
        self.items_window.show()

    def showEvent(self, event):
        self.refresh_data()
        return super().showEvent(event)

