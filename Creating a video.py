import cv2 as cv
import numpy as np

cam=cv.VideoCapture(0)#takes in-built camera(0) and calls it

while(True):
    #Capture frame-by-frame
    ret,frame=cam.read()#frame is frame of image. A split second shot. ret is boolean value(true,false) ret authenticates whether camera when program is running itll take photo.

    #display resulting frame
    cv.imshow('frame',frame)
    key=cv.waitKey(10)#waits every 10 milliseconds for keypress
    if key==27: #if you enter 27, program stops
        break

#releasing capture
cam.release()#release and take photo and makes sure it comes back to normal position
cv.destroyAllWindows()
