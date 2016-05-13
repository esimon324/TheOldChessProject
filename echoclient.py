#!/usr/bin/env python 

""" 
A simple echo client 
""" 

import socket 

host = '127.0.0.1' 
port = 50000
print(host)
print(port)
size = 1024 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((host,port)) 
str = 'hello world'
print('Sending: ',str)
s.send(str.encode()) 
data = s.recv(size) 
s.close() 
print ('Received:', data)