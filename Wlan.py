import network
import time

class Wlan():
    def __init__(self, ssid, password):
        self.__ssid = ssid
        self.__password = password

    def connect(self):
        wlan = network.WLAN(mode=network.WLAN.STA)
        wlan.connect(self.__ssid, auth=(network.WLAN.WPA2, self.__password))
        while not wlan.isconnected():
            time.sleep_ms(50)
        print("connected to WLAN")