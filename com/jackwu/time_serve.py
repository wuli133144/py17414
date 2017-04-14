#!/usr/bin/env python


import os
import re

from socket import *

from time import ctime

host=''
port=8000
bufsize=2048
addr=(host,port)

tcpserve=socket(AF_INET,SOCK_STREAM)
tcpserve.bind(addr)
tcpserve.listen(10)


while True:
    print "waiting  for connect"
    tcpclient,addr=tcpserve.accept()
    print tcpserve.accept.__doc__
    print ".......connected from.....",addr
    while True:
        data=tcpclient.recv(bufsize)
        if not data:
            break
        else :
            tcpclient.send('[%s]%s'%(ctime(),data))

    tcpclient.close()

tcpserve.close()


