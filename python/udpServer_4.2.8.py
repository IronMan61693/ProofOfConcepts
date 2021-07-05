#!/usr/bin/env python3

import socket

HOST = "127.0.0.1"
PORT = 12345

# Not very UDP but a way to tell the server to stop listening
fynMSG = b"xXyY"

dataSize = 16
# Not sending a response to client
# serverMsg = b"Connected to client"

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# AF_INET is IPv4 (2, tuple) for input and SOCK_DGRAM is UDP datagram
server.bind((HOST, PORT))
# Default backlog for multiple connection attempts

while True:
    print("UDP server is listening")
    receivedMsg, address = server.recvfrom(dataSize)
    if receivedMsg == fynMSG:
        print("close packet received, closing")
        server.close()
        break
    # accept gives us a new socket from a client that is how we interact with client

    print("{} sent this message: {}".format(address, receivedMsg))


# with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:
#     # AF_INET is IPv4 (2, tuple) for input and SOCK_DGRAM is UDP datagram
#     server.bind((HOST,PORT))
#     # Default backlog for multiple connection attempts
#     receivedMsg, address = server.recvfrom(dataSize)
#     # accept gives us a new socket from a client that is how we interact with client
#
#     print('{} sent this message: {}'.format(address, receivedMsg))
#     server.sendto(serverMsg, address)
