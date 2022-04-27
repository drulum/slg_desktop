import os
import sys

from dotenv import load_dotenv

# from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication

from db.database import Database
from gui.mainwindow import MainWindow


class ShoppingListGenerator:

    def __init__(self):
        load_dotenv()
        self.db = Database()
        self.db.create_db()
        if os.getenv('SLG_UI_PREF') == 'gui':
            self.launch_gui()
        else:
            self.launch_tui()

    def launch_gui(self):
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        app.exec()

    def launch_tui(self):
        print('Sorry, no TUI option developed yet!')


if __name__ == '__main__':
    slg = ShoppingListGenerator()

