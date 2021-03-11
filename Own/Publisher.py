import paho.mqtt.client as mqtt
import time
import keyboard

MQTT_SERVER = "10.0.0.8"
port=1883

def on_publish(client,userdata,result):           
    print("data published \n")
    pass

def sender():
    client = mqtt.Client("Publisher")
    client.on_publish = on_publish 
    client.connect(MQTT_SERVER,port)
    
    while True:                              
        ret= client.publish("picar/speed","1")         
        time.sleep(4) 

if __name__ == "__main__":
    try:
        sender()
    except:     
        print('Program cancelled')