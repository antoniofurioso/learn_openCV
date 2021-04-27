import cv2 as cv
import numpy as np
'''Bitwise operator are 4 and these execute binary operation'''

blank = np.zeros((400,400), dtype='uint8')
rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

#1. BITWISE "AND"
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('AND', bitwise_and) #return the intersection

#2. BITWISE "OR"
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('OR', bitwise_or) #put together the images

#3. BITWISE "XOR"
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('XOR', bitwise_xor) #delete the intersection

#4. BITWISE "NOT"
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('NOT', bitwise_not) #substantially this split the color of the pass image
                              #Not show the image but the contour

cv.waitKey(0)