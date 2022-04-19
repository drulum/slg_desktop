# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'categories.ui'
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

class Ui_CategoriesWindow(object):
    def setupUi(self, CategoriesWindow):
        if not CategoriesWindow.objectName():
            CategoriesWindow.setObjectName(u"CategoriesWindow")
        CategoriesWindow.resize(400, 600)
        self.centralwidget = QWidget(CategoriesWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.categoryView = QTableView(self.centralwidget)
        self.categoryView.setObjectName(u"categoryView")

        self.verticalLayout.addWidget(self.categoryView)

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

        self.categoryEdit = QLineEdit(self.groupBox)
        self.categoryEdit.setObjectName(u"categoryEdit")

        self.horizontalLayout_2.addWidget(self.categoryEdit)


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

        CategoriesWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(CategoriesWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 400, 23))
        CategoriesWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(CategoriesWindow)
        self.statusbar.setObjectName(u"statusbar")
        CategoriesWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CategoriesWindow)

        QMetaObject.connectSlotsByName(CategoriesWindow)
    # setupUi

    def retranslateUi(self, CategoriesWindow):
        CategoriesWindow.setWindowTitle(QCoreApplication.translate("CategoriesWindow", u"Add, Edit, Delete Categories", None))
#if QT_CONFIG(statustip)
        self.categoryView.setStatusTip(QCoreApplication.translate("CategoriesWindow", u"Double click the field to edit it.", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.deleteButton.setStatusTip(QCoreApplication.translate("CategoriesWindow", u"CAUTION: The selected category will be deleted.", None))
#endif // QT_CONFIG(statustip)
        self.deleteButton.setText(QCoreApplication.translate("CategoriesWindow", u"Delete seleced category", None))
        self.groupBox.setTitle(QCoreApplication.translate("CategoriesWindow", u"GroupBox", None))
        self.label.setText(QCoreApplication.translate("CategoriesWindow", u"Category name", None))
#if QT_CONFIG(statustip)
        self.categoryEdit.setStatusTip(QCoreApplication.translate("CategoriesWindow", u"\"Fresh\", \"Chilled\", \"Baked Goods\" etc.", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.addButton.setStatusTip(QCoreApplication.translate("CategoriesWindow", u"Add a new category.", None))
#endif // QT_CONFIG(statustip)
        self.addButton.setText(QCoreApplication.translate("CategoriesWindow", u"Add", None))
#if QT_CONFIG(statustip)
        self.cancelButton.setStatusTip(QCoreApplication.translate("CategoriesWindow", u"Cancel the addition and reset the fields.", None))
#endif // QT_CONFIG(statustip)
        self.cancelButton.setText(QCoreApplication.translate("CategoriesWindow", u"Cancel", None))
    # retranslateUi

