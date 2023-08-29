from PySide6.QtCore import QDate, Qt
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from PySide6.QtWidgets import QHeaderView, QMainWindow

from gui.ShoppingList import Ui_ShoppingListWindow

db = QSqlDatabase('QSQLITE')
db.setDatabaseName('slg.sqlite3')
db.open()


class ShoppingListWindow(QMainWindow, Ui_ShoppingListWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.addButton.clicked.connect(self.add_record)
        self.cancelButton.clicked.connect(self.cancel_add)
        self.deleteButton.clicked.connect(self.delete)
        self.shoppinglistEdit.setDate(QDate.currentDate())
        self.shoppinglistEdit.userDateChanged.connect(self.shopping_list_change)
        self.model = QSqlTableModel(db=db)
        self.model.setTable('shopping_list')
        self.model.setSort(1, Qt.AscendingOrder)
        self.model.setHeaderData(1, Qt.Horizontal, 'Shopping list date')
        self.shoppinglistView.setModel(self.model)
        self.shoppinglistView.hideColumn(0)
        header = self.shoppinglistView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        self.model.select()
        
    def add_record(self):
        # TODO manually enforce DATE because sqlite3 is pish
        record = self.model.record()
        record.setValue('for_date', self.shoppinglistEdit.date())
        self.model.insertRecord(-1, record)
        self.model.select()
        self.cancel_add()

    def cancel_add(self):
        self.shoppinglistEdit.setDate(QDate.currentDate())
        self.addButton.setEnabled(False)
        self.cancelButton.setEnabled(False)

    def delete(self):
        index = self.shoppinglistView.currentIndex()
        if index:
            self.model.removeRow(index.row())
            self.model.select()

    def shopping_list_change(self):
        self.addButton.setEnabled(True)
        self.cancelButton.setEnabled(True)
