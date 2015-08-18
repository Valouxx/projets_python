from threading import Thread
import socket

try:
    host = ''
    port = 11992
    keepGoing = True
        
    Sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    Sock.bind((host,port))
    
    Sock.listen(1)
    client, adresse = Sock.accept()
    
    print('Client connecte')

    while keepGoing:
        print('en attente de message')
        print(client.recv(255))
        print('Fin message')

    client.close()

except KeyboardInterrupt:
    keepGoing = False
