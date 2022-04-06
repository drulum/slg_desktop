import sys

# from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication

from db.database import Database
from gui.mainwindow import MainWindow


class ShoppingListGenerator:

    def __init__(self):
        self.db = Database()
        self.db.create_db()
        # If config states gui, launch Qt gui, otherwise launch tui
        self.launch_gui()

    def launch_gui(self):
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        app.exec()

    def launch_tui(self):
        pass


if __name__ == '__main__':
    slg = ShoppingListGenerator()

