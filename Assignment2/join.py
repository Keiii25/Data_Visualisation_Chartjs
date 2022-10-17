import pandas as pd

# file1 = pd.read_csv('./data/temperature_changes.csv')
# file2 = pd.read_csv('./data/deaths.csv')
# file1 = file1[file1['Year']==2020]
# file3 = pd.merge(file1, file2, on='ISO3 Code')
# print(file3)
# file3 = file3[['Country_y', 'ISO3 Code', 'Value', 'Deaths']]
# file3.to_csv('temperature_deaths.csv')

# import numpy as np
# import pandas as pd
# import plotly.express as px
# import os
# from datetime import datetime

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
# df = pd.read_csv('./data/FAOSTAT_data_1-10-2022.csv')
# df = df[df['Months']=='December']
# df2 = pd.read_csv('./data/FAOSTAT_data_11-24-2020.csv')
# df3 = pd.merge(df, df2, on='Country')
# # print(df3)
# df3.to_csv('temperature_changes.csv')

# df = pd.read_csv('./data/global-fossil-fuel-consumption.csv')
# gas = df[['Year', 'Gas (TWh)']]
# oil = df[['Year', 'Oild (TWh)']]
# coal = df[['Year', 'Coal (TWh)']]
# gas = gas.rename(columns={'Gas (TWh)': 'Value'})
# oil = oil.rename(columns={'Oild (TWh)': 'Value'})
# coal = coal.rename(columns={'Coal (TWh)': 'Value'})
# gas['type'] = 'Gas (TWh)'
# oil['type'] =  'Oil (TWh)'
# coal['type'] = 'Coal (TWh)'

df = pd.read_csv('./data/ice_age.csv')
one = df[['Year', '1YI']]
two = df[['Year', '2YI']]
three = df[['Year', '3YI']]
four = df[['Year', '4YI']]
five = df[['Year', '5+YI']]

one = one.rename(columns={'1YI': 'Value'})
two = two.rename(columns={'2YI': 'Value'})
three = three.rename(columns={'3YI': 'Value'})
four = four.rename(columns={'4YI': 'Value'})
five = five.rename(columns={'5+YI': 'Value'})

one['type'] = 1
two['type'] = 2
three['type'] = 3
four['type'] = 4
five['type'] = 5

df2 = pd.concat([one, two, three, four, five], axis=0)
df2.to_csv('seaice_age.csv')

# df2 = pd.concat([gas, oil, coal], axis=0)
# # df3 = pd.merge(df2, coal, on='Year')
# print(df2)
# df2.to_csv('fossils_fuel_usage.csv')
# df = pd.read_csv('./data/seaice.csv')
# df = df[df['hemisphere'] == 'north']
# df = df[['Year', 'Month', 'Extent']]
# df2 = df.groupby(['Year', 'Month']).agg('mean')

# print(df2)
# df2.to_csv('sea_ice_extent.csv')