import paho.mqtt.client as mqtt
import time

MQTT_SERVER = "10.0.0.8"
MQTT_PATH = "test_channel"

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True #set flag
        print("connected OK Returned code=",rc)
        #client.subscribe(topic)
    else:
        print("Bad connection Returned code= ",rc)

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    # more callbacks, etc

def client():
    mqtt.Client.connected_flag=False
    client = mqtt.Client('Publisher_1')
    client.on_connect = on_connect
    client.on_message = on_message
 
    client.connect(MQTT_SERVER, 1883, 60)

    client.loop_start()
    time.sleep(1)
    while True:
        print('Wait')
        time.sleep(5)
    client.loop_stop()

if __name__ == "__main__":
    try:
        client()
    except: 
        #client.loop_stop()     
        print('Program cancelled')