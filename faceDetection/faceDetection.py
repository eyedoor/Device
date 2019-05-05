import numpy as np
import cv2
import os
import time

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height

def variance_of_laplacian(image):
    return cv2.Laplacian(image, cv2.CV_64F).var()

def chooseBestImage(imgArray):
    curBest = 0
    for img in imgArray:
        var = variance_of_laplacian(img)
        if var > curBest:
            curBest = var
            bestImage = img
    return bestImage


time_end = time.time() + 10

while time.time() < time_end:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,     
        minSize=(20, 20)
    )
    if len(faces) > 0:
        (x,y,w,h) = faces[0]
        roi_gray = gray[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray);
        if len(eyes) > 0:
            if not os.path.isfile('person1.jpg'):
                nameImage = 'person1'
            elif not os.path.isfile('person2.jpg'):
                nameImage = 'person2'
            else:
                nameImage = 'person3'
            cv2.imwrite(nameImage + '.jpg', img)
        # after three images are taken save to array
        if os.path.isfile('person3.jpg'):
            imgArray = [cv2.imread('person1.jpg'),
                        cv2.imread('person2.jpg'),
                        cv2.imread('person3.jpg')]
            cv2.imwrite('bestImage/chosenImage.jpg',chooseBestImage(imgArray))
            os.remove('person1.jpg')
            os.remove('person2.jpg')
            os.remove('person3.jpg')
            cap.release()
            cv2.destroyAllWindows()
            os.system('python3 encodeImage.py')
            break
    #k = cv2.waitKey(30) & 0xff
    #if k == 27: # press 'ESC' to quit
cap.release()
cv2.destroyAllWindows()
print("Finished Face detection")
