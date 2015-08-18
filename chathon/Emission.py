import socket

class Emission():
    def __init__(self, ipServer):
        self.host = ipServer
        self.port = 11992
        
        self.monSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.monSocket.connect((self.host, self.port))
    
    def finish(self):
        self.monSocket.close()
        
    def envoyerMessage(self, message):
        print('En cours denvoi')
        self.monSocket.send(message)
        print('Message envoye')
