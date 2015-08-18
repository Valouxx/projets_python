from Tkinter import *
from threadReception import *
from Emission import *
class frame():
    def connexionEtablie(self):
        print('Connexion etablie !')
        self.etatConnexion = NORMAL
        self.appliquerEtatConnexion()
    
    def connexionTerminee(self):
        self.etatConnexion = DISABLED
        self.appliquerEtatConnexion()
    
    def connexion(self):
        print('Debut de connexion')
        self.Emission = Emission(self.svIpAdress.get())
        self.connexionEtablie()
    
    def envoyerMessage(self):
        self.Emission.envoyerMessage(self.svMessageTape.get())
        self.ajouterTexte(self.svMessageTape.get())
        self.svMessageTape.set('')
    
    def ajouterTexte(self, nouveauTexte):
        self.monTexte.config(state=NORMAL)
        self.monTexte.insert(END, "\n")
        self.monTexte.insert(END, nouveauTexte)
        self.monTexte.config(state=DISABLED)
    
    def appliquerEtatConnexion(self):
        self.bEnvoyer.config(state = self.etatConnexion)
        self.tfMessageTape.config(state = self.etatConnexion)
    
    
    def __init__(self):
        try:
            self.etatConnexion = DISABLED
            self.threadReception = threadReception(self)
        
            ### FENETRE
            myFrame = Tk()
            myFrame.title('Chathon')
            myFrame.geometry('450x650+100+100')

            ### CHAMP IP
            self.svIpAdress = StringVar()
            tfIpAdress = Entry(myFrame, textvariable=self.svIpAdress)
            tfIpAdress.pack(side=TOP)

            ### BOUTON CONNEXION
            bConnect = Button(myFrame, text = 'Connxion', command = self.connexion)
            bConnect.pack(side=TOP)

            ### BOUTON ENVOYER
            self.bEnvoyer = Button(myFrame, text = 'Envoyer !', command = self.envoyerMessage)
            self.bEnvoyer.pack(side=BOTTOM)

            ### CHAMP MESSAGE A ENVOYER
            self.svMessageTape = StringVar()
            self.tfMessageTape = Entry(myFrame, textvariable=self.svMessageTape)
            self.tfMessageTape.pack(side=BOTTOM)

            ### CONVERSATION AVEC SCROLLBAR
            scrollBar = Scrollbar(myFrame)
            self.monTexte = Text(myFrame, yscrollcommand=scrollBar.set, state=DISABLED)
            self.monTexte.pack(side=LEFT)
            scrollBar.config(command=self.monTexte.yview)
            scrollBar.pack(side=RIGHT, fill="y", expand=False)

            self.appliquerEtatConnexion()

            mainloop()
        
        except KeyboardInterrupt:
            print('fin du programme')
            self.Emission.finish()
            self.threadReception.finish()
            self.myFrame.destroy()