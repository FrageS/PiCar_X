import paho.mqtt.client as mqtt #import the client1
import time

MQTT_SERVER = "10.0.0.8"
speed = 0
steer = 0

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc==0:        
        client.connected_flag=True 
        print("connected OK Returned code=",rc)
        client.subscribe("picar/speed")
        client.subscribe("picar/steer")
        print("Subscribed to topics")
    else:
        print("Bad connection Returned code= ",rc)

def on_message(client, userdata, message):
    global speed, steer
      
    if(message.topic == "picar/speed"):
        speed = int(message.payload)/100
    elif(message.topic == "picar/steer"):        
        steer = int(message.payload)

def client():     
    client = mqtt.Client("Receiver")
    mqtt.Client.connected_flag=False
    client.on_connect = on_connect
    client.on_message=on_message    
    client.connect(MQTT_SERVER)    
    client.loop_start() #start the loop
    while not client.connected_flag:
        time.sleep(0.1)

    i = 0
    while True:  
        i += 1      
        time.sleep(1)        
        print("Speed: ", speed, " / ", "Steering: ", steer)      
    
    client.loop_stop() #stop the loop


if __name__ == "__main__":
    try:
        client()
    except:     
        print('Program cancelled')