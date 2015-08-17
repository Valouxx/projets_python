from Tkinter import *

class frame():
    def connexion(self):
        print('connect hited')
    
    def envoyerMessage(self):
        self.ajouterTexte(self.svMessageTape.get())
        self.svMessageTape.set('')
    
    def connexionEtablie():
        self.etatConnexion = NORMAL
    
    def ajouterTexte(self, nouveauTexte):
        self.monTexte.config(state=NORMAL)
        self.monTexte.insert(END, "\n")
        self.monTexte.insert(END, nouveauTexte)
        self.monTexte.config(state=DISABLED)
    
    
    def __init__(self):
        self.etatConnexion = NORMAL
        
        ### FENETRE
        myFrame = Tk()
        myFrame.title('Communicator')
        myFrame.geometry('450x650+100+100')

        ### CHAMP IP
        tfIpAdress = Entry(myFrame)
        tfIpAdress.pack(side=TOP)

        ### BOUTON CONNEXION
        bConnect = Button(myFrame, text = 'Connxion', command = self.connexion)
        bConnect.pack(side=TOP)

        ### BOUTON ENVOYER
        bEnvoyer = Button(myFrame, text = 'Envoyer !', command = self.envoyerMessage, state=self.etatConnexion)
        bEnvoyer.pack(side=BOTTOM)

        ### CHAMP MESSAGE A ENVOYER
        self.svMessageTape = StringVar()
        tfMessageTape = Entry(myFrame, textvariable=self.svMessageTape, state=self.etatConnexion)
        tfMessageTape.pack(side=BOTTOM)

        ### CONVERSATION AVEC SCROLLBAR
        scrollBar = Scrollbar(myFrame)
        self.monTexte = Text(myFrame, yscrollcommand=scrollBar.set, state=DISABLED)
        self.monTexte.pack(side=LEFT)
        scrollBar.config(command=self.monTexte.yview)
        scrollBar.pack(side=RIGHT, fill="y", expand=False)

        mainloop()