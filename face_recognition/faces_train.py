import os
import cv2 as cv
import numpy as np

'''We are going to build a model with opencv'''

people = ['ben_afflek', 'elton_john', 'jerry_seinfeld', 'madonna', 'mindy_kaling']

DIR = r'C:\Users\anton\Desktop\LEARNOPENCV\Face_Recognition\train'

haar_cascade = cv.CascadeClassifier(r'C:\Users\anton\Desktop\LEARNOPENCV\Face_Detection\haar_face.xml')

features=[]
labels=[] #create a label for each images

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            #find the faces in images
            face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors = 4)

            for (x,y,w,h) in face_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()

#print(f'Length of the features = {len(features)}')
#print(f'Length of the labels = {len(labels)}')

print('Training done-------------------')

#convert features and labels list in numpy array
features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

#Train the Recognizer on the features list and the labels list
face_recognizer.train(features, labels)

#save the models
face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)