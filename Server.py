from tkinter import *
import socket

host = ''
port = 5560

storedValue = "Yo what's up?"


def setupServer():
    # het aanmaken van de server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created.")
    try:
        s.bind((host, port))
    except socket.error as msg:
        print(msg)
    print("Socket has complete.")
    return s

def setupConnection():
    # het aanmaken van de connectie (verbinding)
    s.listen(1)
    conn, address = s.accept()
    print("Connected to: " + address[0] + ":" + str(address[1]))
    return conn

def dataTransfer(conn):
    # een grote loop die data ontvangt/verzend
    # data ontvangen
    data = conn.recv(1024)
    # data decoden
    data = data.decode('utf-8')
    # data splitten
    dataMessage = data.split(' ', 1)
    # eerste "woord" van de data
    command = dataMessage[0]
    print(command)
    # komt de datamessage overeen met button click (ontvangen van client): print dan dit:
    if command == 'button':
        print('motion detected')

global s
s = setupServer()
conn = setupConnection()

class buttons:
    # een class die de hele GUI bundelt met de bijbehorende functies
    def __init__(self, master):
        theLabel = Label(root, text="Beveiligingssysteem")
        theLabel.pack()

        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="Alarm", command=self.alarm)       # knop 1
        self.printButton.pack(side=LEFT)

        self.printButton = Button(frame, text="False alarm", command=self.false_alarm)     # knop 2
        self.printButton.pack(side=LEFT)

    def alarm(self):                                            # stuurt (encoded) "alarm" terug naar client
        print("alarm is binnengekomen op de server")
        conn.sendall(str.encode("alarm"))

    def false_alarm(self):                                      # stuurt (encoded) "falsealarm" terug naar client
        print("vals alarm is binnengekomen op de server")
        conn.sendall(str.encode("falsealarm"))


root = Tk()
a = buttons(root)
root.mainloop()

