import sys
import csv
import matplotlib as plt
import pandas as pd


fdf = pd.read_csv('firstofjuly.csv', sep = ',')
sdf = pd.read_csv('secondofjuly.csv', sep = ',')

df = pd.concat([fdf, sdf]).reset_index(drop = True) #Drop???

count = 0
# for index, row in df.iterrows():
#     if row['precipitation'] == 'yes':
#         count += 1

length1 = int(len(df)/2)
length2 = int(len(df) - length1)

for i in range (length1):
    if (df['precipitation'][i] == 'yes') ^ (df['precipitation'][i+length1] == 'yes'):
        count += 1

print(count / len(df) * 100)


count1 = 1
count2 = 2
count3 = 3
count4 = 4

metersPersecond = 10
# for i in range(length1):
#     if (df['overcast'][i] == 'clear') or (df['overcast'][i+length1] == 'clear'):
#         if df['wind'][i] >= 10 or df['wind'][i+length1] >= 10:
#             count2 += 1
#         elif df['wind'][i] > 10 or df['wind'][i+length1] > 10:
#             count1 += 1
#     elif (df['overcast'][i] == 'clear') or (df['overcast'][i+length1] == 'clear'):

labels = 'Python', 'C++', 'Ruby', 'Java'
sizes = [215, 130, 245, 210]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # explode 1st slice

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()


i = 0
while i < length1:
    if (df['precipitation'][i] == 'yes') or (df['precipitation'][i+length1] == 'yes'):
        df = df.drop([i, i + length1])
    elif (df['temperature'][i] > 20) or (df['temperature'][i+length1] > 20):
        df = df.drop([i, i + length1])
    i += 1

print(df)
