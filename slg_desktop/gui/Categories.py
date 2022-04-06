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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QLineEdit, QListView, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_CategoriesWindow(object):
    def setupUi(self, CategoriesWindow):
        if not CategoriesWindow.objectName():
            CategoriesWindow.setObjectName(u"CategoriesWindow")
        CategoriesWindow.resize(600, 300)
        CategoriesWindow.setMinimumSize(QSize(600, 300))
        CategoriesWindow.setMaximumSize(QSize(600, 300))
        self.centralwidget = QWidget(CategoriesWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.categoryView = QListView(self.centralwidget)
        self.categoryView.setObjectName(u"categoryView")

        self.verticalLayout.addWidget(self.categoryView)

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

        CategoriesWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(CategoriesWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 600, 23))
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
        self.categoryView.setStatusTip(QCoreApplication.translate("CategoriesWindow", u"Select the category to edit the name.", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.addButton.setStatusTip(QCoreApplication.translate("CategoriesWindow", u"Add a new category.", None))
#endif // QT_CONFIG(statustip)
        self.addButton.setText(QCoreApplication.translate("CategoriesWindow", u"Add", None))
#if QT_CONFIG(statustip)
        self.deleteButton.setStatusTip(QCoreApplication.translate("CategoriesWindow", u"CAUTION: The selected category will be deleted.", None))
#endif // QT_CONFIG(statustip)
        self.deleteButton.setText(QCoreApplication.translate("CategoriesWindow", u"Delete", None))
        self.label.setText(QCoreApplication.translate("CategoriesWindow", u"Category name", None))
#if QT_CONFIG(statustip)
        self.nameEdit.setStatusTip(QCoreApplication.translate("CategoriesWindow", u"\"Fresh\", \"Chilled\", \"Baked Goods\" etc.", None))
#endif // QT_CONFIG(statustip)
    # retranslateUi

