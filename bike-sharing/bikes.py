import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import RobustScaler
from sklearn.metrics import mean_absolute_error
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder

df = pd.read_csv('hour.csv')
y = df['cnt']

columns_to_be_deleted = ['cnt', 'casual', 'registered', 'dteday', 'instant']
df.drop(columns_to_be_deleted, axis=1, inplace=True)

# per distinguere una variabile a categoria provo a fare un'operazione matematica
# ad esempio se il tempo è 4, faccio tempo/2 fa sereno, NON ha senso
transformers = [
    ['one_hot', OneHotEncoder(), ['season', 'yr', 'mnth', 'hr', 'weekday','weathersit']],
    ['scaler', RobustScaler(), ['temp', 'atemp', 'hum', 'wctrindspeed']] # anche se in questo caso ha un effetto minimo, dato che i valori sono molto vicini
]

ct = ColumnTransformer(transformers, remainder='passthrough')
X = ct.fit_transform(df)

X_train, X_test, y_train, y_test = train_test_split(X, y)
model = LinearRegression()
model.fit(X_train, y_train)

prediction_train = model.predict(X_train)
prediction_test = model.predict(X_test)

mae_train = mean_absolute_error(y_train, prediction_train)
mae_test = mean_absolute_error(y_test, prediction_test)

print('Median cnt:', np.median(y))
print('MAE Train:', mae_train)
print('MAE Test:', mae_test)
print("end")
