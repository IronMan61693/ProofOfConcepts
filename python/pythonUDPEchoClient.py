#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'
PORT = 12345

dataSize = 1024
message = b"Yo, did things work?"

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as newSocket:
    newSocket.sendto(message, (HOST,PORT))
    serverMsg, serverAddress = newSocket.recvfrom(dataSize)


print('We received back {} from the server'.format(serverMsg))
