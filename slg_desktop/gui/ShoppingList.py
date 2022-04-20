# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'shoppinglist.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTableView, QVBoxLayout, QWidget)

class Ui_ShoppingListWindow(object):
    def setupUi(self, ShoppingListWindow):
        if not ShoppingListWindow.objectName():
            ShoppingListWindow.setObjectName(u"ShoppingListWindow")
        ShoppingListWindow.resize(400, 600)
        self.centralwidget = QWidget(ShoppingListWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.shoppinglistView = QTableView(self.centralwidget)
        self.shoppinglistView.setObjectName(u"shoppinglistView")

        self.verticalLayout.addWidget(self.shoppinglistView)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.deleteButton = QPushButton(self.centralwidget)
        self.deleteButton.setObjectName(u"deleteButton")

        self.horizontalLayout_3.addWidget(self.deleteButton)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.shoppinglistEdit = QDateEdit(self.groupBox)
        self.shoppinglistEdit.setObjectName(u"shoppinglistEdit")
        self.shoppinglistEdit.setMinimumDate(QDate(2022, 4, 1))
        self.shoppinglistEdit.setCalendarPopup(True)

        self.horizontalLayout_2.addWidget(self.shoppinglistEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addButton = QPushButton(self.groupBox)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setEnabled(False)

        self.horizontalLayout.addWidget(self.addButton)

        self.cancelButton = QPushButton(self.groupBox)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setEnabled(False)

        self.horizontalLayout.addWidget(self.cancelButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.groupBox)

        ShoppingListWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ShoppingListWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 400, 23))
        ShoppingListWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ShoppingListWindow)
        self.statusbar.setObjectName(u"statusbar")
        ShoppingListWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ShoppingListWindow)

        QMetaObject.connectSlotsByName(ShoppingListWindow)
    # setupUi

    def retranslateUi(self, ShoppingListWindow):
        ShoppingListWindow.setWindowTitle(QCoreApplication.translate("ShoppingListWindow", u"Add, Edit, Delete Shopping Lists", None))
#if QT_CONFIG(statustip)
        self.shoppinglistView.setStatusTip(QCoreApplication.translate("ShoppingListWindow", u"Double click the field to edit it.", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.deleteButton.setStatusTip(QCoreApplication.translate("ShoppingListWindow", u"CAUTION: The selected shopping list will be deleted.", None))
#endif // QT_CONFIG(statustip)
        self.deleteButton.setText(QCoreApplication.translate("ShoppingListWindow", u"Delete selected shopping list", None))
        self.groupBox.setTitle(QCoreApplication.translate("ShoppingListWindow", u"Add shopping list", None))
        self.label.setText(QCoreApplication.translate("ShoppingListWindow", u"Shopping list date", None))
        self.shoppinglistEdit.setDisplayFormat(QCoreApplication.translate("ShoppingListWindow", u"yyyy/MM/dd", None))
#if QT_CONFIG(statustip)
        self.addButton.setStatusTip(QCoreApplication.translate("ShoppingListWindow", u"Add a new shopping list.", None))
#endif // QT_CONFIG(statustip)
        self.addButton.setText(QCoreApplication.translate("ShoppingListWindow", u"Add", None))
#if QT_CONFIG(statustip)
        self.cancelButton.setStatusTip(QCoreApplication.translate("ShoppingListWindow", u"Cancel the addition and reset the fields.", None))
#endif // QT_CONFIG(statustip)
        self.cancelButton.setText(QCoreApplication.translate("ShoppingListWindow", u"Cancel", None))
    # retranslateUi

