#!/usr/bin/env python3

import socket

HOST = "127.0.0.1"
PORT = 12345

# Not very UDP but a way to tell the server to stop listening
fynMSG = b"xXyY"

# headerSize = 10
# For the sake of allowing a loop and then closing the connection I will be
#  setting a size and a close condition, but as this is UDP that seems weird because
#  UDP is connectionless and packets could get lost, etc so this is not reliable nor
#  best behavior
dataSize = 4
message = b"Yo, did things work?1 Yo, did things work?2 Yo, did things work?3"
sentSize = 0
leftBound = 0
rightBound = dataSize

newSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# newSocket.sendto(message, (HOST,PORT))
while sentSize < len(message):
    newSocket.sendto(message[leftBound:rightBound], (HOST, PORT))
    leftBound = rightBound
    rightBound += dataSize
    sentSize += dataSize
newSocket.sendto(fynMSG, (HOST, PORT))


# I am not having the server send anything but if I did
# serverMsg, serverAddress = newSocket.recvfrom(dataSize)


# print('We received back {} from the server'.format(serverMsg))
