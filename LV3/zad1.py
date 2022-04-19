import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

mtcars = pd.read_csv('C:/Users/lazic/Documents/FERIT/PSU_LV/LV3/mtcars.csv')

mtcars = mtcars.sort_values(by=['mpg'], ascending=False)
print(mtcars.head(5).car)

print("")

mtcars = mtcars.sort_values(by=['mpg'], ascending=True)
print(mtcars[(mtcars.cyl == 8)].head(3).car)

print(mtcars[(mtcars.cyl == 6)].mpg.sum()/mtcars.car.count())