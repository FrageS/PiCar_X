import paho.mqtt.client as mqtt
import time

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc==0:        
        client.connected_flag=True 
        print("connected OK Returned code=",rc)
        client.subscribe("picar/speed")
        client.subscribe("picar/steer")
        client.subscribe("picar/stop")
        print("Subscribed to topics")
    else:
        print("Bad connection Returned code= ",rc)

def on_publish(client,userdata,result):           
    print("data published")
    pass

def create_client(broker, clientname, port):
    client = mqtt.Client(clientname)    
    client.connect(broker, port)
    mqtt.Client.connected_flag=False 
    client.on_connect = on_connect
    client.loop_start()
    while not client.connected_flag:
        time.sleep(0.1)

    return client
    