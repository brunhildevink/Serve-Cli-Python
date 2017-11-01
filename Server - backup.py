import socket

host = ''
port = 5560

storedValue = "Yo what's up?"

def setupServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created.")
    try:
        s.bind((host, port))
    except socket.error as msg:
        print(msg)
    print("Socket has complete.")
    return s

def setupConnection():
    s.listen(1) # Allow one connection at a time
    conn, address = s.accept()
    print("Connected to: " + address[0] + ":" + str(address[1]))
    return conn


def GET():
    reply = storedValue
    return reply

def REPEAT(dataMessage):
    reply = dataMessage[1]
    return reply


def dataTransfer(conn):
    # a big loop that sends/receives data until told not to
    while True:
        # receive data
        data = conn.recv(1024) # receive the data
        data = data.decode('utf-8')
        dataMessage = data.split(' ', 1)
        command = dataMessage[0]
        if command == 'GET':
            reply = GET()
        elif command == 'REPEAT':
            reply = REPEAT(dataMessage)
        elif command == 'EXIT':
            print("Our client has left us : ")
            break
        elif command == 'false alarm':
            print("Everything is safe.")
            s.close()
            break
        else:
            reply = 'Unknown command'
        # send the reply back to the client
        conn.sendall(str.encode(reply))
        print("Data has been sent!")


s = setupServer()

while True:
    try:
        conn = setupConnection()
        dataTransfer(conn)
    except:
        break