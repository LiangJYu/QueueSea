#!/usr/bin/python2
# -*- coding: utf-8 -*-

"""
QSee functionality replacement

Author: Liang Yu
Last edited: September 2017
TODO: better documentation
"""

import random
from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import matplotlib.pyplot as plt

class PlotCanvas(FigureCanvasQTAgg):
    """
    where pretty plots go
    """
    def __init__(self, parent=None):
        self.fig = plt.figure()

        FigureCanvasQTAgg.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvasQTAgg.setSizePolicy(self,
                                        QSizePolicy.Expanding,
                                        QSizePolicy.Expanding)
        FigureCanvasQTAgg.updateGeometry(self)
        self.plot()

    def plot(self, x=[], y=[]):
        """
        draw stuff
        """
        self.fig.clear()
        if not len(x) or not len(y):
            x = range(25)
            y = [random.random() for i in range(25)]
        ax = self.figure.add_subplot(111)
        ax.plot(x, y, 'o')
        ax.set_title('PyQt Matplotlib Example')
        ax.grid()
        self.draw()