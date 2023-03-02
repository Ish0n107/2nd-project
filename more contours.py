import cv2 as cv
import numpy as np

img=cv.imread('PIC1.png')

img_gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret,thresh=cv.threshold(img_gray,127,255,0)


contours,hierarchy=cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
cnt=contours[6]
cv.drawContours(img,[cnt],0,(255,255,0),3)


M=cv.moments(cnt)#determines center of shape at given moment
print(M)

cx=int(M['m10']/M['m00'])#gives us centroid of shape
cy=int(M['m01']/M['m00'])#m10,m00,m01 moments points

print('centroid',(cx,cy))

area=cv.contourArea(cnt)

print("Area of the face is",area)#area of face


perimeter=cv.arcLength(cnt,True)
print("Perimeter of the face is",perimeter)#perimeter of closed shape

x,y,w,h=cv.boundingRect(cnt)
cv.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)#specified shape mentioned above

(x,y),radius=cv.minEnclosingCircle(cnt)#gives the minimum(smallest) circle that can surround the face


centre=(int(x),int(y))#specifications for circles
radius=int(radius)
cv.circle(img,centre,radius,(255,0,0),2)

cv.imshow('Contours',img)

cv.waitKey(0)
cv.destroyAllWindows()





