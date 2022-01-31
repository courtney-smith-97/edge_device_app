import paho.mqtt.client as mqtt


LOCAL_MQTT_HOST="172.16.24.2"
LOCAL_MQTT_PORT=32153
LOCAL_MQTT_TOPIC="image_topic"
REMOTE_MQTT_HOST="172.31.94.10"
REMOTE_MQTT_PORT=31857
REMOTE_MQTT_TOPIC="image_topic_remote"

def on_connect_local(client, userdata, flags, rc):
        print("connected to local broker with rc: " + str(rc))
        client.subscribe(LOCAL_MQTT_TOPIC)
        
def on_connect_remote(client, userdata, flags, rc):
        print("connected to remote broker with rc: " + str(rc))
        client.subscribe(REMOTE_MQTT_TOPIC)
    
def on_message(client,userdata, msg):
  try:
    print("message received: ",str(msg.payload.decode("utf-8")))
    # if we wanted to re-publish this message, something like this should work
    msg = msg.payload
    remote_mqttclient.publish(REMOTE_MQTT_TOPIC, payload=msg, qos=0, retain=False)
  except:
    print("Unexpected error:", sys.exc_info()[0])

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message

remote_mqttclient = mqtt.Client()
remote_mqttclient.on_connect = on_connect_remote
remote_mqttclient.connect(REMOTE_MQTT_HOST, REMOTE_MQTT_PORT, 60)
remote_mqttclient.onmessage = on_message

# go into a loop
remote_mqttclient.loop_start()
local_mqttclient.loop_forever()
