#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
QSee functionality replacement
Code adapted from:
https://stackoverflow.com/questions/7733693/matplotlib-overlay-plots-with-different-scales
https://sukhbinder.wordpress.com/2013/12/16/simple-pyqt-and-matplotlib-example-with-zoompan/

Author: Liang Yu
Last edited: September 2017
TODO: better documentation
"""

import random
import matplotlib
from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import matplotlib.pyplot as plt

class PlotCanvas(FigureCanvasQTAgg):
    """
    where pretty plots go
    """
    def __init__(self, parent=None):
        self.fig = plt.figure()
        self.axes = []

        FigureCanvasQTAgg.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvasQTAgg.setSizePolicy(self,
                                        QSizePolicy.Expanding,
                                        QSizePolicy.Expanding)
        FigureCanvasQTAgg.updateGeometry(self)
        self.plot_triple_yaxis()

    def plot(self, x=[], y=[]):
        """
        draw stuff
        """
        self.fig.clear()
        if not len(x) or not len(y):
            x = range(25)
            y = [random.random() for i in x]
        ax = self.figure.add_subplot(111)
        ax.plot(x, y, 'o')
        ax.set_title('PyQt Matplotlib Example')
        ax.grid()
        self.draw()

    def plot_triple_yaxis(self, x=[], y=[], y_labels=[]):
        """
        draw stuff on 3 seperate axis
        :return:
        """
        # wipe and start anew
        self.fig.clear()

        if not len(x) or not len(y):
            x = range(25)
            # TODO: random to purty sines
            y = [[random.random() for i in x] for j in range(3)]
            y_labels = ["{}".format(str(i)) for i in range(3)]
            x_label = ''
        else:
            x_label = 'time'

        # create 3 axes
        ax = self.figure.add_subplot(111)
        self.axes = [ax, ax.twinx(), ax.twinx()]

        temp = 0.75
        self.figure.subplots_adjust(right=temp)
        right_additive = (0.98-temp)/float(2)

        # Move the last y-axis spine over to the right by x% of the width of the axes
        ax = self.axes[2]
        ax.spines['right'].set_position(('axes', 1. + right_additive))
        ax.set_frame_on(True)
        ax.patch.set_visible(False)
        ax.yaxis.set_major_formatter(matplotlib.ticker.OldScalarFormatter())

        colors = ('Green', 'Red', 'Blue')
        markers = 'xos'
        for i, ax in enumerate(self.axes):
            if len(y[i]) == len(x):
                ax.plot(x, y[i], marker=markers[i], color=colors[i])
                ax.set_ylabel(y_labels[i], color=colors[i])
                ax.tick_params(axis='y', colors=colors[i])
        self.axes[0].set_xlabel(x_label)
        self.axes[0].grid()
        self.axes[0].set_title('3 Axis Plot')

        self.draw()
