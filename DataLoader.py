#!/usr/bin/python2
# -*- coding: utf-8 -*-

"""
QSee functionality replacement

Author: Liang Yu
Website: zetcode.com
Last edited: September 2017
TODO: better documentation
"""

import pandas as pd

class DataLoader(object):
    """
    loads different types of data for visualization
    """
    def __init__(self, parent=None, fname=''):
        self.fname = fname
        self.dataframe = []
        self.data_fields = []

    def load_excel(self):
        """
        load an excel file and extract field names
        """
        self.dataframe = pd.read_excel(self.fname, 'Master')
        self.data_fields = list(self.dataframe)
