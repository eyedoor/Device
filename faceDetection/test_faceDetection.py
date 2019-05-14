import unittest
import cv2
#import numpy as np
from faceDetection_functions import variance_of_laplacian
from faceDetection_functions import chooseBestImage
from faceDetection_functions import sendImageToServer

class TestFaceDetection(unittest.TestCase):
    def test_area(self):
        # Ensure that laplacian function returns expected value
        img = cv2.imread('testImages/person1.jpg')
        self.assertEqual(variance_of_laplacian(img), 228.50595162445708)

class TestImageSelection(unittest.TestCase):
    def test_area(self):
        # Ensures that the least blurry image is selected
        # And ensures that 3 images are taken
        imgArray = [cv2.imread('testImages/person1.jpg'),
                    cv2.imread('testImages/person2.jpg'),
                    cv2.imread('testImages/person3.jpg')]
        self.assertIs(chooseBestImage(imgArray), imgArray[0])

class TestSendImageToServer(unittest.TestCase):
    def test_area(self):
        # Ensures that the image was properly sent to the server
        # Should return a 200 status code
        image = open('testImages/person1.jpg')
        self.assertEqual(sendImageToServer(image),201)

