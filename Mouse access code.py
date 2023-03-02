import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import pyautogui as pyt#mouse functionality

cam = cv.VideoCapture(0)
#defines range of colors for what can be shown to the camera/ anything between lower and upper yellow range is accepted as input, same for green

lower_yellow= np.array([20,100,100])#lower yellow-upper yellow is range for yellow
upper_yellow= np.array([40,255,255])

lower_green = np.array([50,100,100])#same as above
upper_green = np.array([80,255,255])

while(True):
    ret, frame = cam.read()
    frame = cv.flip(frame,1)#flips video so that the right hand is your right hand in the camera, left hand is left hand
    #usually opposites happen when you record.

    image_smooth = cv.GaussianBlur(frame,(7,7),0)
    #blurs image in inputs of 7 rows and 7 columns of pixels

    mask = np.zeros_like(frame)
    mask[50:350, 50:350] = [255,255,255]
    image_roi= cv.bitwise_and(image_smooth, mask)
    cv.rectangle(frame,(50,50),(350,350),(0,0,255),5)#makes rectangle
    
    cv.line(frame,(150,50),(150,350),(0,0,255),5)#makes lines inside rectangle
    cv.line(frame,(250,50),(250,350),(0,0,255),5)
    cv.line(frame,(50,150),(350,150),(0,0,255),5)
    cv.line(frame,(50,250),(350,250),(0,0,255),5)
    
    image_hsv=cv.cvtColor(image_roi,cv.COLOR_BGR2HSV)#image_roi is specified(the rectangles) cv.color_BGRHSV is to polish the image(hue saturation, value)
    

    image_threshold= cv.inRange(image_hsv, lower_yellow, upper_yellow )
    #in range in image hsv specifically from lower yellow to upper yellow
    contours, heirarchy = cv.findContours(image_threshold,\
    #finds borders, outlines for specific yellow things                                                  cv.RETR_TREE,\
                                                       cv.CHAIN_APPROX_NONE)
    if(len(contours)!=0):
        areas=[cv.contourArea(c)for c in contours]#takes coordinates of all contours, calculates the area of the specific outlines, then stores in list
        max_index=np.argmax(areas)#takes the highest coordinate for each contour point, store maxindex
        #e.g contour coordinate is 30, stores 3
        cnt=contours[max_index]#makes contour of max index areas
##        x_bound, y_bound, w_bound, h_bound=cv.boundingRect(cnt)
##        cv.rectangle(frame, (x_bound,y_bound),(x_bound + w_bound,y_bound + h_bound),(255,0,0))

        M =cv.moments(cnt)
        if(M['m00']!=0):
            cx = int(M['m10']/M['m00'])#takes center coordinate
            cy = int(M['m01']/M['m00'])
            cv.circle(frame,(cx,cy),4,(0,255,0),-1)#circle defines center coordinates

            if cx< 150:#if the mouse moves to the right or to the left, dist x moves the green mouse that much
                dist_x =-20#dist x and y are center coordinates
            elif cx > 250:
                dist_x = 20
            else:
                dist_x = 0
            if cy< 150:
                dist_y =-20
            elif cy > 250:
                dist_y = 20
            else:
                dist_y = 0
        #using moments(camera freeze frames) and applying formula to find the center of the mouse
                
            pyt.moveRel(dist_x,dist_y,duration = 0.05)#duration=0.05 seconds
    image_threshold_green = cv.inRange(image_hsv,lower_green,upper_green)
    contour_green, heirarchy = cv.findContours(image_threshold_green,

                                                   
           #if you hover mouse over button, then put green object in camera, then itll clikc the button                                                         cv.RETR_TREE,\
                                                                    cv.CHAIN_APPROX_NONE)
    if(len(contour_green)!=0):
        pyt.click()
        cv.waitKey(300)#every 300 millisecond itll click after green object shows
        
    cv.imshow('Frame',frame)
    key = cv.waitKey(1)
    if key == 27:
        break

cam.release()
cv.destroyAllWindows()
        
        
        
