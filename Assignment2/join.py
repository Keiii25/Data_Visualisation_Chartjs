# import pandas as pd

# file1 = pd.read_csv('pm2_5.csv')
# file2 = pd.read_csv('death-rates-from-air-pollution.csv')

# print(file1)
# file3 = pd.merge(file1, file2, on='Code')

# file3 = file3[['Entity', 'Code', 'Level', 'Deaths']]
# file3.to_csv('air_pollutions_deaths.csv')

import numpy as np
import pandas as pd
import plotly.express as px
import os
from datetime import datetime

# data = []
# data.append(['Iceberg', 'Length', 'Width', 'Latitude', 'Longitude', 'Remarks', 'Last_update'])

# for dirname, _, filenames in os.walk('./archive/'):
#     for filename in filenames:
#         print(os.path.join(dirname, filename))
#         with open(os.path.join(dirname, filename), 'r') as file:
#             i = 0
#             for line in file.readlines():
#                 temp = []
#                 if i != 0:
#                     for el in line.split(','):
#                         temp.append(el.strip())
#                     data.append(temp)
#                     #print(line.split(','))
#                     #data.append(line.split(',').strip())
#                 i += 1
# df = pd.DataFrame(data)
# df = pd.read_csv('ice_berg_location.csv')
# # print(str(df['Last_update'][0]))
# df['Year'] = pd.to_datetime(df['Last_update'], format='%m/%d/%Y')
# df['Year'] = df['Year'].dt.year
# # print(df)
# df.to_csv('ice_berg_location.csv')
# df = pd.read_csv('city_temperature.csv')
# df = df[['Year', 'Country', 'AvgTemperature']]
# d = df.groupby(['Year', 'Country'])['AvgTemperature'].mean().reset_index()
# d['AvgTemperature'] = (d['AvgTemperature']-32) * 5 / 9
# d = d[d['Year']>500]
# # print(d)
# d.to_csv('country_temperature.csv')
# df = pd.read_csv('GlobalLandTemperaturesByCountry.csv')
# df['Year'] = pd.to_datetime(df['dt'], format='%Y-%m-%d')
# df['Year'] = df['Year'].dt.year
# df = df[['Year', 'Country', 'AverageTemperature']]
# d = df.groupby(['Year', 'Country'])['AverageTemperature'].mean().reset_index()
# d = d[d['Year']< 1995]
# d2 = pd.read_csv('country_temperature.csv')
# d2 = d2.rename(columns={'AvgTemperature': 'AverageTemperature'})
# d2 = d2.drop(d2.columns[0], axis=1)
# print(d2)
# d3 = pd.concat([d, d2])
# d3.to_csv('country_temperature2.csv')
# df = pd.read_csv('country_temperature2.csv')
# df = df.dropna()
# df.to_csv('country_temperature2.csv')
df = pd.read_csv('./data/FAOSTAT_data_1-10-2022.csv')
df = df[df['Months']=='December']
df.to_csv('temperature_changes.csv')
