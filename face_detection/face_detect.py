import cv2 as cv

img = cv.imread('group2.jpg')
cv.imshow('Image', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#READING HAARCASCADE FILE
haar_cascade = cv.CascadeClassifier('haar_face.xml')

face_react = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=18)
print(f'Number of faces found: {len(face_react)}')

#DRAW A RECTANGLE AROUND THE FACES
for (x,y,w,h) in face_react:
    rectangle = cv.rectangle(img, (x,y), (x+h, y+w), (0,255,0), thickness=2)

cv.imshow('Detected Faces', img)

cv.waitKey(0)