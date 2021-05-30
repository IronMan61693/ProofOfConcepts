#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'
PORT = 42069

dataSize = 1024
message = b"Yo, did things work?"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as newSocket:
    newSocket.connect((HOST,PORT))
    newSocket.sendall(message)
    data = newSocket.recv(dataSize)

    newSocket.close() # It does this automagically, but I am making it explicit
    # If I wanted to actually manage closing connections manually I would make
    # a multi-connection server

print('We received back ', str(repr(data)))
