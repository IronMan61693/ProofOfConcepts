#!/usr/bin/env python3

import socket

HOST = "127.0.0.1"
PORT = 42069

headerSize = 10
dataSize = 16
closeMessage = "Message received, go ahead and close the connection"
closeMessage = f"{len(closeMessage) :<{headerSize}}" + closeMessage

incomingMsg = ""
newMsg = True
sendClose = False

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as newSocket: #indent if used
newSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
newSocket.connect((HOST, PORT))

while True:
    data = newSocket.recv(dataSize)
    if not data:
        break

    if newMsg:
        print("Incoming message of length:", data[:headerSize])
        msglen = int(data[:headerSize])
        newMsg = False

    incomingMsg += data.decode("utf-8")

    print(len(incomingMsg))  # This demonstrates it coming in pieces

    if len(incomingMsg) - headerSize == msglen:
        print("Message fully received of size {}".format(msglen))
        print(incomingMsg[headerSize:])
        sendClose = True
        newMsg = True  # I could use this to allow receiving of multiple messages

    # newSocket.sendall(bytes(closeMessage, "utf-8"))
