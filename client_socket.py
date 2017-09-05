#!/usr/bin/python

import socket

s = socket.socket()
host = socket.gethostname()
port = 6667

while True:


s.connect((host, port))
print s.recv(1024)
s.send("Hello Bitch")
s.close