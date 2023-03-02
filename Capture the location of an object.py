import cv2 as cv
import numpy as np
cam=cv.VideoCapture(0)

lower_red=np.array([0,125,125])#lower_red upper_red specifies range of color, numbers are rgb goes from lower to upper red
upper_red=np.array([10,255,255])

while(True):
    ret,frame=cam.read()
    frame=cv.flip(frame,1)#in normal image, your right hand flips to be your left hand, so we make sure this is right way to face.

    w=frame.shape[1]#source image
    h=frame.shape[0]#0 for xaxis flip 1 yaxis flip -1 for both axis flip
    #smoothen the image
    image_smooth=cv.GaussianBlur(frame,(7,7),0)#7,7 specifies taking 49 total pixels and finding the average rgb value. 0 specifies gaussian blur
    #Define ROI
    mask=np.zeros_like(frame)#np.zeros creates black frame 
    mask[50:350,50:350]=[255,255,255]#50:350 is the area and puts white colored area over frame
    image_roi=cv.bitwise_and(image_smooth,mask)#if both inputs hight output high any input and likewise
    #creates box in video where we can put images that follow the person  we cant see the box only what we put into it
    
    cv.rectangle(frame,(50,50),(350,350),(0,0,255),2)
    cv.line(frame,(150,50),(150,350),(0,0,255),1)
    cv.line(frame,(150,50),(150,350),(0,0,255),1)
    cv.line(frame,(50,150),(350,150),(0,0,255),1)
    cv.line(frame,(50,250),(150,250),(0,0,255),1)

    #threshold the image for 43e color
    image_hsv=cv.cvtColor(image_smooth,cv.COLOR_BGR2HSV)#hue saturation lightness
    image_threshold=cv.inRange(image_hsv,lower_red, upper_red)

    #find contours
    contours,hierarchy=cv.findContours(image_threshold,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)#RETR_TREE is finding contour CHAIN_APPROX_NONE makes it sharper

    #find the index of largest contour
    if(len(contours)!=0):
        areas=[cv.contourArea(c)for c in contours]#for c in contour means itll give area of each contour to cv.contourArea(c) which is built-in
        max_index=np.argmax(areas)#finds largest area from given area
        cnt=contours[max_index]#finds specific contour with largest area
        x_bound,y_bound,w_bound,h_bound=cv.boundingRect(cnt)
        cv.rectangle(frame,(x_bound,y_bound),(x_bound+w_bound,y_bound+h_bound),(255,0,0),2)#highlights the actual contour
        #pointer on video
        M=cv.moments(cnt)#moments specifies finding the centroid of the object and following it
        if(M['m00']!=0):
            cx=int(M['m10']/M['m00'])
            cy=int(M['m10']/M['m00'])
            cv.circle(frame,(cx,cy),4,(0,255,0),-1)
            #cursor motion
            if cx in range(150,250):
                if cy<150:
                    print("Upper middle")
                elif cy>250:
                    print("lower middle")
                else:
                    print("Center")
            if cy in range(150,250):
                if cx<150:
                    print("left middle")
                elif cx>250:
                    print("right middle")
                else:
                    print("center")
    cv.imshow("Frame",frame)
    key=cv.waitKey(10)
    if key==27:
        break

cam.release()
cv.destroyAllWindows()
        
                
       
        
