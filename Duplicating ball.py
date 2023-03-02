import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img=cv.imread('hazard10.jpg')
cv.imshow('IMAGE',img)

#finding region of interest
#img_RGB=cv.cvtColor(img,cv.COLOR_BGR2RGB)
#plt.axis('off')
#plt.imshow(img_RGB)
#plt.show()

#accessing the ball and converting to white
#ball=img[235:295,465:530]#coordinates
#ball=([255,255,255])
#img[235:295,465:530]=ball#overlaps on ball

#Duplicating the ball
ball=img[235:295,465:530]#actual ball region and then copy pasted it
img[235:295,555:620]=ball#checks/authenticates that ball overlaps; pastes other ball


cv.imshow('IMAGE WITH TWO BALLS',img)#basically copy pasted what was taken out of the image, which was ball, and pasted it different coordinates




cv.waitKey(0)
cv.destroyAllWindows()
