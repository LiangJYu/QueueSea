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
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.plot_widget = QtWidgets.QWidget(self.centralwidget)
        self.plot_widget.setMinimumSize(QtCore.QSize(400, 0))
        self.plot_widget.setObjectName("plot_widget")
        self.horizontalLayout.addWidget(self.plot_widget)
        self.control_verticalLayout = QtWidgets.QVBoxLayout()
        self.control_verticalLayout.setObjectName("control_verticalLayout")
        self.load_data_vericalLayout = QtWidgets.QGridLayout()
        self.load_data_vericalLayout.setObjectName("load_data_vericalLayout")
        self.data_clear_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.data_clear_pushButton.setObjectName("data_clear_pushButton")
        self.load_data_vericalLayout.addWidget(self.data_clear_pushButton, 3, 0, 1, 1)
        self.data_load_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.data_load_pushButton.setObjectName("data_load_pushButton")
        self.load_data_vericalLayout.addWidget(self.data_load_pushButton, 2, 0, 1, 1)
        self.data_select_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.data_select_pushButton.setObjectName("data_select_pushButton")
        self.load_data_vericalLayout.addWidget(self.data_select_pushButton, 1, 0, 1, 1)
        self.data_source_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.data_source_lineEdit.setObjectName("data_source_lineEdit")
        self.load_data_vericalLayout.addWidget(self.data_source_lineEdit, 0, 0, 1, 1)
        self.control_verticalLayout.addLayout(self.load_data_vericalLayout)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.control_verticalLayout.addWidget(self.label_2)
        self.data_select_comboBox_1 = QtWidgets.QComboBox(self.centralwidget)
        self.data_select_comboBox_1.setObjectName("data_select_comboBox_1")
        self.control_verticalLayout.addWidget(self.data_select_comboBox_1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.control_verticalLayout.addWidget(self.label_3)
        self.data_select_comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.data_select_comboBox_2.setObjectName("data_select_comboBox_2")
        self.control_verticalLayout.addWidget(self.data_select_comboBox_2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.control_verticalLayout.addWidget(self.label)
        self.data_select_comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.data_select_comboBox_3.setObjectName("data_select_comboBox_3")
        self.control_verticalLayout.addWidget(self.data_select_comboBox_3)
        self.horizontalLayout.addLayout(self.control_verticalLayout)
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
        self.data_clear_pushButton.setText(_translate("MainWindow", "Clear"))
        self.data_load_pushButton.setText(_translate("MainWindow", "Load"))
        self.data_select_pushButton.setText(_translate("MainWindow", "Select"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.label.setText(_translate("MainWindow", "TextLabel"))

