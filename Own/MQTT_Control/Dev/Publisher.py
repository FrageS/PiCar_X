import paho.mqtt.client as mqtt
import time
import keyboard

MQTT_SERVER = "10.0.0.8"
port=1883

def on_publish(client,userdata,result):           
    print("data published")
    pass

def sender():
    client = mqtt.Client("Publisher")
    client.on_publish = on_publish 
    client.connect(MQTT_SERVER,port)
    i=0
    while True:
        i += 1                              
        client.publish("picar/speed",i)         
        client.publish("picar/steer",i)         
        time.sleep(4) 

if __name__ == "__main__":
    try:
        sender()
    except:     
        print('Program cancelled')