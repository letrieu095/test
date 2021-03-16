#!/usr/bin/python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 1234
s.bind(('0.0.0.0', port))
print ('Socket binded to port ', port)
s.listen(3)
print ('socket is listening..')

while True:
   c, addr = s.accept()
   print ('Got connection from ', addr)
   print (c.recv(1024))
   c.close()