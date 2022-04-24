from PySide6.QtCore import Qt
from PySide6.QtSql import QSqlDatabase, QSqlRelation, QSqlRelationalDelegate, QSqlRelationalTableModel, QSqlTableModel
from PySide6.QtWidgets import QHeaderView, QMainWindow

from gui.Items import Ui_ItemsWindow

db = QSqlDatabase('QSQLITE')
db.setDatabaseName('slg.sqlite3')
db.open()


class ItemsWindow(QMainWindow, Ui_ItemsWindow):

    column_titles = {
        'brand_id': 'Brand',
        'category_id': 'Category',
        'name': 'Item name',
        'size': 'Size',
        'expected_cost': 'Expected cost'
    }

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.itemEdit.textChanged.connect(self.item_change)
        self.addButton.clicked.connect(self.add_item)
        self.cancelButton.clicked.connect(self.cancel_add)
        self.deleteButton.clicked.connect(self.delete)

        self.model = QSqlRelationalTableModel(db=db)
        self.model.setJoinMode(QSqlRelationalTableModel.LeftJoin)
        self.model.setTable('item')
        self.model.setRelation(1, QSqlRelation('brand', 'id', 'name'))
        self.model.setRelation(2, QSqlRelation('category', 'id', 'name'))
        self.model.setSort(3, Qt.AscendingOrder)
        for original, replacement in self.column_titles.items():
            index = self.model.fieldIndex(original)
            self.model.setHeaderData(index, Qt.Horizontal, replacement)
        self.itemView.setModel(self.model)
        self.itemView.setItemDelegate(QSqlRelationalDelegate(self.itemView))
        self.itemView.hideColumn(0)
        header = self.itemView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

        self.brands_model = QSqlTableModel(db=db)
        self.brands_model.setTable('brand')
        self.brands_model.setSort(1, Qt.AscendingOrder)
        self.brandBox.setModel(self.brands_model)
        self.brandBox.setModelColumn(1)

        self.categories_model = QSqlTableModel(db=db)
        self.categories_model.setTable('category')
        self.categories_model.setSort(1, Qt.AscendingOrder)
        self.categoryBox.setModel(self.categories_model)
        self.categoryBox.setModelColumn(1)

    def add_item(self):
        record = self.model.record()
        brand_pk = self.brandBox.model().index(self.brandBox.currentIndex(), 0, self.brandBox.rootModelIndex())
        record.setValue(1, brand_pk.data())
        category_pk = self.categoryBox.model().index(self.categoryBox.currentIndex(), 0, self.categoryBox.rootModelIndex())
        record.setValue(2, category_pk.data())
        record.setValue('name', self.itemEdit.text())
        record.setValue('size', self.sizeEdit.text())
        record.setValue('expected_cost', self.costEdit.text())
        self.model.insertRecord(-1, record)
        self.model.select()
        self.cancel_add()

        self.refresh_data()

    def refresh_data(self):
        self.model.select()
        self.model.relationModel(1).select()
        self.model.relationModel(2).select()
        self.brands_model.select()
        self.categories_model.select()
        self.brandBox.setCurrentIndex(-1)
        self.categoryBox.setCurrentIndex(-1)

    def cancel_add(self):
        self.refresh_data()
        self.itemEdit.setText('')
        self.sizeEdit.setText('')
        self.costEdit.setText('')

    def delete(self):
        index = self.itemView.currentIndex()
        if index:
            self.model.removeRow(index.row())
            self.model.select()
            self.refresh_data()

    def item_change(self):
        if self.itemEdit.text():
            self.addButton.setEnabled(True)
            self.cancelButton.setEnabled(True)
        else:
            self.addButton.setEnabled(False)
            self.cancelButton.setEnabled(False)

    def showEvent(self, event):
        self.refresh_data()
        return super().showEvent(event)

