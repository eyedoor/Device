import base64
import cv2
import os
import requests
import json

image = open('bestImage/chosenImage.jpg', 'rb')
image_read = image.read()
image_64_encode = base64.encodestring(image_read)
os.remove('bestImage/chosenImage.jpg')
API_ENDPOINT = "https://joseph-frank.com/api/images"
API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjMsImp3dFR5cGUiOiJkZXZpY2UiLCJpYXQiOjE1NTY1NzY5MTB9.FGd2TNXQNT5qM9tXKkxA6G-PmTkK56sb0EkuI8RH770"

headers = {
	'Content-Type':"application/x-www-form-urlencoded",
	'x-access-token':API_KEY
}
payload = {
	'image':image_64_encode
}

print("Request sent")
r = requests.post(url = API_ENDPOINT, headers=headers, data=payload)
r.raise_for_status()
print(r)
