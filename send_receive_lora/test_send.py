from network import LoRa
import socket
import time


lora = LoRa(mode=LoRa.LORA, frequency=863000000,  tx_power=14)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)
print("Started receiving")

i = 0
while True:
    to_send = str(i)
    i += 1
    s.send(to_send)
    print("Sending:{0}".format(to_send))
    time.sleep(2)
