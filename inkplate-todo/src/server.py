"""
Web server for controlling the Inkplate remotely
"""

import network

from config import config

# try:
#     import usocket as socket
# except ImportError:
#     import socket

class Server:
    def __init__(self) -> None:
        ssid = config["network"]["ssid"]
        password = config["network"]["password"]
        print(f"Connecting to WiFi\n  SSID={ssid}\n  Password={password}")

        self.wlan = network.WLAN(network.STA_IF)

        if not self.wlan.isconnected():
            self.wlan.active(True)
            self.wlan.config(dhcp_hostname='inkplate-todo')
            self.wlan.connect(ssid, password)
            while not self.wlan.isconnected():
                pass

        ip, subnet, gateway, dns = self.wlan.ifconfig()
        print(f"Connected to WiFi\n  IP={ip}\n  Subnet={subnet}\n  Gateway={gateway}\n  DNS={dns}")
