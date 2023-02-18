import os
import utime
import random

uart = machine.UART(0, baudrate = 115200, timeout =1)
print ("UART Info: ", uart)

while (True):
    uart.write(str(random.uniform (-320, 452)))
    utime.sleep(2)
