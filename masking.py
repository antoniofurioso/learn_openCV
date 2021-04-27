import cv2 as cv
import  numpy as np

img = cv.imread('cat2.jpg')
cv.imshow('Cat', img)
'''Masking is basically focus on the some part of the image'''

blank = np.zeros(img.shape[:2], dtype='uint8') #the mask have to have the same dimensions of the image
cv.imshow('Blank', blank)

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('Mask', mask)

masked_img= cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked image', masked_img)


cv.waitKey(0)