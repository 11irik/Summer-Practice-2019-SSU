import matplotlib as plt
import matplotlib.pyplot as plt
import pandas as pd

fdf = pd.read_csv('firstofjuly.csv', sep = ',')
sdf = pd.read_csv('secondofjuly.csv', sep = ',')

df = pd.concat([fdf, sdf]).reset_index(drop = True)

count = 0

length1 = int(len(df)/2)
length2 = int(len(df) - length1)

for i in range (length1):
    if (df['precipitation'][i] == 'yes') ^ (df['precipitation'][i+length1] == 'yes'):
        count += 1

print(count / len(df) * 100)

df1 = df.loc[(df["overcast"] != 'clear') & (df["wind"] >= 10)]
df2 = df.loc[(df["overcast"] != 'clear') & (df["wind"] > 10)]
df3 = df.loc[(df["overcast"] != 'clear') & (df["wind"] >= 10)]
df4 = df.loc[(df["overcast"] != 'clear') & (df["wind"] > 10)]
sizes = [df1.size, df2.size, df3.size, df4.size]

labels = 'Python', 'C++', 'Ruby', 'Java'
sizes = [215, 130, 245, 210]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # explode 1st slice
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()

# df.groupby('overcast')
# labels = 'Python', 'C++', 'Ruby', 'Java'
# sizes = [215, 130, 245, 210]
# colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
# explode = (0.1, 0, 0, 0)  # explode 1st slice
#
# # Plot
#
# plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
#
# plt.axis('equal')
# plt.show()


i = 0
while i < length1:
    if (df['precipitation'][i] == 'yes') or (df['precipitation'][i+length1] == 'yes'):
        df = df.drop([i, i + length1])
    elif (df['temperature'][i] > 20) or (df['temperature'][i+length1] > 20):
        df = df.drop([i, i + length1])
    i += 1

print(df)
