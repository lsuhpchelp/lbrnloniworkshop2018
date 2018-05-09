import numpy as np
from scipy.misc import imread, imresize
import matplotlib.pyplot as plt

img = imread('cat.jpg')
#img_tinted = img * [1, 0.95, 0.9]
#img_tinted = img * [0.4, 0.8, 0.8]
#img_tinted = np.average(img)
#img_tinted = np.average(img,axis=2)
#img_tinted = img.average(axis=2)
img_tinted = np.average(img,weights=[0.299,0.587,0.114],axis=2)
#img_tinted = img
#img_tinted = np.average(img,axis=2).reshape(img.shape[0],img.shape[1],1)
print img_tinted.shape
print img.shape
#print img[0].shape
#print img[0].shape

# Show the original image
plt.subplot(1, 2, 1)
plt.imshow(img)

# Show the tinted image
plt.subplot(1, 2, 2)

# A slight gotcha with imshow is that it might give strange results
# if presented with data that is not uint8. To work around this, we
# explicitly cast the image to uint8 before displaying it.
#plt.imshow(np.uint8(img_tinted), cmap=plt.get_cmap('gray'))
plt.imshow(np.uint8(img_tinted), cmap='gray')
#plt.imshow(img_tinted)
plt.show()
