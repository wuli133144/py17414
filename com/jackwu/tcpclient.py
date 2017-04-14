#!/usr/bin/env python


import os
import re

from socket import *



host='localhost'
port=8000
bufsize=2048
addr=(host,port)

tcpclient=socket(AF_INET,SOCK_STREAM)

tcpclient.connect(addr)

while True:
    data=raw_input('input data')
    if not data:
        break
    else :
        tcpclient.send(data)
        data=tcpclient.recv(bufsize)
        if not data:
            break
        else :
         print data

tcpclient.close()

