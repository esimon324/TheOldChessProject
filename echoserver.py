#!/usr/bin/env python 

""" 
A simple echo server 
""" 

import socket 

host = '' 
port = 50000 
backlog = 5 
size = 1024 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind((host,port)) 
s.listen(backlog) 
while 1: 
    print ('listening')
    client, address = s.accept() 
    data = client.recv(size) 
    print(data)
    str = data.decode('utf-8')
    str = str.upper()
    if data:
        client.send(str.encode()) 
    client.close()