import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.linear_model as lm

from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error, max_error

# ucitavanje ociscenih podataka
df = pd.read_csv('LV4/cars_processed.csv')
print(df.info())

#odabir ulaznih velicina
df = df.drop(['name', 'mileage', 'seats'], axis = 1) #izbacili smo ove parametre

x = df[['km_driven', 'year', 'engine', 'max_power']]
y = df['selling_price']

#podjela na train i test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=300)

#skaliranje ulaznih velicina
Scaler = MinMaxScaler()
x_train_s=Scaler.fit_transform(x_train)
x_test_s = Scaler.transform(x_test)

#model
linearModel = lm.LinearRegression()
linearModel.fit(x_train_s,y_train)

#evaluacija modela
y_pred_train = linearModel.predict(x_train_s)
y_pred_test = linearModel.predict(x_test_s)

print("MAE: ", max_error(y_pred_test,y_test))
