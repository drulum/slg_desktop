from PySide6.QtCore import Qt
from PySide6.QtSql import QSqlDatabase, QSqlRelation, QSqlRelationalDelegate, QSqlRelationalTableModel, QSqlTableModel
from PySide6.QtWidgets import QHeaderView, QMainWindow, QTableView

from export import Export

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
        'notes': 'Notes',
        'store_id': 'Store'
    }

    delivery_options = {
        'Email': 'email',
        'Save': 'save',
    }
    format_options = {
        'CSV': 'csv',
        'JSON': 'json',
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

        self.shoppinglistBox.currentIndexChanged.connect(self.date_changed)
        self.itemBox.currentIndexChanged.connect(self.item_change)
        self.addButton.clicked.connect(self.add_shopping_item)
        self.cancelButton.clicked.connect(self.clear_input)
        self.removeButton.clicked.connect(self.delete)

        self.formatBox.addItems(list(self.format_options.keys()))
        self.deliveryBox.addItems(list(self.delivery_options.keys()))
        self.exportButton.clicked.connect(self.export_list)

        self.model = QSqlRelationalTableModel(db=db)
        self.model.setJoinMode(QSqlRelationalTableModel.LeftJoin)
        self.model.setTable('shopping_list_item')
        self.model.setRelation(1, QSqlRelation('shopping_list', 'id', 'for_date'))
        self.model.setRelation(2, QSqlRelation('item', 'id', 'name'))
        self.model.setRelation(5, QSqlRelation('store', 'id', 'name'))
        self.model.setSort(2, Qt.AscendingOrder)
        for original, replacement in self.column_titles.items():
            index = self.model.fieldIndex(original)
            self.model.setHeaderData(index, Qt.Horizontal, replacement)
        self.itemlistView.setModel(self.model)
        self.itemlistView.setItemDelegate(QSqlRelationalDelegate(self.itemlistView))
        self.itemlistView.hideColumn(0)
        self.itemlistView.hideColumn(1)
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
        stores_tableview_header = stores_tableview.horizontalHeader()
        stores_tableview_header.setSectionResizeMode(QHeaderView.ResizeToContents)
        stores_tableview_header.setStretchLastSection(True)
        self.storeBox.setModel(self.stores_model)
        self.storeBox.setView(stores_tableview)
        self.storeBox.setModelColumn(1)

    def add_shopping_item(self):
        record = self.model.record()
        date_pk = self.shoppinglistBox.model().index(self.shoppinglistBox.currentIndex(), 0, self.shoppinglistBox.rootModelIndex())
        item_pk = self.itemBox.model().index(self.itemBox.currentIndex(), 0, self.itemBox.rootModelIndex())
        store_pk = self.storeBox.model().index(self.storeBox.currentIndex(), 0, self.storeBox.rootModelIndex())
        record.setValue(1, date_pk.data())
        record.setValue(2, item_pk.data())
        record.setValue('quantity', self.quantityBox.value())
        record.setValue('notes', self.notesTextEdit.toPlainText())
        record.setValue(5, store_pk.data())
        self.model.insertRecord(-1, record)
        self.model.select()
        self.clear_input()

    def clear_input(self):
        self.itemBox.setCurrentIndex(-1)
        self.quantityBox.setValue(1)
        self.storeBox.setCurrentIndex(-1)
        self.notesTextEdit.setPlainText('')

    def date_changed(self):
        index = self.shoppinglistBox.model().index(self.shoppinglistBox.currentIndex(), 0, self.shoppinglistBox.rootModelIndex())
        if index:
            self.model.setFilter(f'shopping_list_id = {index.data()}')
        pass

    def delete(self):
        index = self.itemlistView.currentIndex()
        if index:
            self.model.removeRow(index.row())
            self.model.select()

    def export_list(self):
        list_pk = self.shoppinglistBox.model().index(self.shoppinglistBox.currentIndex(), 0, self.shoppinglistBox.rootModelIndex()).data()
        export_delivery = self.delivery_options[self.deliveryBox.currentText()]
        output = Export(list_pk, export_delivery)
        export_format = getattr(output, self.format_options[self.formatBox.currentText()])
        export_format()

    def item_change(self):
        if self.itemBox.currentText():
            self.quantityBox.setEnabled(True)
            self.storeBox.setEnabled(True)
            self.notesTextEdit.setEnabled(True)
            self.addButton.setEnabled(True)
            self.cancelButton.setEnabled(True)
        else:
            self.quantityBox.setEnabled(False)
            self.storeBox.setEnabled(False)
            self.notesTextEdit.setEnabled(False)
            self.addButton.setEnabled(False)
            self.cancelButton.setEnabled(False)

    def refresh_data(self):
        self.model.select()
        self.dates_model.select()
        self.items_model.select()
        self.stores_model.select()
        self.clear_input()

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

