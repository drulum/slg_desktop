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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QLineEdit, QListView, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_BrandsWindow(object):
    def setupUi(self, BrandsWindow):
        if not BrandsWindow.objectName():
            BrandsWindow.setObjectName(u"BrandsWindow")
        BrandsWindow.resize(600, 300)
        BrandsWindow.setMinimumSize(QSize(600, 300))
        BrandsWindow.setMaximumSize(QSize(600, 300))
        self.centralwidget = QWidget(BrandsWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.brandView = QListView(self.centralwidget)
        self.brandView.setObjectName(u"brandView")

        self.verticalLayout.addWidget(self.brandView)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addButton = QPushButton(self.centralwidget)
        self.addButton.setObjectName(u"addButton")

        self.horizontalLayout.addWidget(self.addButton)

        self.deleteButton = QPushButton(self.centralwidget)
        self.deleteButton.setObjectName(u"deleteButton")

        self.horizontalLayout.addWidget(self.deleteButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.nameEdit = QLineEdit(self.centralwidget)
        self.nameEdit.setObjectName(u"nameEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.nameEdit)


        self.horizontalLayout_2.addLayout(self.formLayout)

        BrandsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(BrandsWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 600, 23))
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
        self.brandView.setStatusTip(QCoreApplication.translate("BrandsWindow", u"Select the brand to edit the name.", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.addButton.setStatusTip(QCoreApplication.translate("BrandsWindow", u"Add a new brand entry.", None))
#endif // QT_CONFIG(statustip)
        self.addButton.setText(QCoreApplication.translate("BrandsWindow", u"Add", None))
#if QT_CONFIG(statustip)
        self.deleteButton.setStatusTip(QCoreApplication.translate("BrandsWindow", u"CAUTION: The selected brand will be deleted.", None))
#endif // QT_CONFIG(statustip)
        self.deleteButton.setText(QCoreApplication.translate("BrandsWindow", u"Delete", None))
        self.label.setText(QCoreApplication.translate("BrandsWindow", u"Brand name", None))
#if QT_CONFIG(statustip)
        self.nameEdit.setStatusTip(QCoreApplication.translate("BrandsWindow", u"\"Tropicana\", \"Heinz\", \"Yeo Valley\" etc.", None))
#endif // QT_CONFIG(statustip)
    # retranslateUi

