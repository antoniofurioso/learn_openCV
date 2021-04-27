import cv2 as cv

img = cv.imread('cat.png')
cv.imshow('Cat', img)
#-----------------------------------------------
#BGR to Gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#-----------------------------------------------
#HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

#-----------------------------------------------
#LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

#-----------------------------------------------
#BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

cv.waitKey(0)

#OPENCV can't convert grayscale directly to HSV or LAB image