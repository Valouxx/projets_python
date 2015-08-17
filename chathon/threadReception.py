from threading import Thread
import socket

class threadReception(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.host = ''
        self.port = 11992
        self.keepGoing = True
        
        self.Sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.Sock.bind((Host,Port))

    def run(self):
        self.Sock.listen(1)
        self.client, self.adresse = self.Sock.accept()

        while keepGoing:
            self.messageRecu = client.recv(255)

    def finish():
        self.keepGoing = False
        self.client.close()