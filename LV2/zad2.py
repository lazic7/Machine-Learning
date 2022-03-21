import numpy as np 
import matplotlib.pyplot as plt
import collections

array = np.random.randint(1,7,100)
y = collections.Counter(array)
y= [y[1],y[2],y[3],y[4],y[5],y[6]]

x = np.array([1,2,3,4,5,6])

print(y)

plt.bar(x,y)
plt.show()

