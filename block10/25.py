import matplotlib.pyplot as plt
import pandas as pd


fdf = pd.read_csv('firstofjuly.csv', sep = ',')
sdf = pd.read_csv('secondofjuly.csv', sep = ',')

df = pd.concat([fdf, sdf]).reset_index(drop = True) #Drop???

count = 0
length = int(len(df) / 2)

for i in range (length):
    if (df['precipitation'][i] == 'yes') ^ (df['precipitation'][i + length] == 'yes'):
        count += 1
print('Task 1: ', count / len(df) * 100, '%')


count1 = 1
count2 = 2
count3 = 3
count4 = 4

df1 = df.loc[(df["overcast"] == 'clear') & (df["wind"] >= 10)]
df2 = df.loc[(df["overcast"] == 'clear') & (df["wind"] > 10)]
df3 = df.loc[(df["overcast"] != 'clear') & (df["wind"] >= 10)]
df4 = df.loc[(df["overcast"] != 'clear') & (df["wind"] > 10)]

sizes = [df1.size, df2.size, df3.size, df4.size]
labels = 'C & w>=10', 'C & w>10', 'notC & w>=10', 'notC & w>10'
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # explode 1st slice

plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.show()


i = 0
while i < length:
    if (df['precipitation'][i] == 'yes') or (df['precipitation'][i + length] == 'yes'):
        df = df.drop([i, i + length])
    elif (df['temperature'][i] > 20) or (df['temperature'][i + length] > 20):
        df = df.drop([i, i + length])
    i += 1

print('tast 3:\n', df)