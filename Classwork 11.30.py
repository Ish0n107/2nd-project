import cv2 as cv
import numpy as np

cam=cv.VideoCapture(0)

while(True):
    ret,frame=cam.read()#ret is boolean frames for whether frame access the camera
    frame=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)#greyscaled the image
    edges=cv.Canny(frame,1,100)#any pixel of frame with value greater than equal to 70, will become white.
    #anything over 200 is black
    cv.imshow('Edges',edges)

    key=cv.waitKey(20)
    if key==27:
        break
cam.release()
cv.destroyAllWindows()
