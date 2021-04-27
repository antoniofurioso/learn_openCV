import cv2 as cv
import numpy as np

haar_cascade = cv.CascadeClassifier(r'C:\Users\anton\Desktop\LEARNOPENCV\Face_Detection\haar_face.xml')

people = ['ben_afflek', 'elton_john', 'jerry_seinfeld', 'madonna', 'mindy_kaling']
#features = np.load('features.npy')
#labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread(r'C:\Users\anton\Desktop\LEARNOPENCV\Face_Recognition\val\ben_afflek\httpafilesbiographycomimageuploadcfillcssrgbdprgfacehqwMTENDgMDUODczNDcNTcjpg.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Person', gray)

#detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in faces_rect:
    faces_roi= gray[y:y+h, x:x+w]

    #now we are going to predict
    label, confidence = face_recognizer.predict(faces_roi)
    #print(f'label = {label} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_ITALIC, 1.0, (0, 255, 255), thickness=2)
    cv.putText(img, str(confidence), (20, 50), cv.FONT_ITALIC, 1.0, (0, 255, 255), thickness=2)
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow('Detected', img)

cv.waitKey(0)