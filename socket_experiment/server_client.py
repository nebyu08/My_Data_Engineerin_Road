import socket

#lets define a port for which the server listens to
port=1234

#lets create socket
sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("socket has been created!!!")

#lets bind it
sk.bind(('',port))
print("socket has been binded with ",port)

#lets start listening to conncetions
sk.listen(5) #5 people are waiting inline

while True:
    c,addr=sk.accept()  #this returns new clients socket and his address
    print('got connection from, ',addr)

    #lets send thank you for reaching out message
    thank_you_message="thanks for reaching our"
    c.send(thank_you_message.encode())

    c.close()

    break