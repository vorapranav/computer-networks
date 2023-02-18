import paho.mqtt.client as mqtt
import time


def on_message (client, userdata, message):
    dictMsg = str(message.payload.decode ("utf=8"))    
    print ("RECEIVED: ", dictMsg)
    
    
def on_connect (client, userdata, flags, rc):
    if (rc == 0):
        print (f"Connection Success")
    else:
        print (f"Connection failure {rc}")

def on_subscribe (client, userdata, mid, granted_qos):
    print ("Subscribed")

# Running main function to call other subroutines here
def main ():
    broker_address = "localhost"
    mqtt_client = mqtt.Client ("P1")
    
    mqtt_client.on_connect = on_connect
    mqtt_client.on_subscribe = on_subscribe

    mqtt_client.connect (broker_address, 1883)
    mqtt_client.subscribe ("readingserver")

    mqtt_client.loop_start ()
    mqtt_client.on_message = on_message

if __name__ == "__main__":
    main ()

