import mqtt
import time

MQTT_SERVER = "10.0.0.8"
MQTT_CLIENT = "Receiver"
port=1883
speed = 0
steer = 0

def on_message(client, userdata, message):
    global speed, steer
      
    if(message.topic == "picar/speed"):
        speed = int(message.payload)/100
    elif(message.topic == "picar/steer"):        
        steer = int(message.payload)

def client():     
    client = mqtt.create_client(MQTT_SERVER, MQTT_CLIENT, port)       
    client.on_message=on_message 

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