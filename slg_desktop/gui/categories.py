from PySide6.QtCore import Qt
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from PySide6.QtWidgets import QHeaderView, QMainWindow

from gui.Categories import Ui_CategoriesWindow

db = QSqlDatabase('QSQLITE')
db.setDatabaseName('slg.sqlite3')
db.open()


class CategoriesWindow(QMainWindow, Ui_CategoriesWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.addButton.clicked.connect(self.add_record)
        self.cancelButton.clicked.connect(self.cancel_add)
        self.deleteButton.clicked.connect(self.delete)
        self.categoryEdit.textChanged.connect(self.category_change)
        self.model = QSqlTableModel(db=db)
        self.model.setTable('category')
        self.model.setSort(1, Qt.AscendingOrder)
        self.categoryView.setModel(self.model)
        self.categoryView.hideColumn(0)
        header = self.categoryView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        self.model.select()
        
    def add_record(self):
        record = self.model.record()
        record.setValue('name', self.categoryEdit.text())
        self.model.insertRecord(-1, record)
        self.model.select()
        self.cancel_add()

    def cancel_add(self):
        self.categoryEdit.setText('')

    def delete(self):
        index = self.categoryView.currentIndex()
        if index:
            self.model.removeRow(index.row())
            self.model.select()

    def category_change(self):
        if self.categoryEdit.text():
            self.addButton.setEnabled(True)
            self.cancelButton.setEnabled(True)
        else:
            self.addButton.setEnabled(False)
            self.cancelButton.setEnabled(False)


