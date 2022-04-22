import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

mtcars = pd.read_csv('LV3/mtcars.csv')
print(mtcars)

print("")
print(mtcars.sort_values(by=['mpg'], ascending=True).head(5)[['car','mpg']])

print("")
print(mtcars[(mtcars.cyl == 8)].sort_values(by=['mpg'], ascending=False).head(3)[['car','mpg']])

print("")
print("AVG potrosnja 6cyl: ",mtcars[(mtcars.cyl == 6)].mpg.sum() / mtcars[(mtcars.cyl == 6)].mpg.count())

print("")
print("AVG potrosnja 4cyl masa izmedju 2000 i 2200lbs: ",mtcars[(mtcars.cyl == 4) & (mtcars.wt >= 2.0) & (mtcars.wt <= 2.2)].mpg.sum()/mtcars[(mtcars.cyl == 4) & (mtcars.wt >= 2.0) & (mtcars.wt <= 2.2)].mpg.count())

print("")
print("Broj automatic vozila: ", mtcars[(mtcars.am == 0)].car.count())

print("")
print("Broj manual vozila: ", mtcars[(mtcars.am == 1)].car.count())

print("")
print("Broj automatic vozila hp>100: ", mtcars[(mtcars.am == 1) & (mtcars.hp > 100)].car.count())

mtcars['wt_in_kg'] = mtcars.wt * 1000 * 0.454
print(mtcars[['car','wt_in_kg']])