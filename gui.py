#!/usr/bin/python2
# -*- coding: utf-8 -*-

"""
QSee functionality replacement

Author: Liang Yu
Website: zetcode.com
Last edited: September 2017
TODO: do better documentation
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from window import Ui_MainWindow
from DataLoader import DataLoader

class QseeGui(QMainWindow, Ui_MainWindow):
    """
    class ties gui and reading elements together
    """
    def __init__(self, parent=None):
        super(qsee_gui, self).__init__()
        self.setupUi(self)

        #
        self.file_name = ''
        self.data_loader = DataLoader()

        # connect buttons
        self.data_select_pushButton.clicked.connect(self.file_load_popup)
        self.data_load_pushButton.clicked.connect(self.load_file)
        self.data_clear_pushButton.clicked.connect(self.clear_loaded_data)

    def file_load_popup(self):
        """
        bring up file dialog window
        """
        self.file_name = QFileDialog.getOpenFileName()[0]
        self.data_loader.fname = self.file_name
        self.data_source_lineEdit.setText(self.file_name)

    def load_file(self):
        """
        load file
        """
        self.data_loader.load_excel()
        fields = self.data_loader.data_fields
        self.data_select_comboBox_1.addItems(fields)
        self.data_select_comboBox_2.addItems(fields)
        self.data_select_comboBox_3.addItems(fields)

    def clear_loaded_data(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = qsee_gui()
    form.show()
    sys.exit(app.exec_())
    