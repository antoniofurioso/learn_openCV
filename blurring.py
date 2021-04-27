import cv2 as cv

img = cv.imread('cat.png')
cv.imshow('Cat', img)
#-----------------------------------------------
#AVERAGE METHOD
average = cv.blur(img, (3,3))
cv.imshow('Average', average)

#-----------------------------------------------
#GAUSSIAN
'''This method give a certain wight for each windows and then give it back
the average of the product of the weights. With this method we are less blur
compare to average but it is more natural'''

gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian', gauss)

#----------------------------------------------
#MEDIAN BLUR
'''It's the same of average but instead of find the average, it find the median of the kernel.
This reduce more noise respect the other methods'''

median = cv.medianBlur(img, 7) #we put only one number because opencv assumes that this is a kernel
cv.imshow('Median Blur', median)

#-----------------------------------------------
#BILATERAL BLUR
'''This method is the best method because Bilateral Blur consider the edges of the image'''
bilateral = cv.bilateralFilter(img, 10, 30, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)