import cv2 as cv
import numpy as np

img = cv.imread('cat.png')

#------------------------------------------------------------------------------------------------
#TRANSLATION
def translate(img, x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0]) #shape[1] is for width shape[0] is for height
    return cv.warpAffine(img, transMat, dimensions)

# SHIFT--> -x = left, x = right, -y = up, y = down,

translated = translate(img, 100, 100)
#cv.imshow('Img translated', translated)

#----------------------------------------------------------------------------------------------
#ROTATION
def rotation(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint == None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions= (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotation(img, 90)
#cv.imshow('Rotation', rotated)

#------------------------------------------------------------------------------------------------
#RESIZE
resize = cv.resize( img, (500,500), interpolation=cv.INTER_LINEAR)
#cv.imshow('Resized img', resize)

#------------------------------------------------------------------------------------------------
#FLIPPING
flip = cv.flip(img, -1) # 0 = vertically --- 1 = horizontally
#cv.imshow('Flipped', flip)

#------------------------------------------------------------------------------------------------
#CROPPING
crop = img[200:250, 300:350]
cv.imshow('Cropped', crop)

cv.waitKey(0)