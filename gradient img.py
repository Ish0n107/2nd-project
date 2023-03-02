import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img=cv.imread('gradient.png',0)
cv.imshow('original image',img)#127 value is magnitude of pixel. magnitude meaning the color it can generate.
ret,thresh1=cv.threshold(img,127,255,cv.THRESH_BINARY)#if pixel number is above 127, becomes white, else, becomes black. 127 is threshold. 255 in rgb is white
ret,thresh2=cv.threshold(img,127,255,cv.THRESH_BINARY_INV)#same as above but opposite. If value is above 127, becomes black, else, white
ret,thresh3=cv.threshold(img,127,255,cv.THRESH_TRUNC)#if value below 127, pixel color goes from black to grey, but if above 127, it's white 
ret,thresh4=cv.threshold(img,127,255,cv.THRESH_TOZERO)#if value below 127, pixel color is black. else, color of pixel goes from grey to white
ret,thresh5=cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)# opposite

titles=['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images=[img,thresh1,thresh2,thresh3,thresh4,thresh5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')#2,3 is rows and columns. i+1 image specification
    plt.title(titles[i])#gives image title
    plt.xticks([]),plt.yticks([])#plotting the image x and y
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
