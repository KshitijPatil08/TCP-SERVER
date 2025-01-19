#!/usr/bin/python3

import socket

serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostbyname('localhost')
port = 1024

serversocket.bind(("x.xxx.xxx.xxx",port))

serversocket.listen(3)

while True:
    clientsocket, addr = serversocket.accept()
    print("Got a connection from %s" % str(addr))

    message = "hello! Thank you for connecting to the server" +'\r\n'
    clientsocket.send(message.encode('ascii'))

    clientsocket.close() 