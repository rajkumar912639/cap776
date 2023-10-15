#print(ord('H'))
import socket
mysock =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect((dta.pr4e.org.80))
cmd ='get http:https://www.coursera.org/learn/python-network-data/lecture/MbRIS/12-3-unicode-characters-and-strings'.encode()
mysock.send(cmd)
while True:
    data =mysock.recv(512)
    if(len(data)<1) :
        break
    print(data.decode())
mysock.close()
