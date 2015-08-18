from threading import Thread
import socket

class threadReception(Thread):
    def __init__(self, frame):
        Thread.__init__(self)
        self.host = ''
        self.port = 11992
        self.keepGoing = True
        self.frame = frame
        
        self.Sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.Sock.bind((self.host,self.port))
    
        self.start()

    def run(self):
        self.Sock.listen(1)
        self.client, self.adresse = self.Sock.accept()

        while self.keepGoing:
            self.frame.ajouterTexte(self.client.recv(255))
        
        self.client.close()

    def finish():
        self.keepGoing = False
