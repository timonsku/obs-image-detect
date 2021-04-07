from lobe import ImageModel
import os
import json
import numpy as np
import cv2
from PIL import Image
import time
import paho.mqtt.client as mqtt
import json

# set the path to the Tensorflow model exported from lobe.ai
model_dir = os.path.join(os.getcwd())

# this is the index of your OBS Virtual Camera. You can check this in any video conferencing app. The index is 0 based.
# or just go by trial and error, if you only have one cam this will be 0
cap = cv2.VideoCapture(2)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 960) #960
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 540) #540

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# connect to MQTT broker
client.connect("localhost", 1883, 60)

client.loop_start()

model = ImageModel.load(model_dir)

while True:
		ret, image_np = cap.read()
		image_rgb = cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB)
		im_pil = Image.fromarray(image_rgb)
		result = model.predict(im_pil)
		client.publish("birdcam/detections", json.dumps(result.__dict__), qos=0, retain=False)
		print(result.prediction)
		#comment the line below if you don't want the webcam preview
		cv2.imshow('object detection', image_np)
		time.sleep(1)
		if cv2.waitKey(25) & 0xFF == ord('q'):
			break

cap.release()
cv2.destroyAllWindows()
