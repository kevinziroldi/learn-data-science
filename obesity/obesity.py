import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('obesity-cleaned.csv')

df.rename(columns={'Obesity (%)':'Percentage'},inplace=True)
df.Percentage.replace('No data','NaN',inplace=True) # empty values are No data instead of NaN

step = [] # creating a new percentage columns without the part between [], only percentage
Perc = []

for i in range(len(df.index)):
    step.append(df.loc[i,'Percentage'].split(' '))
    Perc.append(step[i][0])

df.drop(columns='Percentage',inplace=True)
     
df['Percentage'] = Perc
df.Percentage = df.Percentage.astype('float64')
df.dropna(inplace=True)

input_country=input('Inserire un paese del mondo: ') # mean percentage of a country, taken in input
print('The mean percentage of obesity in ',input_country,'is of ',df.loc[df.Country == input_country].Percentage.mean())

print(df.groupby('Country').Percentage.mean().sort_values(ascending=False)) # mean percentage of every country, sorted

years_mean = df.groupby('Year').Percentage.mean().sort_values(ascending=False) # mean percentage of every yeat to see how it increases in the world by the years
print(years_mean)

plt.plot(years_mean, color='#30D5C8', linewidth=3) # creating a graph in matplotlib
plt.title('OBESITY PERCENTAGE BY THE YEARS')
plt.xlabel('year')
plt.ylabel('mean obesity percentage in the world')
plt.show()

dfsex = df.copy()
dfsex.drop(dfsex[dfsex['Sex']=='Both sexes'].index,inplace=True)
print(dfsex.groupby('Sex').Percentage.mean().sort_values())
