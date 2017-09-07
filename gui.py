#!/usr/bin/python2
# -*- coding: utf-8 -*-

"""
QSee functionality replacement

Author: Liang Yu
Last edited: September 2017
TODO: do better documentation
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
from window import Ui_MainWindow
from DataLoader import DataLoader
from PlotCanvas import PlotCanvas

class QseeGui(QMainWindow, Ui_MainWindow):
    """
    class ties gui and reading elements together
    """
    def __init__(self, parent=None):
        super(QseeGui, self).__init__()
        self.setupUi(self)

        # setup plot
        self.plot_canvas = PlotCanvas(self.plot_widget)
        self.plot_widget.layout().addWidget(self.plot_canvas)
        #self.plot_widget.layout.addItems(self.plot_canvas)

        # partially setup plot controls
        self.toolbar = NavigationToolbar2QT(self.plot_canvas, self)
        self.toolbar.hide()

        self.file_name = ''
        self.data_loader = DataLoader()

        self.init()

    def init(self):
        """
        additional init missing from setupUI()
        """
        # connect data loading interface
        self.data_select_pushButton.clicked.connect(self.file_load_popup)
        self.data_load_pushButton.clicked.connect(self.load_file)
        self.data_clear_pushButton.clicked.connect(self.clear_loaded_data)
        self.data_source_lineEdit.textChanged.connect(self.rename_fname)

        # connect plotting buttons
        self.plot_zoom_pushButton.clicked.connect(self.toolbar.zoom)
        self.plot_pan_pushButton.clicked.connect(self.toolbar.pan)
        self.plot_reset_pushButton.clicked.connect(self.toolbar.home)

    def file_load_popup(self):
        """
        bring up file dialog window
        """
        self.file_name = QFileDialog.getOpenFileName()[0]
        self.data_loader.fname = self.file_name
        self.data_source_lineEdit.setText(self.file_name)

    def rename_fname(self):
        """
        do something when text in lineEdit changes
        :return:
        """
        self.data_loader.fname = self.data_source_lineEdit.text()

    def load_file(self):
        """
        load file
        """
        if self.data_source_lineEdit.text():
            if not self.data_loader.fname:
                self.data_loader.fname = self.data_source_lineEdit.text()
            self.data_loader.load_excel()
            fields = self.data_loader.data_fields
            self.data_select_comboBox_1.addItems(fields)
            self.data_select_comboBox_2.addItems(fields)
            self.data_select_comboBox_3.addItems(fields)

    def clear_loaded_data(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = QseeGui()
    form.show()
    sys.exit(app.exec_())
