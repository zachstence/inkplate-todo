from inkplate6_COLOR import Inkplate

import network
import json
import os

inkplate = Inkplate()

def connect():
    print(os.listdir())

    with open("secret/network.json", "r") as config:
        parsed = json.load(config)
        ssid = parsed["ssid"]
        password = parsed["password"]
    
    print(f"Read network config {ssid} / {password}")

    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("connecting to network...")
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass
    print("network config:", sta_if.ifconfig())

def http_get(url):
    import socket

    res = ""
    _, _, host, path = url.split("/", 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes("GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n" % (path, host), "utf8"))
    while True:
        data = s.recv(100)
        if data:
            res += str(data, "utf8")
        else:
            break
    s.close()

    return res

if __name__ == "__main__":
    connect()
    response = http_get("http://micropython.org/ks/test.html")

    # Initialise our Inkplate object
    display = Inkplate()
    display.begin()

    # Print response in lines
    cnt = 0
    for x in response.split("\n"):
        display.printText(
            10, 10 + cnt, x.upper()
        )  # Default font has only upper case letters
        cnt += 10

    # Display image from buffer
    display.display()
