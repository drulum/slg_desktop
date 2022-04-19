from PySide6.QtCore import Qt
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel, QSqlTableModel
from PySide6.QtWidgets import QHeaderView, QMainWindow

from gui.Items import Ui_ItemsWindow

db = QSqlDatabase('QSQLITE')
db.setDatabaseName('slg.sqlite3')
db.open()


class ItemsWindow(QMainWindow, Ui_ItemsWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.itemEdit.textChanged.connect(self.item_change)
        self.addButton.clicked.connect(self.add_item)
        self.cancelButton.clicked.connect(self.cancel_add)
        self.deleteButton.clicked.connect(self.delete)
        self.model = QSqlTableModel(db=db)
        self.model.setTable('item')
        self.model.setSort(3, Qt.AscendingOrder)
        self.itemView.setModel(self.model)
        self.itemView.hideColumn(0)
        header = self.itemView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        self.model.select()

        self.brands_model = QSqlTableModel(db=db)
        self.brands_model.setTable('brand')
        self.brands_model.setSort(1, Qt.AscendingOrder)
        self.brandBox.setModel(self.brands_model)
        self.brandBox.setModelColumn(1)
        self.brands_model.select()

        self.categories_model = QSqlTableModel(db=db)
        self.categories_model.setTable('category')
        self.categories_model.setSort(1, Qt.AscendingOrder)
        self.categoryBox.setModel(self.categories_model)
        self.categoryBox.setModelColumn(1)
        self.categories_model.select()

        self.refresh_comboboxes()
        
    def add_item(self):
        self.refresh_comboboxes()

    def refresh_comboboxes(self):
        self.brands_model.select()
        self.categories_model.select()
        self.brandBox.setCurrentIndex(-1)
        self.categoryBox.setCurrentIndex(-1)

    def cancel_add(self):
        self.refresh_comboboxes()
        self.itemEdit.setText('')
        self.sizeEdit.setText('')
        self.costEdit.setText('')

    def delete(self):
        index = self.itemView.currentIndex()
        if index:
            self.model.removeRow(index.row())
            self.model.select()
            self.refresh_comboboxes()

    def item_change(self):
        if self.itemEdit.text():
            self.addButton.setEnabled(True)
            self.cancelButton.setEnabled(True)
        else:
            self.addButton.setEnabled(False)
            self.cancelButton.setEnabled(False)

    def showEvent(self, event):
        self.refresh_comboboxes()
        return super().showEvent(event)

