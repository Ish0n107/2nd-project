import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img=cv.imread('OpenCV.png')

blur=cv.blur(img,(25,25))#takes 25 and 25 rows of pixels in bunches, average the rgb value, and then assign that value to all pixels


gauss_blur=cv.GaussianBlur(img,(25,25),0)#again, 0 parameter greyscales image

plt.subplot(131)
plt.imshow(img)
plt.title("Original")



plt.subplot(132)
plt.imshow(blur)
plt.title("Averaging")

plt.subplot(133)
plt.imshow(gauss_blur)
plt.title("Gaussian blur")

plt.show()
