"""
Web server for controlling the Inkplate remotely
"""

import network
try:
    import usocket as socket
except ImportError:
    import socket

from config import config

CONTENT = b"""\
HTTP/1.0 200 OK

Hello #%d from MicroPython!
"""

class Server:
    socket: socket.socket
    
    def __init__(self) -> None:
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

        self.socket = socket.socket()
        # Binding to all interfaces - server will be accessible to other hosts!
        ai = socket.getaddrinfo("0.0.0.0", 8080)
        print("Bind address info:", ai)
        addr = ai[0][-1]

        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(addr)
        self.socket.listen(5)
        print("Listening, connect your browser to http://<this_host>:8080/")

        counter = 0
        while True:
            res = self.socket.accept()
            client_sock = res[0]
            client_addr = res[1]
            print("Client address:", client_addr)
            print("Client socket:", client_sock)

            print("Request:")
            req = client_sock.readline()
            print(req)
            while True:
                h = client_sock.readline()
                if h == b"" or h == b"\r\n":
                    break
                print(h)
            client_sock.write(CONTENT % counter)

            client_sock.close()
            counter += 1
            print()
