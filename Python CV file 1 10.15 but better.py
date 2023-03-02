import cv2 as cv
import numpy as np
img1=cv.imread('a.jpg')#cv reads image a.jpg
img=cv.imread('a.jpg',0)#,0 makes image grayscaled or black or white
cv.imshow('Grey',img)#shows img greyscaled
cv.imshow('image',img1)#shows img1 as image
cv.waitKey(0)#waits until key is pressed to get rid of image.
cv.destroyAllWindows()#destroys image


