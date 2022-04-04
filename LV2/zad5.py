import numpy as np
import matplotlib.pyplot as plt

def board(xdim,ydim,xelements,yelements):

    black = np.zeros((xdim,ydim), dtype='uint8')
    white = 255*np.ones((xdim,ydim), dtype='uint8')

    row1=black
    row2=white

    for y in range(yelements-1):
        if y%2==0:
            row1=np.hstack((row1,white))
            row2=np.hstack((row2,black))
        else:
            row1=np.hstack((row1,black))
            row2=np.hstack((row2,white))

    


    return row1

    

img = board(50,50,2,4)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.show()