import pycom
import ujson
from machine import UART

from TextSensorDataParser import TextSensorDataParser
from Wlan import Wlan
from ApiDataSender import ApiDataSender
import config

pycom.heartbeat(False)
uart = UART(1, baudrate=9600)
parser = TextSensorDataParser(config.sensor_mapping)
api_data_sender = ApiDataSender(config.endpoint)
print("Connecting to Wifi")
wlan = Wlan(config.wifi['user'], config.wifi['password'])
wlan.connect()

print('Program started, listening on serial 1')
buffer = ''
while True:
    incomming = uart.read(5)
    if incomming == None:
        continue
    buffer += incomming.decode('utf-8')
    if parser.is_buffer_parsable(buffer):
        sensors = parser.parse(buffer)
        print('Decoded sensors: {0}'.format(ujson.dumps(sensors)))
        try:
            api_data_sender.send(sensors)
        except Exception as e:
            print ('Http request failed, retrying..' + str(e))
        buffer = ''
