#!/usr/bin/python3
import sys
sys.path.append(r'/opt/ezblock')
from ezblock import __reset_mcu__
import time
__reset_mcu__()
time.sleep(0.01)
import mqtt
import time

from picarx import dir_servo_angle_calibration
from picarx import forward
from ezblock import delay
from picarx import backward
from picarx import set_dir_servo_angle
from picarx import stop


MQTT_SERVER = "10.0.0.8"
MQTT_CLIENT = "Receiver"
port=1883
speed = 0
steer = 0
stop = 0

def on_message(client, userdata, message):
    global speed, steer, stop
      
    if(message.topic == "picar/speed"):
        speed = int(message.payload)/100
    elif(message.topic == "picar/steer"):        
        steer = int(message.payload)
    elif(message.topic == "picar/stop"):
        stop = 1
        
def client():     
    client = mqtt.create_client(MQTT_SERVER, MQTT_CLIENT, port)    
    client.on_message=on_message    
    
    while True:
        
        forward(speed)
        set_dir_servo_angle((steer)) 
        if(stop == 1):
            break             
    
    forward(0)
    set_dir_servo_angle(0)
    client.loop_stop() #stop the loop


if __name__ == "__main__":
    try:
        client()
    except:  
        forward(0)  
        set_dir_servo_angle((0)) 
        print('Program cancelled')