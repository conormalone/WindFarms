# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 09:37:34 2022

@author: conny
"""
import pandas as pd
import numpy as np

windturbines = pd.read_csv("uswtdb.csv")
print(windturbines)
lightning_by_state = pd.read_excel("lightning_by_state.xlsx")
#check ages of turbines
windturbines["p_year"].mean()
windturbines["p_year"].median()
windturbines["retrofit_year"].mean()

state_abbr = pd.DataFrame({'State': ["Alabama",
    "Alaska",
    "Arizona",
    "Arkansas",
    "California",
    "Colorado",
    "Connecticut",
    "Delaware",
    "Florida",
    "Georgia",
    "Hawaii",
    "Idaho",
    "Illinois",
    "Indiana",
    "Iowa",
    "Kansas",
    "Kentucky",
    "Louisiana",
    "Maine",
    "Maryland",
    "Massachusetts",
    "Michigan",
    "Minnesota",
    "Mississippi",
    "Missouri",
    "Montana",
    "Nebraska",
    "Nevada",
    "New Hampshire",
    "New Jersey",
    "New Mexico",
    "New York",
    "North Carolina",
    "North Dakota",
    "Ohio",
    "Oklahoma",
    "Oregon",
    "Pennsylvania",
    "Rhode Island",
    "South Carolina",
    "South Dakota",
    "Tennessee",
    "Texas",
    "Utah",
    "Vermont",
    "Virginia",
    "Washington",
    "West Virginia",
    "Wisconsin",
    "Wyoming",
    "District of Columbia",
    ],
                    'abbr': ['AK','AL','AR','AZ','CA','CO','CT','DC','DE','FL','GA',
          'HI','IA','ID','IL','IN','KS','KY','LA','MA','MD','ME',
          'MI','MN','MO','MS','MT','NC','ND','NE','NH','NJ','NM',
          'NV','NY','OH','OK','OR','PA','RI','SC','SD','TN','TX',
          'UT','VA','VT','WA','WI','WV','WY']})

#
merge_abbr = pd.merge(lightning_by_state, state_abbr)
turbine_merge = pd.merge(windturbines, merge_abbr, left_on="t_state", right_on="abbr")
