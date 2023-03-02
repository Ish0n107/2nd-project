import cv2 as cv
import numpy as np
img0=cv.imread('a.jpg')
img0greyscaled=cv.imread('a.jpg')
img=cv.imread('b.jpg')
imggreyscaled=cv.imread('b.jpg',0)
img3=cv.imread('c.jpg')
img3greyscaled=cv.imread('c.jpg',0)
cv.imshow('flower',img)# inside commas give name of pop up window when code is run
cv.imshow('black',imggreyscaled)
cv.imshow('image',img3)
cv.imshow('Grey',img3greyscaled)
cv.imshow('Family-Vin Diesal',img0)
cv.imshow('white',img0greyscaled)
cv.waitKey(0)
cv.destroyAllWindows()
