import cv2 as cv

img = cv.imread('cat.png')
cv.imshow('Cat', img)

#We are going to split the image color blue, gree, red
b,g,r = cv.split(img)
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red',r)

'''With this split we obtained a grayscale of blue, green and red. But if we can try to merge these images
we can see that opencv turn the images to the original image'''
#LET'S SEE IT

merged= cv.merge([b,g,r]) #we have to pass a list
cv.imshow('Merged Images', merged)

cv.waitKey(0)