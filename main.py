# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 09:37:34 2022

@author: conny
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

windturbines = pd.read_csv("uswtdb.csv")
print(windturbines)
lightning_by_state = pd.read_excel("lightning_by_state.xlsx")
#get summary stats
windturbines["p_year"].mean()
windturbines["p_year"].median()
windturbines["retrofit_year"].mean()

#get a turbine age variable as the turbine age or the retrofit age
windturbines["age"] =np.where(windturbines["retrofit"] == 1, 2022 -  windturbines["retrofit_year"], 
     2022 -  windturbines["p_year"])


#plot the ages as a histogram
plt.hist(windturbines["age"])
plt.xlabel('Age')
plt.title('Years Since Turbine Construction or Retrofit')
plt.show()
#plot turbine heights (indicative of strike risk)
plt.hist(windturbines["t_ttlh"], color='red')
plt.xlabel('Height')
plt.title('Turbine Height')
plt.show()

#add state lightning data as dataframe with State and abbreviation cols
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

#merge the lightning file with my df combining abbreviations
merge_abbr = pd.merge(lightning_by_state, state_abbr)
#group by state to get summed data
state_grouped = windturbines.groupby("t_state").mean().sort_values(by='age',ascending= False)
#merge turbine data with the lightning/abbr data
turbine_merge = pd.merge(state_grouped, merge_abbr, left_on="t_state", right_on="abbr")

plt.bar(turbine_merge["abbr"], turbine_merge["age"])
plt.xlabel('Average Age')
plt.xticks(rotation=90)
plt.title('Average Turbine Age by State')
plt.show()

plt.bar(turbine_merge["abbr"], turbine_merge["t_cap"])
plt.xlabel('Average Age')
plt.xticks(rotation=90)
plt.title('Average Turbine Capacity by State')
plt.show()

#add lightning data to original data to get figure per project
long_turbine_merge = pd.merge(windturbines, merge_abbr, left_on="t_state", right_on="abbr")
#scatter of avg lightning per sq mile by age
plt.scatter(long_turbine_merge["age"], long_turbine_merge["Average Lightning Count Per Square Mile"], color = "purple")
plt.xlabel('Turbine Age')
plt.ylabel("State Average Lightning Count Per Square Mile")
plt.title('How Lightning Affects Turbine Lifecycle')
plt.show()

