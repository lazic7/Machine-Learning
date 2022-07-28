import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from keras.layers import Dense, Dropout
from keras.models import Sequential
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix

df = pd.read_csv('diabetes.csv')
print(df.info())
print(df.describe())

#ispravljamo podatke unutar dataset-a
df['Glucose'] = df['Glucose'].replace(0, df['Glucose'].mean())
df['BloodPressure'] = df['BloodPressure'].replace(0, df['BloodPressure'].mean())

df['BMI'] = df['BMI'].replace(0, df['BMI'].median())
df['SkinThickness'] = df['SkinThickness'].replace(0, df['SkinThickness'].median())
df['Insulin'] = df['Insulin'].replace(0, df['Insulin'].median())


#provjeravamo korelaciju izmedju varijabli podataka
plt.figure(figsize=(15,10))
sns.heatmap(df.corr(), annot=True, fmt =".2f", cmap="coolwarm")
plt.show()

#provjeravamo dataset, koliko osoba ima dijabetes, a koliko ne
sns.countplot('Outcome', data=df)
plt.show()

#provjeravamo odnos razine glukoze u krvi na BMI i broj godina
plt.figure(figsize=(20,10))
sns.scatterplot(data=df, x="Glucose", y="BMI", hue="Age", size="Age")
plt.show()

#normalna razina glukoze prema nasim istrazivanjima je ispod 140mg/dL krvi. preko toga je visoka sansa za uzrok dijabetesa
sns.violinplot(data=df, x="Outcome", y="Glucose", split=True, inner="quartile", linewidth=1)
plt.show()

#izvlacimo podatke iz dataseta koji su nam potrebni

dataset = df.values

x = dataset[:, 0:8]
y = dataset[:, 8]


#skaliramo podatke
scaler = StandardScaler()
x = scaler.fit_transform(x)
print(x)

#dijelimo skup izvucenih podataka na train i test skupove
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=42)


#konfiguracija mreze, tu pokusavamo definirati kako ce nas model za predikciju izgledati
model = Sequential()
model.add(Dense(units=8, input_dim=8, kernel_initializer='normal', activation='relu'))
model.add(Dense(units=200, input_dim=8, kernel_initializer='normal', activation='relu'))
model.add(Dense(units=64, input_dim=200, kernel_initializer='normal', activation='relu'))
model.add(Dropout(0.25))
model.add(Dense(units=1, activation='sigmoid'))
model.summary()

#podesavanje karakteristika procesa ucenja
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

#provedba ucenja modela
model.fit(x_train, y_train, epochs=200, batch_size=5)

#confusion_matrix
y_pred = model.predict(x_test)
y_pred = (y_pred > 0.5).astype('int')

cf_matrix = confusion_matrix(y_test, y_pred)
sns.heatmap(cf_matrix, annot=True, cmap='Blues')
plt.show()


