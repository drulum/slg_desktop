from PySide6.QtWidgets import QMainWindow

from gui.Brands import Ui_BrandsWindow


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

