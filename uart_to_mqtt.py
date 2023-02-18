import serial
from time import sleep
import random
import paho.mqtt.client as paho

# publish message to broker on localhost at port 1883
broker = "localhost"
port = 1883

# the on_publish function
def on_publish(client, userdata, result):
    print("data published \n")
    pass

# set up paho publish client
client1 = paho.Client("PublishingClient")
client1.on_publish = on_publish
client1.connect(broker, port)

ser = serial.Serial (
    port = '/dev/ttyS0',
    baudrate = 115200,
    timeout=1)



while (True):
    x = ser.readline ()
    data = x.decode ("utf-8")
    
    if (data != ""):
        # publish to the selected MQTT server
        ref = client1.publish("readingserver", str(data))
        print("SENT: " + str(data))

    sleep(0.5)
