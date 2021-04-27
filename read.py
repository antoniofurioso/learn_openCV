import cv2 as cv

#READING IMAGES
img = cv.imread('cat.png')
cv.imshow('Cat', img)
cv.waitKey(0)


#READING VIDEOS
capture = cv.VideoCapture('dog.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'): #INTERRUPT VIDEO
        break

capture.release()
cv.destroyAllWindows()


