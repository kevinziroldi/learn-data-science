import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('country-wise-average.csv')
df.dropna(inplace=True)

df_waste = df.sort_values(by='Wasting')
df_waste.reset_index(inplace=True)
df_waste.drop(['index'], axis=1, inplace=True)

slices = [df_waste.loc[i,'Wasting'] for i in range(len(df_waste))]
labels = [df_waste.loc[i,'Country'] for i in range(len(df_waste))]

print(df_waste.Wasting.max())

plt.pie(slices, labels=labels, startangle=90)
plt.show()
