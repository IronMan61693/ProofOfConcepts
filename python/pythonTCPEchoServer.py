#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'
PORT = 42069

dataSize = 1024
localHostName = socket.gethostname()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    # AF_INET is IPv4 (2, tuple) for input and SOCK_STREAM is  TCP
    server.bind((HOST,PORT))
    server.listen()
    print("TCP server is listening")
    # Default backlog for multiple connection attempts
    connection, address = server.accept()
    # accept gives us a new socket from a client that is how we interact with client
    with connection:
        print('{} established connection with: {}'.format(localHostName, address))
        while True:
            connectData = connection.recv(dataSize)
            if not connectData:
                break
            connection.sendall(connectData)
