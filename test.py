import time
import pycom
from machine import UART
import ure


from TextSensorDataParser import TextSensorDataParser

pycom.heartbeat(False)
uart = UART(1, baudrate=9600)
parser = TextSensorDataParser()
print('reading...x')

buffer = ''
while True:
    incomming = uart.read(5)
    if incomming == None:
        continue
    buffer += incomming.decode('utf-8')
    if parser.is_buffer_parsable(buffer):
        print(parser.parse(buffer))
        buffer = ''
