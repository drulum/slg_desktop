# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'items.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTableView, QVBoxLayout,
    QWidget)

class Ui_ItemsWindow(object):
    def setupUi(self, ItemsWindow):
        if not ItemsWindow.objectName():
            ItemsWindow.setObjectName(u"ItemsWindow")
        ItemsWindow.resize(800, 600)
        self.centralwidget = QWidget(ItemsWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.itemView = QTableView(self.centralwidget)
        self.itemView.setObjectName(u"itemView")

        self.verticalLayout_4.addWidget(self.itemView)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.deleteButton = QPushButton(self.centralwidget)
        self.deleteButton.setObjectName(u"deleteButton")

        self.horizontalLayout.addWidget(self.deleteButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.categoryBox = QComboBox(self.groupBox)
        self.categoryBox.setObjectName(u"categoryBox")

        self.gridLayout.addWidget(self.categoryBox, 0, 3, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.itemEdit = QLineEdit(self.groupBox)
        self.itemEdit.setObjectName(u"itemEdit")

        self.gridLayout.addWidget(self.itemEdit, 1, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.sizeEdit = QLineEdit(self.groupBox)
        self.sizeEdit.setObjectName(u"sizeEdit")

        self.gridLayout.addWidget(self.sizeEdit, 1, 3, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)

        self.brandBox = QComboBox(self.groupBox)
        self.brandBox.setObjectName(u"brandBox")

        self.gridLayout.addWidget(self.brandBox, 0, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.costEdit = QLineEdit(self.groupBox)
        self.costEdit.setObjectName(u"costEdit")

        self.gridLayout.addWidget(self.costEdit, 2, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.addButton = QPushButton(self.groupBox)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.addButton)

        self.cancelButton = QPushButton(self.groupBox)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.cancelButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_4.addWidget(self.groupBox)

        ItemsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ItemsWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        ItemsWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ItemsWindow)
        self.statusbar.setObjectName(u"statusbar")
        ItemsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ItemsWindow)

        QMetaObject.connectSlotsByName(ItemsWindow)
    # setupUi

    def retranslateUi(self, ItemsWindow):
        ItemsWindow.setWindowTitle(QCoreApplication.translate("ItemsWindow", u"Add, Edit, Delete Items", None))
        self.deleteButton.setText(QCoreApplication.translate("ItemsWindow", u"Delete selected item", None))
        self.groupBox.setTitle(QCoreApplication.translate("ItemsWindow", u"Add a new item", None))
        self.label.setText(QCoreApplication.translate("ItemsWindow", u"Brand", None))
        self.label_3.setText(QCoreApplication.translate("ItemsWindow", u"Item name", None))
        self.label_2.setText(QCoreApplication.translate("ItemsWindow", u"Category", None))
        self.label_4.setText(QCoreApplication.translate("ItemsWindow", u"Size", None))
        self.label_5.setText(QCoreApplication.translate("ItemsWindow", u"Expected cost", None))
        self.addButton.setText(QCoreApplication.translate("ItemsWindow", u"Add", None))
        self.cancelButton.setText(QCoreApplication.translate("ItemsWindow", u"Cancel", None))
    # retranslateUi

