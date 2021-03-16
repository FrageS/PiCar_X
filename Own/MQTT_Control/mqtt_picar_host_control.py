import paho.mqtt.client as mqtt
import time
import keyboard

MQTT_SERVER = "10.0.0.8"
MQTT_CLIENT = "Publisher"
port=1883

def on_publish(client,userdata,result):           
    print("data published")
    pass

def sender():
    speed = 0
    old_speed = 0
    steer = 0
    old_steer = 0
    client = mqtt.Client("Publisher")
    client.on_publish = on_publish 
    client.connect(MQTT_SERVER,port)
    
    while True: 
        old_speed = speed
        old_steer = steer

        # Longitudinal control
        if keyboard.is_pressed('w'):
            speed += 1                     
            time.sleep(0.15) 
        elif keyboard.is_pressed('s'):
            speed -= 1                     
            time.sleep(0.15) 
        elif keyboard.is_pressed('space'):
            speed = 0
            time.sleep(0.15)
        else:
            speed = old_speed
        
        if(old_speed != speed):
            ret= client.publish("picar/speed",speed)

        # Lateral control
        if keyboard.is_pressed('a') and speed != 0:
            steer -= 2
            time.sleep(0.15)
        if keyboard.is_pressed('d') and speed != 0:
            steer += 2
            time.sleep(0.15)
        
        if (steer > 35):
            steer = 35
        elif (steer < -35):
            steer = -35

        if(old_steer != steer):
            ret = client.publish("picar/steer",steer)

        if keyboard.is_pressed('q'):
            speed = 0
            steer = 0
            ret = client.publish("picar/speed", speed)
            ret = client.publish("picar/steer", steer)
            time.sleep(0.15)
            exit()
        
       


if __name__ == "__main__":
    try:
        sender()
    except:     
        print('Program cancelled')