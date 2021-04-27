import cv2 as cv

img= cv.imread('cat.png')
#cv.imshow('Cat', img)

#CONVERT IMAGE TO GRAY
gray_img= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray image', gray_img)

#BLUR
blur= cv.GaussianBlur(img, (9,9), cv.BORDER_DEFAULT)
#cv.imshow('BLUR', blur)

#EDGE CASCADE
canny = cv.Canny(img, 120, 200)
#cv.imshow('Edge evidence', canny)

#DILATING IMAGE
dilated = cv.dilate(img, (9,9), iterations=10)
#cv.imshow('Dilated', canny)

#ERODITING
erod= cv.erode(img, (9,9), iterations=10)
#cv.imshow('Erode', canny)

#RESIZE
resize = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
#cv.imshow('Resized', resize)

#CROPPING
crop = img[200:250, 100:1500]
cv.imshow('Cropped', crop)




cv.waitKey(0)