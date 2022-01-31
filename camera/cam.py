# this is from https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
import numpy as np
import cv2 as cv
import paho.mqtt.client as mqtt
# the index depends on your camera setup and which one is your USB camera.
LOCAL_MQTT_HOST="172.16.24.2"
LOCAL_MQTT_PORT=31044
LOCAL_MQTT_TOPIC="image_topic"

def on_connect_local(client, userdata, flags, rc):
        print("connected to local broker with rc: " + str(rc))

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv.VideoCapture(0)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        rc,png = cv.imencode('.png', gray)
        msg = png.tobytes()

    #publish the message
        local_mqttclient.publish(LOCAL_MQTT_TOPIC, msg)
        print('msg received')
    
    # Display the resulting frame
    cv.imshow('frame',gray)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
