import cv2 as cv
import numpy as np

img = cv.imread('cat.png')
cv.imshow('Cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#LAPLACIAN
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

#SOBEL ---> compute the gradient in two section x and y
sobelx = cv.Sobel(gray, cv.CV_64F, 1,0)
sobely = cv.Sobel(gray, cv.CV_64F, 0,1)
cv.imshow('SobelX', sobelx)
cv.imshow('SobelY', sobely)

#we also can combine these two
combined = cv.bitwise_or(sobelx, sobely)
cv.imshow('Combined', combined)



cv.waitKey(0)