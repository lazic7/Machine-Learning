import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

mtcars = pd.read_csv('C:/Users/lazic/Documents/FERIT/PSU_LV/LV3/mtcars.csv')
print(mtcars)

print("")
mtcars = mtcars.sort_values(by=['mpg'], ascending=False)
print(mtcars.head(5).car)

print("")
mtcars = mtcars.sort_values(by=['mpg'], ascending=True)
print(mtcars[(mtcars.cyl == 8)].head(3).car)

print("")
print("AVG potrosnja 6cyl: ",mtcars[(mtcars.cyl == 6)].mpg.sum() / mtcars[(mtcars.cyl == 6)].mpg.count())

print("")
print("AVG potrosnja 4cyl masa izmedju 2000 i 2200lbs: ",mtcars[(mtcars.cyl == 4) & (mtcars.wt >= 2.0) & (mtcars.wt <= 2.2)].mpg.sum()/mtcars[(mtcars.cyl == 4) & (mtcars.wt >= 2.0) & (mtcars.wt <= 2.2)].mpg.count())