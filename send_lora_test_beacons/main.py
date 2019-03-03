import uos
import socket
import time

from network import LoRa


lora = LoRa(mode=LoRa.LORA, frequency=863000000,  tx_power=14)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)
print("Started sending")

while True:
    number = uos.urandom(1)[0]
    to_send = str(number)
    s.send(to_send)
    print("Sending:{0}".format(to_send))
    time.sleep(2)
