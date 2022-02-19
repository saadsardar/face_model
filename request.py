import requests
import json
import cv2


url = "http://35.232.11.230:5000/face"
headers = {"content-type": "image/jpg"}

# encode image
image = cv2.imread('Images/Atif.jpg')
_, img_encoded = cv2.imencode(".jpg", image)
# print(img_encoded.tostring())

# send HTTP request to the server
print("sending")
response = requests.post(url, data=img_encoded.tostring(), headers=headers)
print(response)
predictions = response.json()
print(predictions)
