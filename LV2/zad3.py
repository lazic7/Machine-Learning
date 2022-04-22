import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(open("LV2/mtcars.csv", "rb"), usecols=(1,2,3,4,5,6), delimiter=",", skiprows=1)
i = 0
mpg = data[:,0]
hp = data[:,3]
wt = data[:,5]
s = [3*n for n in range(len(wt))]

plt.scatter(mpg, hp, s=s)
plt.title("Ovisnost mpg o hp")
plt.xlabel("mpg")
plt.ylabel("hp")
plt.show()

print("Min mpg: ", np.min(mpg))
print("Max mpg: ", np.max(mpg))
print("Average mpg: ", np.average(mpg))

while i < 2:
    if (data[i,1] == 6):
        vSixData.append(data[i])

print(vSixData)