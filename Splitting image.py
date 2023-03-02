import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img=cv.imread('Hazard10.jpg')

b,g,r=cv.split(img)#split separates the photo into giving values by rgb, but there's only one color channel, so it greyscales the image
#based on image of only blue, or only red, or only green color channel
cv.imshow('BLUE',b)
cv.imshow('GREEN',g)
cv.imshow('RED',r)

img_merged=cv.merge([r,g,b])#split stores values of where the blue or red color is in the image.
#if you assign wrong values in the "merged" image, then in this case, the blue assigned areas become red, and vice versa
cv.imshow('Merged BGR',img_merged)

plt.subplot(221)
plt.imshow(b)

plt.subplot(222)
plt.imshow(g)

plt.subplot(223)
plt.imshow(r)

plt.subplot(224)
plt.imshow(img_merged)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()

