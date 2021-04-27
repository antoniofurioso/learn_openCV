import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
'''Histogram allow you to visualize the pixel intensity of the distribution
of the color'''

img = cv.imread('cat2.jpg')
cv.imshow('Cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray image', gray)

blank = np.zeros(img.shape[:2], dtype='uint8')
circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
mask = cv.bitwise_and(img,img,mask=circle)
cv.imshow('Mask', mask)


#GRAY HISTOGRAM
'''
gray_hist= cv.calcHist([gray], [0], mask,[256],[0,256])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()
'''

#COLOR HISTOGRAM
colors= ('b', 'g', 'r')
plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color= col)
    plt.xlim([0,256])

plt.show()
cv.waitKey(0)