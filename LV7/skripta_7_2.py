from keras.models import load_model
from matplotlib import pyplot as plt
from skimage.transform import resize
from skimage import color
import matplotlib.image as mpimg
import numpy as np

filename = 'LV6/test.png'

img = mpimg.imread(filename)
img = color.rgb2gray(img[:,:,0:3])
img = resize(img, (28, 28))


plt.figure()
plt.imshow(img, cmap=plt.get_cmap('gray'))
plt.show()


img = img.reshape(1, 28, 28, 1)
img = img.astype('float32')


# TODO: ucitaj model
model = load_model("CNN/")

# TODO: napravi predikciju 
digit = np.argmax(model.predict(img), axis=1)

# TODO: ispis rezultat
print("------------------------")
print(digit[0])



