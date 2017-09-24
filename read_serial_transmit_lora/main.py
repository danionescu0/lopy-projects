import pycom
import socket
from machine import UART
from network import LoRa

import config

pycom.heartbeat(False)
uart = UART(1, baudrate=config.serial_baud)
lora = LoRa(mode=LoRa.LORA, frequency=config.lora_frequency,  tx_power=14)
lora_socket = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
lora_socket.setblocking(False)

print('Program started, listening on Serial port 1, transmitting on LoRa')
while True:
    incomming = uart.read(5)
    if incomming == None:
        continue
    buffer = incomming.decode('utf-8')
    print("Sending:'{0}'".format(buffer))
    lora_socket.send(buffer)