#!/usr/bin/python

import socket
import time

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 1234))
    msg = 'Hello World!'
    s.sendall(msg.encode())
    s.close()
    time.sleep(3)