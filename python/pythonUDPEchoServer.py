#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'
PORT = 12345

dataSize = 1024
serverMsg = b"Connected to client"

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:
    # AF_INET is IPv4 (2, tuple) for input and SOCK_DGRAM is UDP datagram
    server.bind((HOST,PORT))
    print("UDP server is listening")
    # Default backlog for multiple connection attempts
    receivedMsg, address = server.recvfrom(dataSize)
    # accept gives us a new socket from a client that is how we interact with client

    print('{} sent this message: {}'.format(address, receivedMsg))
    server.sendto(serverMsg, address)
