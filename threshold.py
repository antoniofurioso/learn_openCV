import cv2 as cv
'''THRESHOLDING IS THE BINARIZATION OF THE IMAGE
(transform the image in a binary image)'''

img = cv.imread('cat.png')
cv.imshow('Cat', img)

gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#SIMPLE THRESHOLDING ------> specify the value
threshold, thresh = cv.threshold(gray, 150, 255,cv.THRESH_BINARY) #modify 150 to see the difference, near 255 become black image
cv.imshow('Threshold', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255,cv.THRESH_BINARY_INV) #modify 150 to see the difference, near 255 become white image
cv.imshow('Threshold', thresh_inv)

#ADAPTIVE THRESHOLDING
adaptive = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, #try cv.ADAPTIVE_THRESH_GAUSSIAN_C
                                cv.THRESH_BINARY,11, 3) #try to change the last 2 values to set the minimun and see the difference
cv.imshow('Adaptive', adaptive)


cv.waitKey(0)