import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('covid19_data.csv')

df_ita = df.loc[df.Country == 'Italy']
# problem: df_ita has the same index of df, but has to start from 0
df_ita.reset_index(inplace=True)
df_ita = df_ita.drop(['index', 'Unnamed: 0'], axis=1)
# removing all the days without any confermed case
i = 0
ok = True
while ok == True and i < len(df_ita):
    if df_ita.loc[i, 'Confirmed'] != 0:
        ok = False
    else:
        i += 1
df_ita = df_ita.iloc[i:,:]
# reset the index after removing some elements
df_ita.reset_index(inplace=True)
df_ita = df_ita.drop(['index'], axis=1)

# maximum number of new infected in a day
maxInfections = df_ita.newConfirmed.max()
print('Maximum number of infections in one day:', maxInfections)
maxRowInf = 0
while df_ita.loc[maxRowInf,'newConfirmed'] != maxInfections:
    maxRowInf += 1
print('Day of the maximum number of infection:', df_ita.loc[maxRowInf,'Date'])

maxDeaths = df_ita.newDeath.max()
maxRowDeath = 0
while df_ita.loc[maxRowDeath,'newDeath'] != maxDeaths:
    maxRowDeath += 1

maxHospitalizations = df_ita.newRecovered.max()    
maxRowRec = 0
while df_ita.loc[maxRowRec, 'newRecovered'] != maxHospitalizations:
    maxRowRec +=1

# coronavirus in the world
infectionPerCountry = df.groupby('Country').Confirmed.max()
slices = [infectionPerCountry[i] for i in range(len(infectionPerCountry))]
labels = []
for i in range (len(infectionPerCountry)):
    if infectionPerCountry[i] > 100000:
        labels.append(infectionPerCountry.index[i])
    else:
        labels.append('')


plt.pie(slices,labels=labels, startangle=90)
plt.title('COVID19 in the world')
plt.show()


# graph to show infections, deaths and hospitalizations in italy
x_ita = [df_ita.loc[i,'Date'] for i in range(len(df_ita))]
yInfection_ita = [df_ita.loc[i,'newConfirmed'] for i in range(len(df_ita))]
yDeaths = [df_ita.loc[i,'newDeath'] for i in range(len(df_ita))]
yHospitalizations = [df_ita.loc[i,'newRecovered'] for i in range(len(df_ita))]
plt.plot(x_ita, yInfection_ita, linewidth=2.5, color='r', label='Number of new infected')
plt.text(maxRowInf,yInfection_ita[maxRowInf], maxInfections, color='#FF00FF')
plt.plot(x_ita, yDeaths, linewidth=2.5, color='k', label='Number of new deaths')
plt.text(maxRowDeath, yDeaths[maxRowDeath], maxDeaths, color='#FF00FF')
plt.plot(x_ita, yHospitalizations, linewidth=2.5, color='g', label='Number of new recovered')
plt.text(maxRowRec, yHospitalizations[maxRowRec], maxHospitalizations, color='#FF00FF')
plt.title('COVID19 in Italy')
plt.xlabel('days')
plt.ylabel('number of people')
# dato che si sovrappongono, raggruppo e inclino
plt.xticks(x_ita, rotation = 60)
plt.locator_params(axis='x', nbins=10)
plt.tick_params(axis='both', labelsize=7)
plt.legend()
plt.show()

# italy vs us infections graph
df_us = df.loc[df.Country == 'US'] # creating the us dataframe
df_us.reset_index(inplace=True)
df_us = df_us.drop(['index', 'Unnamed: 0'], axis=1) # reset of the index
i = 0 # removing all the first dates with no infection
ok = True
while ok == True and i < len(df_us):
    if df_us.loc[i, 'Confirmed'] != 0:
        ok = False
    else:
        i += 1
df_us = df_us.iloc[i:,:]
df_us.reset_index(inplace=True) # second reset of the index
df_us = df_us.drop(['index'], axis=1)

# in the us the first case of covid is before than in italy
# so I use the x_us for both
x_us = [df_us.loc[i,'Date'] for i in range(len(df_us))]
population_us = 328200000
yInfection_us = [df_us.loc[i,'newConfirmed']/population_us for i in range(len(df_us))]

# I assign 0 to yIta in the extra days
y_adapted = []
for i in range(len(x_us)-len(x_ita)):
    y_adapted.append(0)
population_ita = 60360000
y_adapted += yInfection_ita
for i in range(len(y_adapted)):
    y_adapted[i] /= population_ita

# creazione del grafico
plt.plot(x_us, y_adapted, linewidth=2.5, color='r', label='Infections/population in Italy')
plt.plot(x_us, yInfection_us, linewidth=2.5, color='b', label='Infections/population in America')
plt.xticks(x_ita, rotation = 60)
plt.locator_params(axis='x', nbins=10)
plt.tick_params(axis='both', labelsize=7)
plt.xlabel('Date')
plt.ylabel('Number of infected / population')
plt.title('Italy vs America\nNumber of infected/population')
plt.legend()
plt.show()

plt.scatter(df_ita.Date, df_ita.newConfirmed)
plt.title('COVID19 in Italy')
plt.xlabel('days')
plt.ylabel('number of new cases')
plt.show()

plt.plot(df_ita.Confirmed, linewidth=2.5, color='#E30B5C')
plt.title('COVID19 in Italy')
plt.xlabel('days')
plt.ylabel('number of total cases')
plt.show()