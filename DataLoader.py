#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
QSee functionality replacement

Author: Liang Yu
Last edited: September 2017
TODO: better documentation
"""

import pandas as pd
from OnePass import OnePass

class DataLoader(object):
    """
    loads different types of data for visualization
    """
    def __init__(self, parent=None, fname=''):
        self.fname = fname
        self.df = []
        self.data_fields = ['']
        self.time_key = ''
        self.time = []

    def load_excel_baseline(self):
        """
        load an excel file and extract field names
        """
        plant_df = pd.read_excel(self.fname, 'PlantData')
        temp_data_fields = list(plant_df)
        plant_df[temp_data_fields[2:]] = plant_df[temp_data_fields[2:]].apply(pd.to_numeric)

        # assume there exists only 1 column for time
        self.time_key = [x for x in temp_data_fields if 'date' in x.lower() or 'time' in x.lower()][0]
        # remove time key from data_fields
        if self.time_key:
            temp_data_fields.remove(self.time_key)

        # get prepare time values
        # TODO: merge date and time fields
        if not self.time:
            self.time = plant_df[self.time_key].values
            
        self.data_fields.extend(temp_data_fields)

        # calculate n-pass derivative parameters and concat to plant baseline dataframe
        n_pass_derived = OnePass(plant_df)
        self.df = pd.concat([plant_df, n_pass_derived.df], axis=1)
        self.data_fields.extend(n_pass_derived.data_fields)

    def get_data(self, key=''):
        """
        get data
        :return: np.array of keyed data or empty list if key is invalid
        """
        values = []
        if key in self.data_fields and key:
            values = self.df[key].values
        return values
