import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img=cv.imread('hazard10.jpg')
cv.imshow('IMAGE',img)

img_RGB=cv.cvtColor(img,cv.COLOR_BGR2RGB)
plt.axis('off')
plt.imshow(img_RGB)
plt.show()

#accessing the ball and converting to white
ball=img[237:297,400:465]#coordinates
img[235:295,465:530]=ball


cv.imshow("Image with two heads",img)

cv.waitKey(0)
cv.destroyAllWindows()
