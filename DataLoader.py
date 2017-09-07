#!/usr/bin/python2
# -*- coding: utf-8 -*-

"""
QSee functionality replacement

Author: Liang Yu
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
        self.data_fields = ['']
        self.time_key = ''
        self.time = []

    def load_excel(self):
        """
        load an excel file and extract field names
        """
        self.dataframe = pd.read_excel(self.fname, 'BW ES QSee')

        temp_data_fields = list(self.dataframe)

        # assume there exists only 1 column for time
        self.time_key = [x for x in temp_data_fields if 'date' in x.lower() or 'time' in x.lower()][0]
        # remove time key from data_fields
        if self.time_key:
            temp_data_fields.remove(self.time_key)

        # get prepare time values
        if not self.time:
            self.time = self.dataframe[self.time_key].values

        self.data_fields.extend(temp_data_fields)

    def get_data(self, key=''):
        """
        get data
        :return: list of times
        """
        values = self.dataframe[key].values
        return values
