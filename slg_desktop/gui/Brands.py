# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'brands.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTableView, QVBoxLayout, QWidget)

class Ui_BrandsWindow(object):
    def setupUi(self, BrandsWindow):
        if not BrandsWindow.objectName():
            BrandsWindow.setObjectName(u"BrandsWindow")
        BrandsWindow.resize(400, 600)
        BrandsWindow.setMinimumSize(QSize(0, 0))
        self.centralwidget = QWidget(BrandsWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.brandView = QTableView(self.centralwidget)
        self.brandView.setObjectName(u"brandView")

        self.verticalLayout.addWidget(self.brandView)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.deleteButton = QPushButton(self.centralwidget)
        self.deleteButton.setObjectName(u"deleteButton")

        self.horizontalLayout.addWidget(self.deleteButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


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

        self.brandEdit = QLineEdit(self.groupBox)
        self.brandEdit.setObjectName(u"brandEdit")

        self.horizontalLayout_2.addWidget(self.brandEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.addButton = QPushButton(self.groupBox)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.addButton)

        self.cancelButton = QPushButton(self.groupBox)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.cancelButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addWidget(self.groupBox)

        BrandsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(BrandsWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 400, 23))
        BrandsWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(BrandsWindow)
        self.statusbar.setObjectName(u"statusbar")
        BrandsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(BrandsWindow)

        QMetaObject.connectSlotsByName(BrandsWindow)
    # setupUi

    def retranslateUi(self, BrandsWindow):
        BrandsWindow.setWindowTitle(QCoreApplication.translate("BrandsWindow", u"Add, Edit, Delete Brands", None))
#if QT_CONFIG(statustip)
        self.brandView.setStatusTip(QCoreApplication.translate("BrandsWindow", u"Double click the field to edit it.", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.deleteButton.setStatusTip(QCoreApplication.translate("BrandsWindow", u"CAUTION: The selected brand will be deleted.", None))
#endif // QT_CONFIG(statustip)
        self.deleteButton.setText(QCoreApplication.translate("BrandsWindow", u"Delete selected brand", None))
        self.groupBox.setTitle(QCoreApplication.translate("BrandsWindow", u"GroupBox", None))
        self.label.setText(QCoreApplication.translate("BrandsWindow", u"Brand name", None))
#if QT_CONFIG(statustip)
        self.brandEdit.setStatusTip(QCoreApplication.translate("BrandsWindow", u"\"Tropicana\", \"Heinz\", \"Yeo Valley\" etc.", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.addButton.setStatusTip(QCoreApplication.translate("BrandsWindow", u"Add a new brand entry.", None))
#endif // QT_CONFIG(statustip)
        self.addButton.setText(QCoreApplication.translate("BrandsWindow", u"Add", None))
#if QT_CONFIG(statustip)
        self.cancelButton.setStatusTip(QCoreApplication.translate("BrandsWindow", u"Cancel the addition and reset the fields.", None))
#endif // QT_CONFIG(statustip)
        self.cancelButton.setText(QCoreApplication.translate("BrandsWindow", u"Cancel", None))
    # retranslateUi

