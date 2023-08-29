from PySide6.QtCore import Qt
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from PySide6.QtWidgets import QHeaderView, QMainWindow

from gui.Brands import Ui_BrandsWindow

db = QSqlDatabase("QSQLITE")
db.setDatabaseName('slg.sqlite3')
db.open()


class BrandsWindow(QMainWindow, Ui_BrandsWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.addButton.clicked.connect(self.add_record)
        self.cancelButton.clicked.connect(self.cancel_add)
        self.deleteButton.clicked.connect(self.delete)
        self.brandEdit.textChanged.connect(self.brand_change)
        self.model = QSqlTableModel(db=db)
        self.model.setTable('brand')
        self.model.setSort(1, Qt.AscendingOrder)
        self.model.setHeaderData(1, Qt.Horizontal, 'Brand name')
        self.brandView.setModel(self.model)
        self.brandView.hideColumn(0)
        header = self.brandView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        self.model.select()
 
    def add_record(self):
        record = self.model.record()
        record.setValue('name', self.brandEdit.text())
        self.model.insertRecord(-1, record)
        self.model.select()
        self.cancel_add()

    def cancel_add(self):
        self.brandEdit.setText('')

    def delete(self):
        index = self.brandView.currentIndex()
        if index:
            self.model.removeRow(index.row())
            self.model.select()

    def brand_change(self):
        if self.brandEdit.text():
            self.addButton.setEnabled(True)
            self.cancelButton.setEnabled(True)
        else:
            self.addButton.setEnabled(False)
            self.cancelButton.setEnabled(False)
