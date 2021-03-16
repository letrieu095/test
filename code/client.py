#!/usr/bin/python

import socket
import time
import os
from datetime import datetime

ip_server = os.getenv('IP_SERVER', '127.0.0.1')
port = os.getenv('PORT', 1234)

while True:
    now = datetime.now()
    date = now.strftime("%Y-%m-%d %H:%M:%S")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip_server, int(port)))
    msg = "(%s) - Hello World!" % date
    s.sendall(msg.encode())
    s.close()
    time.sleep(60)