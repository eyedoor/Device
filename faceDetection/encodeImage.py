import base64
import cv2
import os
import requests
import json

image = open('bestImage/chosenImage.jpg', 'rb')
image_read = image.read()
image_64_encode = base64.encodestring(image_read)
os.remove('bestImage/chosenImage.jpg')
API_ENDPOINT = "https://joseph-frank.com/test/images"
API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NSwiand0VHlwZSI6ImRldmljZSIsImlhdCI6MTU1MzAzMjI0Nn0.6jozKQELi6z8LpXU1fgWDLjSIfwt5dTn5b0in_qPaGM"

headers = {
	'Content-Type':"application/x-www-form-urlencoded",
	'x-access-token':API_KEY
}
payload = {
	'image':image_64_encode
}


r = requests.post(url = API_ENDPOINT, headers=headers, data=payload)
r.raise_for_status()
print(r)
