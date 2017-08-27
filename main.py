import pycom
from machine import UART


from TextSensorDataParser import TextSensorDataParser
from Wlan import Wlan
from ApiDataSender import ApiDataSender
import config

pycom.heartbeat(False)
uart = UART(1, baudrate=9600)
parser = TextSensorDataParser()
api_data_sender = ApiDataSender(config.endpoint)
wlan = Wlan(config.wifi['user'], config.wifi['password'])
wlan.connect()

print("Program started, listening on serial 1")
buffer = ''
while True:
    incomming = uart.read(5)
    if incomming == None:
        continue
    buffer += incomming.decode('utf-8')
    if parser.is_buffer_parsable(buffer):
        sensors = parser.parse(buffer)
        print(sensors)
        api_data_sender.send(sensors)
        buffer = ''
