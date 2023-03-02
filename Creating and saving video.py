import cv2 as cv
import numpy as np

cam=cv.VideoCapture(0)

#Define codec, used to make video smaller in size without affecting quality
fourcc=cv.VideoWriter_fourcc(*'XVID')#minimize video codec to XVID codec
output=cv.VideoWriter('Output1.avi',fourcc,20.0,(640,480))#output1.avi specifies nname of video output1 20.0 is frames per second, (640,480) video size 

while(cam.isOpened()):
    ret,frame=cam.read()
    if ret==True:
        cv.imshow('frame',frame)#authenticates camera works
        output.write(frame)#output.write means that puts frame into video

        if(cv.waitKey(1)==ord('q')):
           print('Saved Video')#keypress q will end and save video
           break
    else:
        print("Error in capturing video")
        break

#Release everything

cam.release()
output.release()
cv.destroyAllWindows()
