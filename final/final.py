import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



# df = pd.read_csv('FinalBase.csv', sep=';',  low_memory=False)
# df.fillna(0, inplace=True)
# df = df.drop(df[df['Schengen State'] == 0].index)
# df = df.drop(df.columns[0], axis=1)
# df = df.sample(frac = 1)

df = pd.read_csv('drop.csv')

#df.to_csv('drop.csv')

column = 'Uniform visas applied for'

# Task 2
print('Task 2:')
print('Median: ', df[column].median())
print('Mode: ', df.mode()[column][0])
print('Average: ', df[column].mean())
print('Minimum: ', df[column].min())
print('Maximum: ', df[column].max())

# Task 3
print('Task 3:')
maxVisas = df[column].max()
df['delta'] = abs(df[column] - maxVisas)
print(df.loc[:, 'delta'], sep='\n')

# Tasks 4, 5
font = {'size': 15}
plt.rc('font', **font)
groups = df.groupby('Schengen State').size()
plt.pie = groups.plot(kind='pie', figsize=(15, 15), autopct='%.2f',
     title='Number of visas to the country', legend=False, subplots=True)
plt.show()

# Task 6
font = {'size': 7}
plt.rc('font', **font)
fig, ax = plt.subplots()

def generateChart(country):
     consulate = list(set(df.loc[df['Schengen State'] == country, 'Consulate'].values))
     consulates = list(df.loc[df['Schengen State'] == country, column].values)
     x = np.arange(len(consulate))
     plt.bar(x[:5], consulates[:5])
     plt.xticks(x[:5], consulate[:5])
     plt.show()

generateChart('Belgium')
generateChart('Austria')
generateChart('Finland')

# Task 7
print('Task 7:')
groups = []
names = []
for key, groupdf in df.groupby('Schengen State'):
     groups.append(groupdf)
     names.append(key)

groups[4] = groups[4].sort_values(by=['Uniform visas applied for', 'Consulate'])
groups[6] = groups[6].sort_values(by=['Total ATVs and uniform visas not issued', 'Country where consulate is located'])
print(names[4], '\n', groups[4][['Uniform visas applied for', 'Consulate']])
print(names[6], '\n', groups[6][['Total ATVs and uniform visas not issued', 'Country where consulate is located']])


