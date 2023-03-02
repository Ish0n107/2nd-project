import cv2 as cv
import numpy as np
img=cv.imread('a.jpg')
img1=cv.imread('a.jpg',0)
cv.imshow('no senor',img)
cv.imshow('the purge is legal for 12 hrs',img1)
cv.waitKey(2000)#waits 2 seconds before killing program
cv.destroyAllWindows()
