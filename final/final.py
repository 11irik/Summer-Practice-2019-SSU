import pandas as pd
import matplotlib.pyplot as plt
import random
import datetime
import calendar
from collections import Counter
import numpy as np


df = pd.read_csv('FinalBase.csv', sep=';',  low_memory=False)
df.fillna(0, inplace=True)
df = df.drop(df[df['Schengen State'] == 0].index)

#task 2
column = 'Uniform visas applied for'

print('Median: ', df[column].median())


print('Mode: ', df.mode()[column][0])
#print('????: ', Counter(df[column]).most_common())
print(df[df[column] == 16])

print('Average: ', df[column].mean())
print('Minimum: ', df[column].min())
print('Maximum: ', df[column].max())

# task 3
max = df[column].max()
df['delta'] = abs(df[column] - max)
print(df.loc[:, 'delta'], sep='\n')

# task 4
font = {'size': 15}
plt.rc('font', **font)
groups = df.groupby('Schengen State').size()
plt.pie = groups.plot(kind='pie', figsize=(15, 15), autopct='%.2f',
     title='Number of visas to the country', legend=False, subplots=True)
plt.show()







consulate = list(set(df.loc[df['Schengen State'] == 'Austria', 'Consulate'].values))
print(consulate)
print(len(consulate))

cons = list(df.loc[df['Schengen State'] == 'Austria', column].values)

print(cons)
print(len(cons))

x = np.arange(len(consulate))
#
font = {'size': 7}
plt.rc('font', **font)
fig, ax = plt.subplots()
plt.bar(x[:5], cons[:5])
plt.xticks(x[:5], consulate[:5])

plt.show()









# 6 ? ??????????? ?? ???????????? ?????? ??????
# ??? ??????? ????? ????????? ?????? (???????????)
# countries = list(set(df.loc[:, 'Schengen State'].values))
#
# res = []
# for x in countries:
#     res.append(df.loc[df['Schengen State'] == x, column])
# colors = ['#cc0605', '#009900', '#0000FF', '#FFFFFF', '#FF33FF',
#           '#CCFF00', '#666666']
# fig, ax = plt.subplots()

# for i in range(len(res)):
#     x_axis = np.full(len(res[i]), i+1)
#     ax.scatter(x_axis, res[i].values, c=colors[i], s=1, label=countries[i])
# ax.set_facecolor('black')
# ax.set_title('????????????? ?????????? ??? ?? ???????')
# fig.set_figwidth(5)
# fig.set_figheight(5)
# plt.legend(loc='upper left', markerscale=10)
# plt.show()

