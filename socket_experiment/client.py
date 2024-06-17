import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#the port of the server
port=12345

#lets connecting the server port with our local host
s.connect(('127.0.0.1',port))  

#lets receive data from the server and decode the byte into words
print(s.recv(1024).decode())  

s.close()
