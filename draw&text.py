import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8') #uint8 is basically the images and we start with zeros AND show black image
#cv.imshow('Blank', blank)

#1. COLOR THE IMAGE
'''
blank[:] = 0,255,0 #in the [:] we can set the size and position of the color eg. [50:100, 100:300]-------- set image color with RGB
cv.imshow('Blank green', blank)
'''
#2. SHOW A RECTANGLE
cv.rectangle(blank, (100,100), (400,400), color=(0,0,255), thickness=3) #we set the image, point1 and point 2, color, thickness (also can we filled the rectangle with thinckness=cv.FILLED
#cv.imshow('rectangle', blank)

#3. DRAW A CIRCLE
cv.circle(blank, center=(250,250), radius=50, color=(255,0,0), thickness=-1)
#cv.imshow('Circle', blank)

#4. DRAW LINE
cv.line(blank, (100,100), (400, 400), (255,255,255), 4)
#cv.imshow('Line', blank)

#5. WRITE TEXT
cv.putText(blank, "I'm beautiful", (150,450), fontFace= cv.FONT_HERSHEY_DUPLEX, fontScale= 1.0, color=(255,0,0), thickness= 2)
#cv.imshow('Text', blank)

cv.imshow('Final form :)', blank)
cv.waitKey(0)