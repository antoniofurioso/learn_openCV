import cv2 as cv
import numpy as np

img = cv.imread('cat2.jpg')
cv.imshow('Cat', img)

blank = np.zeros(img.shape, dtype='uint8')

gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)

canny = cv.Canny(img, 125,175)
cv.imshow('Canny', canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank,contours,-1, (0,0,255), 1)
cv.imshow('Blank contour', blank)

cv.waitKey(0)