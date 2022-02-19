import requests
import json
import cv2


url = "http://104.197.246.24:5000/face"
headers = {"content-type": "image/jpg"}

# encode image
image = cv2.imread('images/baggage_claim.jpg')
_, img_encoded = cv2.imencode(".jpg", image)

# send HTTP request to the server
response = requests.post(url, data=img_encoded.tostring(), headers=headers)
predictions = response.json()
print(predictions)
