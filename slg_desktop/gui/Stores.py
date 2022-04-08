# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stores.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTableView, QVBoxLayout, QWidget)

class Ui_StoresWindow(object):
    def setupUi(self, StoresWindow):
        if not StoresWindow.objectName():
            StoresWindow.setObjectName(u"StoresWindow")
        StoresWindow.resize(400, 600)
        StoresWindow.setMinimumSize(QSize(400, 600))
        self.centralwidget = QWidget(StoresWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.storeView = QTableView(self.centralwidget)
        self.storeView.setObjectName(u"storeView")
        self.storeView.setAlternatingRowColors(True)
        self.storeView.setSelectionMode(QAbstractItemView.SingleSelection)

        self.verticalLayout.addWidget(self.storeView)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.deleteButton = QPushButton(self.centralwidget)
        self.deleteButton.setObjectName(u"deleteButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteButton.sizePolicy().hasHeightForWidth())
        self.deleteButton.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.deleteButton)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.storeEdit = QLineEdit(self.groupBox)
        self.storeEdit.setObjectName(u"storeEdit")
        self.storeEdit.setEnabled(True)

        self.horizontalLayout.addWidget(self.storeEdit)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.locationEdit = QLineEdit(self.groupBox)
        self.locationEdit.setObjectName(u"locationEdit")
        self.locationEdit.setEnabled(False)

        self.horizontalLayout.addWidget(self.locationEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

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


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.groupBox)

        StoresWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(StoresWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 400, 23))
        StoresWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(StoresWindow)
        self.statusbar.setObjectName(u"statusbar")
        StoresWindow.setStatusBar(self.statusbar)

        self.retranslateUi(StoresWindow)

        QMetaObject.connectSlotsByName(StoresWindow)
    # setupUi

    def retranslateUi(self, StoresWindow):
        StoresWindow.setWindowTitle(QCoreApplication.translate("StoresWindow", u"Add, Edit, Delete Stores", None))
#if QT_CONFIG(statustip)
        self.storeView.setStatusTip(QCoreApplication.translate("StoresWindow", u"Select the store to display and edit the name & location.", None))
#endif // QT_CONFIG(statustip)
        self.deleteButton.setText(QCoreApplication.translate("StoresWindow", u"Delete selected store", None))
        self.groupBox.setTitle(QCoreApplication.translate("StoresWindow", u"Add new store", None))
        self.label.setText(QCoreApplication.translate("StoresWindow", u"Store name", None))
        self.label_2.setText(QCoreApplication.translate("StoresWindow", u"Location", None))
        self.addButton.setText(QCoreApplication.translate("StoresWindow", u"Add", None))
        self.cancelButton.setText(QCoreApplication.translate("StoresWindow", u"Cancel", None))
    # retranslateUi

