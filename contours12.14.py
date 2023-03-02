import cv2 as cv
import numpy as np

img=cv.imread("PIC1.png")

img_gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret,thresh=cv.threshold(img_gray,127,255,0)
#thresh is the image on which we are performing the operation on.
#RETR_TREE & CHAIN_APPROX_SIMPLE helps us by approximating the whole image and creating a smooth outlin
contours,hierarchy=cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
cnt=contours[4]
cv.drawContours(img,[cnt],0,(255,0,255),3)
#contour is perimeter of a unique shape, and hierarchy is the specified order of those perimeters. If you change the value of the perimeter, you specify the selected outline.


cv.imshow('Contours',img)
cv.waitKey(0)
cv.destroyAllWindows()
