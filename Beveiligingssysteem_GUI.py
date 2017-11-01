from tkinter import *
import tkinter.messagebox

class buttons:

    def __init__(self, master):
        theLabel = Label(root, text="Beveiligingssysteem")
        theLabel.pack()

        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="Turn on", command=self.passwordON)       # knop 1
        self.printButton.pack(side=LEFT)

        self.printButton = Button(frame, text="Turn off", command=self.passwordOFF)     # knop 2
        self.printButton.pack(side=LEFT)

    def passwordON(self):
        password = input("Geef wachtwoord:")
        if password == "123":
            print("Systeem is ingeschakeld.")
            tkinter.messagebox.showinfo('prompt', 'Systeem is ingeschakeld.')
        else:
            print("Wachtwoord onjuist")
            tkinter.messagebox.showinfo('prompt', 'Wachtwoord is onjuist. \n Probeer opnieuw.')

    def passwordOFF(self):
        password = input("Geef wachtwoord:")
        if password == "123":
            print("Systeem is uitgeschakeld.")
            tkinter.messagebox.showinfo('prompt', 'Systeem is uitgeschakeld.')
        else:
            print("Wachtwoord onjuist")
            tkinter.messagebox.showinfo('prompt', 'Wachtwoord is onjuist. \n Probeer opnieuw')

root = Tk()
a = buttons(root)
root.mainloop()