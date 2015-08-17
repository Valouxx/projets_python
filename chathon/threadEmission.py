import PicoBorgRev
from threading import Thread
from time import sleep
import numpy

class threadCommande(Thread):
    def __init__(self, client):
        Thread.__init__(self)
        self.client = client
        self.keepGoing = True
        self.octetsRecus = numpy.zeros(5, dtype='i')
        
        PBR = PicoBorgRev.PicoBorgRev()
        PBR.Init()
        PBR.ResetEpo()
    
    def run(self):
        while keepGoing:
            for i in range(0,4):
                self.octetsRecus[i] = client.recv(1)
            
            idEcran = struct.unpack("!b", self.octetsRecus[1])[0]
            valDirection = struct.unpack("!b", self.octetsRecus[2])[0]
            valVitesse = - struct.unpack("!b", self.octetsRecus[3])[0] # probleme Android corrige ici
                
            print 'Ecran de pilotage : ', idEcran
            print 'Valeur de la direction : ', valDirection
            print 'Valeur de la vitesse : ', valVitesse
            print ''
        
            PBR.SetMotor1(valVitesse/100.0)
            PBR.SetMotor2(valDirection/100.0)

    def finish():
        keepGoing=False
        sleep(2)
        PBR.MotorsOff()
        print 'threadCommande arrete'