###### im_upload.py
import paho.mqtt.client as mqtt
import sys
import os
import boto3
import logging
from botocore.exceptions import ClientError
from datetime import datetime
LOCAL_MQTT_HOST="54.158.175.80"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="usbcam/images"

def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def on_connect_local(client, userdata, flags, rc):
        print("connected to local broker with rc: " + str(rc))
        client.subscribe(LOCAL_MQTT_TOPIC)
    
def on_message(client,userdata, msg):
  try:
    print("message received")
    # if we wanted to re-publish this message, something like this should work
    msg = msg.payload
    filename = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")+".png" 
    f = open(filename,'wb')
    f.write(msg)
    f.close()
    upload_file(filename, "hw3-image-bucket", filename)
    os.remove(filename)
    print('success')
  except:
    print("Unexpected error:", sys.exc_info()[0])

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message
# go into a loop
local_mqttclient.loop_forever()
