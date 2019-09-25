import pandas as pd
import matplotlib.pyplot as plt
import datetime
import calendar
from collections import Counter
import numpy as np


df = pd.read_csv('visa - visa (3).csv', sep=',',  low_memory=False)
df.fillna(0, inplace=True)
df = df.drop(df[df['Schengen State'] == 0].index)

#task 2
column = 'Uniform visas applied for'
df[column] = pd.to_numeric(df[column])

df.to_csv('FinalBase.csv', sep = ';')

print('Median: ', df[column].median())
print('Mode: ', df.mode()[column][0])
print('Average: ', df[column].mean())
print('Minimum: ', df[column].min())
print('Maximum: ', df[column].max())

# task 3
# max = df['btc_transaction_fees'].max()
# df['delta'] = abs(df['btc_transaction_fees'] - max)
# print(df['delta'], sep='\n')
print(df)
# task 4
font = {'size': 15}
plt.rc('font', **font)
groups = df.groupby('Schengen State').size()
plt.pie = groups.plot(kind='pie', figsize=(15, 15), autopct='%.2f',
     title='btc_transaction_fees', legend=False, subplots=True)
plt.show()

