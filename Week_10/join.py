import pandas as pd

file1 = pd.read_csv('pm2_5.csv')
file2 = pd.read_csv('death-rates-from-air-pollution.csv')

print(file1)
file3 = pd.merge(file1, file2, on='Code')

file3 = file3[['Entity', 'Code', 'Level', 'Deaths']]
file3.to_csv('air_pollutions_deaths.csv')