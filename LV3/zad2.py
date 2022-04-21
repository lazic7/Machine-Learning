import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

mtcars = pd.read_csv('C:\\Users\\lazic\\Documents\\FERIT\\PSU_LV\\LV3\\mtcars.csv')
print(mtcars)

mtcars.groupby('cyl')['mpg'].mean().plot.bar()
plt.show()

mtcars.boxplot(by='cyl', column='wt')
plt.show()

mtcars.boxplot(by='am', column='mpg')
plt.show()


mtcars.plot.scatter(x = 'qsec', y='hp', c='am', colormap='viridis')
plt.show()