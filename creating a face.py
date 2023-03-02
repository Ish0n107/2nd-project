import cv2 as cv
import numpy as np

img=np.zeros((500,500,3),np.uint8)

cv.circle(img,(200,250),150,(255,255,255),5)

cv.line(img,(150,350),(250,350),(255,255,255),4)

cv.line(img,(150,345),(250,345),(0,0,255),8)

cv.line(img,(150,355),(250,355),(0,0,255),8)

cv.rectangle(img,(200,230),(205,270),(0,255,255),9)

cv.circle(img,(150,185),30,(255,255,255),35)

cv.line(img,(290,185),(210,200),(255,255,255),1)

cv.line(img,(210,200),(290,215),(255,255,255),1)

cv.line(img,(100,90),(200,120),(0,255,0),30)

cv.line(img,(200,120),(275,120),(0,255,0),20)

cv.imshow('IMAGE',img)
cv.waitKey(0)
cv.destroyAllWindows()
