#!/usr/bin/env python3

import socket

HOST = "127.0.0.1"
PORT = 42069

headerSize = 10
dataSize = 16
localHostName = socket.gethostname()
serverMsg = ""

incomingMsg = ""
newMsg = True

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
# AF_INET is IPv4 (2, tuple) for input and SOCK_STREAM is  TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
print("TCP server is listening")

# with connection:

while True:
    # Default backlog for multiple connection attempts
    connection, address = server.accept()
    print("{} established connection with: {}".format(localHostName, address))
    # accept gives us a new socket from a client that is how we interact with client

    # connectData = connection.recv(dataSize)
    # if not connectData:
    #     break
    serverMsg = "This is a test from the server."
    serverMsg = f"{len(serverMsg) :<{headerSize}}" + serverMsg
    print(serverMsg)
    connection.sendall(bytes(serverMsg, "utf-8"))
    # If I want a persistent connection to send and receive multiple communications
    # I would not have a close here and I would make use of newMsg
    connection.close()
    break

    # connectData = connection.recv(dataSize)
    # if not connectData:
    #     break
    #
    # if newMsg:
    #     print("Incoming message of length:",connectData[:headerSize])
    #     msglen = int(connectData[:headerSize])
    #     newMsg = False
    #
    # incomingMsg += connectData.decode("utf-8")
    #
    # print(len(incomingMsg)) # This demonstrates it coming in pieces
    #
    # if len(incomingMsg) - headerSize == msglen:
    #     print("Message fully received of size {}".format(msglen))
    #     print(incomingMsg[headerSize:])
    #     newMsg = True # I could use this to allow receiving of multiple messages
    #     server.close()
