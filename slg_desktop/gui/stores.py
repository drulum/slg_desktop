from PySide6.QtCore import Qt
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from PySide6.QtWidgets import QHeaderView, QMainWindow

from gui.Stores import Ui_StoresWindow

db = QSqlDatabase("QSQLITE")
db.setDatabaseName('slg.sqlite3')
db.open()


class StoresWindow(QMainWindow, Ui_StoresWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.storeEdit.textChanged.connect(self.store_change)
        self.addButton.clicked.connect(self.add_record)
        self.cancelButton.clicked.connect(self.cancel_add)
        self.deleteButton.clicked.connect(self.delete)
        self.model = QSqlTableModel(db=db)
        self.model.setTable('store')
        self.model.setSort(1, Qt.AscendingOrder)
        self.model.setHeaderData(1, Qt.Horizontal, 'Store name')
        self.model.setHeaderData(2, Qt.Horizontal, 'Location')
        self.storeView.setModel(self.model)
        self.storeView.hideColumn(0)
        header = self.storeView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        self.model.select()

    def add_record(self):
        record = self.model.record()
        record.setValue('name', self.storeEdit.text())
        record.setValue('location', self.locationEdit.text())
        self.model.insertRecord(-1, record)
        self.model.select()
        self.cancel_add()

    def cancel_add(self):
        self.storeEdit.setText('')
        self.locationEdit.setText('')

    def delete(self):
        index = self.storeView.currentIndex()
        if index:
            self.model.removeRow(index.row())
            self.model.select()

    def store_change(self):
        if self.storeEdit.text():
            self.addButton.setEnabled(True)
            self.cancelButton.setEnabled(True)
            self.locationEdit.setEnabled(True)
        else:
            self.addButton.setEnabled(False)
            self.cancelButton.setEnabled(False)
            self.locationEdit.setEnabled(False)

