#Source: https://stackoverflow.com/questions/38854169/typeerror-schreiben-methode-missing-1-required-positional-argument-self
from tkinter import *

class Versenden(object):
    def testen(self):
        print("Funktioniert")


class Schreiben(object):


    def __init__(self, sender, smtpserver, smtppasswort):
        self.Absender = sender
        self.Smtpserver = smtpserver
        self.Smtppasswort = smtppasswort
        Schreiben.schreiben_methode()

    def schreiben_methode(self):
        root1 = Tk()
        versenden = Versenden()
        labelEmpfaenger = Label(root1, text="Empfaenger:")
        labelBetreff = Label(root1, text="Betreff:")
        empfaenger = Entry(root1)
        betreff = Entry(root1)
        inhalt = Text(root1, height=10, width=50)
        buttonSenden = Button(root1, text="senden", command=lambda: versenden.testen())

        labelEmpfaenger.grid(row=0, column=0)
        empfaenger.grid(row=0, column=1)
        labelBetreff.grid(row=1, column=0)
        betreff.grid(row=1, column=1)
        inhalt.grid(row=2, columnspan=2)
        buttonSenden.grid(row=3, columnspan=2)

        root1.mainloop()

root = Tk()
schreiben = Schreiben("a", "a", "a")

labelEmail = Label(root, text="Ihre Email-Addresse")
labelPasswort = Label(root, text="Ihr Passwort")
labelServer = Label(root, text="SMTP-Server")


email = Entry(root)
passwort = Entry(root)
server = Entry(root)

buttonWeiter = Button(root, text="Weiter", command=lambda: schreiben.schreiben_methode(email, server, passwort))


labelEmail.grid(row=0)
labelPasswort.grid(row=1)
email.grid(row=0, column=1)
passwort.grid(row=1, column=1)
labelServer.grid(row=2)
server.grid(row=2, column=1)
buttonWeiter.grid(row=3, columnspan=2)

root.mainloop()