import network

from config import config

# Connect to WiFi
ssid = config["network"]["ssid"]
password = config["network"]["password"]
print(f"Connecting to WiFi\n  SSID={ssid}\n  Password={password}")

wlan = network.WLAN(network.STA_IF)

if not wlan.isconnected():
    wlan.active(True)
    wlan.config(dhcp_hostname='inkplate-todo')
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        pass

ip, subnet, gateway, dns = wlan.ifconfig()
print(f"Connected to WiFi\n  IP={ip}\n  Subnet={subnet}\n  Gateway={gateway}\n  DNS={dns}")
