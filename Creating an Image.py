import cv2 as cv
import numpy as np


#creating black background image
img=np.zeros((500,500,3),np.uint8)#np.zeros(rows, columns, color channels(rgb),pixel size)

#creating purple line
cv.line(img,(20,20),(500,500),(255,0,255),8) #background, start pt, end pt, (B,G,R), width in pixels

#creating rectangle
cv.rectangle(img,(20,20),(400,400),(255,255,0),7)

#creating circle
cv.circle(img,(250,250),50,(255,0,255),5)

#writing text in image
font=cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'sky',(0,480),font,2,(255,0,0),2) #cv.putText(background img,text in string, left bottom corner, font, zoom, colour, size)

cv.imshow('IMAGE',img)
cv.waitKey(0)
cv.destroyAllWindows()
           
