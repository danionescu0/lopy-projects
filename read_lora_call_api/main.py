import pycom
import ujson
import socket
from network import LoRa

from TextSensorDataParser import TextSensorDataParser
from Wlan import Wlan
from ApiDataSender import ApiDataSender
import config

pycom.heartbeat(False)
parser = TextSensorDataParser(config.sensor_mapping)
api_data_sender = ApiDataSender(config.endpoint)
print("Connecting to Wifi")
wlan = Wlan(config.wifi['user'], config.wifi['password'])
wlan.connect()
lora = LoRa(mode=LoRa.LORA, frequency=config.lora_frequency,  tx_power=14)
lora_socket = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
lora_socket.setblocking(False)

print('Program started, listening on LoRa frequency {0}'.format(config.lora_frequency))
buffer = ''

while True:
    incomming = lora_socket.recv(5)
    if incomming == None:
        continue
    buffer += incomming.decode('utf-8')
    if not parser.is_buffer_parsable(buffer):
        continue
    sensors = parser.parse(buffer)
    print('Decoded sensors: {0}'.format(ujson.dumps(sensors)))
    try:
        api_data_sender.send(sensors)
    except Exception as e:
        print ('Http request failed, retrying..' + str(e))
    buffer = ''
