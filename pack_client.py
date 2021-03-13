import socket
import threading

name = raw_input("Enter the username:")
#

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 5000
s.connect(('localhost',port))
#t=threading.Thread(Target=recv(),args=(s,))

while 1:
    data=s.recv(1024)
    print data
    message = raw_input()
    for i in range(0,len(message)):
            s.sendall(message[i])

