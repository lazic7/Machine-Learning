import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('diabetes.csv')
print(df.info())
print(df.describe())
print(df.isnull().sum())

#provjeravamo korelaciju izmedju varijabli podataka
sns.heatmap(df.corr(), annot=True, fmt =".2f", cmap="coolwarm")
plt.show()


