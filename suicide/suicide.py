import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('suicide.csv')

# selecting only suicides of 2016 of people aged 15-24
df_2016_young = df.loc[df.year == 2016]
df_2016_young = df_2016_young.loc[df_2016_young.age == '15-24 years']

# index reset
df_2016_young.sort_values(by='country', inplace=True)
df_2016_young.reset_index(inplace=True)
df_2016_young.drop(['index'],axis=1,inplace=True)

# sum of male and female suicides by country
total_number = []
for i in range(0, len(df_2016_young), 2):
    for j in range(2):
        total_number.append(df_2016_young.loc[i,'suicides/100k pop'] + df_2016_young.loc[i+1,'suicides/100k pop'])

df_2016_young['total/100k pop'] = pd.Series(total_number)

df_2016_young.drop(['sex'],axis=1,inplace=True)

delete_index = [i for i in range(0, len(df_2016_young), 2)]
df_2016_young.drop(delete_index, inplace=True)
df_2016_young.reset_index(inplace=True)
df_2016_young.drop(['index'],axis=1,inplace=True)


slices = [df_2016_young.loc[i, 'total/100k pop'] for i in range(len(df_2016_young))]
labels = [df_2016_young.loc[i, 'country'] for i in range(len(df_2016_young))]
plt.pie(slices, labels=labels, startangle=90)
plt.title('SUICIDE in 2016\nAGE 15-24')
plt.show()

# suicide in the years in the world
df_years =  df.groupby('year')['suicides/100k pop'].sum()

years = [i for i in range(1985,2017)]
suicide_no = [df_years.iloc[i] for i in range(len(df_years))]
plt.bar(years, suicide_no, color='#FF7F50')
plt.title('Suicides by the years')
plt.xlabel('Years')
plt.ylabel('Number of suicides in the world')
plt.show()

# suicides males vs females in last 10 years
# create a dataframe with only last 10 years datas
df_shortened = df.copy()
df_shortened.sort_values(by='year',inplace=True)
delete_list = []
for i in range(len(df_shortened)):
    if df_shortened.loc[i,'year'] < 1996:
        delete_list.append(i)
df_shortened.drop(delete_list, inplace=True)
df_shortened.reset_index(inplace=True)
df_shortened.drop(['index'],axis=1,inplace=True)
# groupby sex
df_sexes = df_shortened.groupby('sex')['suicides/100k pop'].sum()

slices = [df_sexes.iloc[0], df_sexes.iloc[1]]
labels = ['female', 'male']
plt.title('Suicides im the last 10 years\nMALES VS FEMALES')
plt.pie(slices, labels=labels)
plt.show()


# suicide for age
df_age = df.groupby('age')['suicides/100k pop'].sum()
slices = [df_age.iloc[i] for i in range(len(df_age))]
labels = [df_age.index[i] for i in range(len(df_age))]
plt.pie(slices, labels=labels, startangle=90)
plt.title('Suicides by age')
plt.show()
