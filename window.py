# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 611, 401))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.data_load_pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.data_load_pushButton.setObjectName("data_load_pushButton")
        self.gridLayout_2.addWidget(self.data_load_pushButton, 2, 0, 1, 1)
        self.data_select_pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.data_select_pushButton.setObjectName("data_select_pushButton")
        self.gridLayout_2.addWidget(self.data_select_pushButton, 1, 0, 1, 1)
        self.data_clear_pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.data_clear_pushButton.setObjectName("data_clear_pushButton")
        self.gridLayout_2.addWidget(self.data_clear_pushButton, 3, 0, 1, 1)
        self.data_source_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.data_source_lineEdit.setObjectName("data_source_lineEdit")
        self.gridLayout_2.addWidget(self.data_source_lineEdit, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.data_select_comboBox_1 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.data_select_comboBox_1.setObjectName("data_select_comboBox_1")
        self.verticalLayout.addWidget(self.data_select_comboBox_1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.data_select_comboBox_2 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.data_select_comboBox_2.setObjectName("data_select_comboBox_2")
        self.verticalLayout.addWidget(self.data_select_comboBox_2)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.data_select_comboBox_3 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.data_select_comboBox_3.setObjectName("data_select_comboBox_3")
        self.verticalLayout.addWidget(self.data_select_comboBox_3)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.data_load_pushButton.setText(_translate("MainWindow", "Load"))
        self.data_select_pushButton.setText(_translate("MainWindow", "Select"))
        self.data_clear_pushButton.setText(_translate("MainWindow", "Clear"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.label.setText(_translate("MainWindow", "TextLabel"))

