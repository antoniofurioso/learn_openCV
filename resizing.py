import cv2 as cv

#RESIZE VIDEO, IMAGES, LIVE VIDEO
def resizeFrame(frame, scale=0.70):
    width = int(frame.shape[1] * scale) #shape[1] is for width
    height = int(frame.shape[0] * scale) #shape [0] is for height

    dimensions= (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
'''
#RESIZE PER VIDEO LIVE
def resizelive(width, height):
    capture.set(3, width)
    capture.set(4,height)
'''

capture = cv.VideoCapture('dog.mp4')
while True:
    isTrue, frame = capture.read()

    resize= resizeFrame(frame, scale=0.5) #to resize video

    cv.imshow('Video', frame) #normal video
    cv.imshow('Video Resized', resize) #resized video

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
