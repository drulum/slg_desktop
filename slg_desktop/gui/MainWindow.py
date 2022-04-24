# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStatusBar, QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.shoppinglistBox = QComboBox(self.groupBox)
        self.shoppinglistBox.setObjectName(u"shoppinglistBox")

        self.horizontalLayout_2.addWidget(self.shoppinglistBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.refreshButton = QPushButton(self.groupBox)
        self.refreshButton.setObjectName(u"refreshButton")

        self.horizontalLayout_2.addWidget(self.refreshButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.itemlistView = QTableView(self.groupBox)
        self.itemlistView.setObjectName(u"itemlistView")

        self.verticalLayout_2.addWidget(self.itemlistView)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.removeButton = QPushButton(self.groupBox)
        self.removeButton.setObjectName(u"removeButton")

        self.horizontalLayout_5.addWidget(self.removeButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.itemBox = QComboBox(self.groupBox_3)
        self.itemBox.setObjectName(u"itemBox")

        self.horizontalLayout_4.addWidget(self.itemBox)

        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.quantityBox = QSpinBox(self.groupBox_3)
        self.quantityBox.setObjectName(u"quantityBox")
        self.quantityBox.setMinimum(1)

        self.horizontalLayout_4.addWidget(self.quantityBox)

        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.storeBox = QComboBox(self.groupBox_3)
        self.storeBox.setObjectName(u"storeBox")

        self.horizontalLayout_4.addWidget(self.storeBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.addButton = QPushButton(self.groupBox_3)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.addButton)

        self.cancelButton = QPushButton(self.groupBox_3)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.cancelButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addWidget(self.groupBox_3)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.shoppinglistsButton = QPushButton(self.groupBox_2)
        self.shoppinglistsButton.setObjectName(u"shoppinglistsButton")

        self.horizontalLayout.addWidget(self.shoppinglistsButton)

        self.storesButton = QPushButton(self.groupBox_2)
        self.storesButton.setObjectName(u"storesButton")

        self.horizontalLayout.addWidget(self.storesButton)

        self.categoriesButton = QPushButton(self.groupBox_2)
        self.categoriesButton.setObjectName(u"categoriesButton")

        self.horizontalLayout.addWidget(self.categoriesButton)

        self.brandsButton = QPushButton(self.groupBox_2)
        self.brandsButton.setObjectName(u"brandsButton")

        self.horizontalLayout.addWidget(self.brandsButton)

        self.itemsButton = QPushButton(self.groupBox_2)
        self.itemsButton.setObjectName(u"itemsButton")

        self.horizontalLayout.addWidget(self.itemsButton)


        self.verticalLayout.addWidget(self.groupBox_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.shoppinglistBox, self.refreshButton)
        QWidget.setTabOrder(self.refreshButton, self.itemlistView)
        QWidget.setTabOrder(self.itemlistView, self.removeButton)
        QWidget.setTabOrder(self.removeButton, self.itemBox)
        QWidget.setTabOrder(self.itemBox, self.quantityBox)
        QWidget.setTabOrder(self.quantityBox, self.storeBox)
        QWidget.setTabOrder(self.storeBox, self.addButton)
        QWidget.setTabOrder(self.addButton, self.cancelButton)
        QWidget.setTabOrder(self.cancelButton, self.shoppinglistsButton)
        QWidget.setTabOrder(self.shoppinglistsButton, self.storesButton)
        QWidget.setTabOrder(self.storesButton, self.categoriesButton)
        QWidget.setTabOrder(self.categoriesButton, self.brandsButton)
        QWidget.setTabOrder(self.brandsButton, self.itemsButton)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Shopping List Generator", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Shopping List for date", None))
#if QT_CONFIG(statustip)
        self.shoppinglistBox.setStatusTip(QCoreApplication.translate("MainWindow", u"Select the date to build the list.", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.refreshButton.setStatusTip(QCoreApplication.translate("MainWindow", u"Click this if you make any changes in the 'Management' section!", None))
#endif // QT_CONFIG(statustip)
        self.refreshButton.setText(QCoreApplication.translate("MainWindow", u"Refresh data", None))
        self.removeButton.setText(QCoreApplication.translate("MainWindow", u"Remove item from list", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Add item to list", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Item to add", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Quantity", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"From store", None))
        self.addButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.cancelButton.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Management", None))
        self.shoppinglistsButton.setText(QCoreApplication.translate("MainWindow", u"Shopping Lists", None))
        self.storesButton.setText(QCoreApplication.translate("MainWindow", u"Stores", None))
        self.categoriesButton.setText(QCoreApplication.translate("MainWindow", u"Categories", None))
        self.brandsButton.setText(QCoreApplication.translate("MainWindow", u"Brands", None))
        self.itemsButton.setText(QCoreApplication.translate("MainWindow", u"Items", None))
    # retranslateUi

