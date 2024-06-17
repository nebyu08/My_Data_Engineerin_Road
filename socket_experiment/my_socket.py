import socket
import sys


try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #this is creating a socket
    print("socket succesully ceated")

except socket.error as err:
    print("socket creation failed due to %S",err)


#lets connect to the google domain using socket
local_port=80

try:
    host_ip=socket.gethostbyname('www.google.com')   #this gives me the ip adress of the site
except socket.gaierror:
    print("there was an error in connecting to the website")
    sys.exit()

#lets connect to it now
s.connect((host_ip,local_port))

print("have sucssefully connected to the google ")