#!/usr/bin/python2
# -*- coding: utf-8 -*-

"""
compute single pass

Author: Liang Yu
Last edited: September 2017
TODO: do better documentation
"""

import pandas as pd
import numpy as np
import collections

water_tcf0 = 3400.
salt_tcf0 = 5500.
min_per_day = 1440.
membrane_area = 2800.
elements_per_vessel = 7.


def calculate_tcf(t, tcf0):
    """
    calculate material temperature adjusted temperature correction factor
    :param t: temperature in Celcius
    :param tcf: material temperature correction factor
    :return: temperature adjusted temperature correction factor
    """
    adjusted_tcf = np.exp(tcf0*(1./298.15-1./(t+273.15)))  # sorry; magic numbers using for now
    return adjusted_tcf


def calculate_tds(cond):
    """
    calculate total dissolved solids from conductivity
    :param cond: conductivity
    :return: total dissolved solids
    """
    tds = 2.0282*1e-6*cond**2+0.522*cond    # IDK what magic numbers are
    return tds


class OnePass:
    """
    compute single pass derivative parameters from basic plant parameters
    """
    def __init__(self, plant_df=''):
        self.df = []
        self.data_fields = []
        if not plant_df.empty:
            self.create_dataframe(plant_df)

    def create_dataframe(self, plant_df=''):
        """

        :param plant_df:
        :return:
        """
        Plant = collections.namedtuple('Plant', 'date time ph temp \
                                                conc_flow perm_flow \
                                                feed_pres conc_pres perm_press \
                                                feed_cond perm_cond')

        # assign plant labels to namedtuple for easier referencing
        plant = Plant(*[plant_df[x].values for x in list(plant_df)])

        # calculate reused parameters
        feed_flow = plant.conc_flow + plant.perm_flow
        recovery = plant.perm_flow/feed_flow
        cpf = np.exp((0.75*2*recovery)/(2-recovery)/elements_per_vessel)
        feed_tds = calculate_tds(plant.feed_cond)
        perm_tds = calculate_tds(plant.perm_cond)
        avg_feed_tds = cpf * feed_tds * (-np.log(1 - recovery) / recovery)
        diff_pres = plant.feed_pres - plant.conc_pres
        perm_osm_pres = 1.8*perm_tds/55850*0.0821*(273+plant.temp)*14.7
        flux = plant.perm_flow * min_per_day / membrane_area
        tcf_water = calculate_tcf(plant.temp, water_tcf0)
        tcf_salt = calculate_tcf(plant.temp, salt_tcf0)
        avg_feed_osm_pres = 0.0385 * avg_feed_tds * (plant.temp + 273.15) / (1e3 - avg_feed_tds / 1e3)
        net_driving_pres = plant.feed_pres - diff_pres / 2. - avg_feed_osm_pres - plant.perm_press + perm_osm_pres
        norm_salt_pass = (perm_tds/avg_feed_tds)*(plant.perm_flow*feed_tds*avg_feed_tds[0]*tcf_salt[0])/(plant.perm_flow[0]*feed_tds[0]*avg_feed_tds*tcf_salt)

        # assign parameters to dataframe
        temp = pd.DataFrame({'Feed Temp (°C)': plant.temp,
                             'TCF (Water)': tcf_water,
                             'TCF (Salt)': tcf_salt,
                             'Feed Flow (gpm)': feed_flow,
                             'Recovery (%)': recovery,
                             'Flux (GFD)': flux,
                             'Differential Press (psi)': diff_pres,
                             'TMP (psi)': plant.feed_pres - plant.perm_press,
                             'Feed TDS (ppm)': feed_tds,
                             'Perm TDS (ppm)': perm_tds,
                             'Concentration Polarization Factor': cpf,
                             'Average Feed TDS (ppm)': avg_feed_tds,
                             'Average Feed Osmotic Pressure (psi)': avg_feed_osm_pres,
                             'Permeate Osmotic Pressure (psi)': perm_osm_pres,
                             'Net Driving Pressure (psi)': net_driving_pres,
                             'A-Value [Specific Flux] (gfd/psi)': flux/net_driving_pres/tcf_water,
                             'B Value \n[STC] \n(m/s)': plant.perm_flow*perm_tds/tcf_salt/264.17/60./(membrane_area*0.0929)/(avg_feed_tds - perm_tds),
                             'Normalized Permeate Flow (gpm)': plant.perm_flow * net_driving_pres[0]* tcf_water[0] / (net_driving_pres * tcf_water),
                             'Normalized Salt  (%)\nPassage': norm_salt_pass,
                             'Normalized Differential Pressure (psi)': diff_pres*(((feed_flow[0]+plant.conc_flow[0])/2.)**1.5)/(((feed_flow+plant.conc_flow)/2.)**1.5),
                             'rejection': 1-norm_salt_pass,
                             'Projected FP (wet test: [], psi)': (-1.95*plant.temp) + 149.73,
                             'Projected FP (specs: [], psi)': (-1.9907*plant.temp) + 152.03,
                             'Projected Permeate TDS (wet test: [], ppm)': (0.605*plant.temp) - 5.79,
                             'Projected Permeate TDS (specs, ppm)': (0.69*plant.temp) - 6.5714})
        self.df = temp
        self.data_fields = list(temp)
