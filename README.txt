


Instructions:

Terminal command to execute python scripts

Before running python scripts on RPi, make sure MQTT server is running. This is done through following command:
mosquitto_sub -h localhost -t “readingserver”
 
mqtt_subscribing.py script listens to the mqtt broker on localhost:1883 and fetches data from topic, “readingserver” and logs received data on the screen. To start this script, execute following command on the terminal (make sure you are in the same directory where your scripts are):
python3 mqtt_subscribing.py
 
uart_to_mqtt.py fetches data received on UART and decodes it in utf-8 format. The script then publishes the data over to the MQTT topic on localhost at port 1883. To run this script execute following command on the terminal (make sure you are in the same directory where your scripts are):
python3 uart_to_mqtt.py

