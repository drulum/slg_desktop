from PySide6.QtCore import Qt
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
        # TODO: set to today's date by default
        self.shoppinglistEdit.dateChanged.connect(self.shopping_list_change)
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
        pass

    def cancel_add(self):
        # Reset datefield to defaults
        pass

    def delete(self):
        pass

    def shopping_list_change(self):
        if self.shoppinglistEdit.date():
            self.addButton.setEnabled(True)
            self.cancelButton.setEnabled(True)
        else:
            self.addButton.setEnabled(True)
            self.cancelButton.setEnabled(True)

