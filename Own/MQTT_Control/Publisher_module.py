import mqtt
import time
import keyboard

MQTT_SERVER = "10.0.0.8"
MQTT_CLIENT = "Publisher"
port=1883

def sender():
    client = mqtt.create_client(MQTT_SERVER, MQTT_CLIENT, port)    
    client.on_publish = mqtt.on_publish 
    
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