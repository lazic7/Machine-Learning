import numpy as np
import skimage.io
import matplotlib.pyplot as plt

img = skimage.io.imread('LV2/tiger.png', as_gray=True) #dtype uint8, dimenzije: 640x960
plt.figure(1)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)



img2 = img.copy()
rows, cols = img2.shape
rotated = np.zeros((cols,rows))
mirrored = np.zeros((rows,cols))
lowres = np.zeros((rows,cols))

for i in range(rows):
    for j in range(cols):
            img2[i][j] += 50 #jaci brightness

for i in range(rows):
    rotated[:,-i] = img2[i,:] #rotacija za 90

for j in range(cols):
    mirrored[:,j] = img2[:,cols-1-j] #zrcaljenje

            

plt.figure(2)
plt.imshow(rotated, cmap='gray', vmin=0,vmax=255)

plt.figure(3)
plt.imshow(mirrored, cmap='gray', vmin=0,vmax=255)

plt.figure(4)
plt.imshow(lowres, cmap='gray', vmin=0,vmax=255)



plt.show()