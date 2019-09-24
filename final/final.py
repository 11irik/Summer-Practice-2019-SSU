import pandas as pd
import matplotlib.pyplot as plt
import datetime
import calendar
from collections import Counter
import numpy as np

df = pd.read_csv('bdataset.csv', sep=';',  low_memory=False)
df.fillna(0, inplace=True)

# 2 медиана, мода, средняя, минимум, максимум
print('Медиана: ', df['Первое_измерение_АД_систолическое '
                      '(значение. мм. рт.ст/пропуск)'].median())
print('Мода: ', Counter(df['Первое_измерение_АД_систолическое '
        '(значение. мм. рт.ст/пропуск)']).most_common(1)[0][0])
print('Среднее: ', df['Первое_измерение_АД_систолическое '
                      '(значение. мм. рт.ст/пропуск)'].mean())
print('Минимум: ', df['Первое_измерение_АД_систолическое '
                      '(значение. мм. рт.ст/пропуск)'].min())
print('Максимум: ', df['Первое_измерение_АД_систолическое '
                       '(значение. мм. рт.ст/пропуск)'].max())

# 3 Создать новый столбец, в котором разместить разницу между
# максимумом и текущим значением для некоторого числового параметра.
max_pressure = df['Первое_измерение_АД_систолическое ' 
                  '(значение. мм. рт.ст/пропуск)'].max()
df['delta'] = abs(df['Первое_измерение_АД_систолическое '
            '(значение. мм. рт.ст/пропуск)'] - max_pressure)
print('Разница между максимумом и текушим значением '
      'для каждой строки:', df['delta'], sep='\n')
# 4,5  Разбить данные на несколько блоков (не менее 3,
# приблизительно равных по размеру)
# по некоторому критерию (критерий определить самостоятельно).
# Привести круговую диаграмму для проделанного разбиения.
font = {'size': 10}
plt.rc('font', **font)
groups = df.groupby('Уровень глюкозы плазмы крови '
                    '(значение. ммоль/л /пропуск)').size()
plt.pie = groups.plot(kind='pie', figsize=(15, 15), autopct='%.2f',
     title='Уровень глюкозы плазмы крови', legend=False, subplots=True)
plt.show()

# 6 В зависимости от особенностей набора данных
# для каждого блока построить график (гистограмму)
sub_df1 = df.loc[df['Пол (Мужской/Женский/Нет данных - 1/2/0)'] == 1,
                 ['Первое_измерение_АД_систолическое ' 
                  '(значение. мм. рт.ст/пропуск)']]
sub_df2 = df.loc[df['Пол (Мужской/Женский/Нет данных - 1/2/0)'] == 2,
                 ['Первое_измерение_АД_систолическое ' 
                  '(значение. мм. рт.ст/пропуск)']]
n, bins, patches = plt.hist(sub_df1.values, 5, facecolor='blue',
                            alpha=0.5)
plt.show()
n, bins, patches = plt.hist(sub_df2.values, 5, facecolor='red',
                            alpha=0.5)
plt.show()

# 7 Сгруппировать данные (GroupBy) по некоторому признаку и сохранить
# результаты в новые таблицы. Для каждой новой таблицы провести
# сортировку по сложному ключу, состоящему из нескольких признаков.
# Для каждой таблицы своя сортировка.
data_array = []
for key, group_df in df.groupby('Пол (Мужской/Женский/Нет данных - 1/2/0)'):
    data_array.append(group_df)
data_array[0].sort_values(by=['Дата рождения',
  'Уровень мочевины сыворотки крови (значение. ммоль/л /пропуск)'])
data_array[1].sort_values(by=['Дата внесения в Регистр',
   'Общий холестерин сыворотки крови (значение. мг/дл /пропуск)'])
print(data_array[0])
print(data_array[1])
# 8 Для вариантов № 1, 2, 4, 13, 20, 22, 23: отобразить распределение
# некоторого параметра по дням недели (в каждой группе), по месяцам
# (суммарно).
df['dayOfWeek'] = df['Дата внесения в Регистр'].apply(
    lambda x: calendar.day_abbr[datetime.datetime.strptime(x,
                                    "%d.%m.%Y").date().weekday()])
dayOfWeek = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
res = []
for x in dayOfWeek:
    res.append(df.loc[df.dayOfWeek == x, 'Первое_измерение_АД_систолическое '
                      '(значение. мм. рт.ст/пропуск)'])
colors = ['#cc0605', '#009900', '#0000FF', '#FFFFFF', '#FF33FF',
          '#CCFF00', '#666666']
fig, ax = plt.subplots()
for i in range(len(res)):
    x_axis = np.full(len(res[i]), i+1)
    ax.scatter(x_axis, res[i], c=colors[i], s=1, label=dayOfWeek[i])
ax.set_facecolor('black')
ax.set_title('Распределение артерииального давления')
fig.set_figwidth(5)
fig.set_figheight(5)
plt.legend(loc='upper left', markerscale=10)
plt.show()
