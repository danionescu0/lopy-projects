from network import LoRa
import socket
import time
import pycom

pycom.heartbeat(False)
lora = LoRa(mode=LoRa.LORA, frequency=863000000,  tx_power=14)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)
print("Started receiving")

while True:
    text = s.recv(64)
    if text != b'':
        print("received {0}, sending Pong".format(text))
        pycom.rgbled(0x007f00)
        time.sleep(0.5)
        pycom.rgbled(0x000000)
        s.send('Pong')
    time.sleep(5)
