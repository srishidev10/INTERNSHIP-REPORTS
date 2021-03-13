import socket
import threading

connections=[]
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('',5000))
def recv_dat(conn,text):
    while 1:
        data=[]
        data.append(conn.recv(1024))
        if not data:
            continue
        print data
        if data==text:
            print "hi"



def connection():
    while 1:
        s.listen(1)
        conn,addr=s.accept()
        connections.append(conn)
        text = raw_input("Enter the text:")
        conn.send(text)
        print addr
        t1=threading.Thread(target=recv_dat,args=(conn,text))
        t1.start()


t=threading.Thread(target=connection,args=())
t.start()