import socket
import client.py

host = '192.168.42.1'
port = 5560

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:
    command = get
    if command == "true":
        # send EXIT request to other end
        s.send(str.encode(command))
        break
    elif command == "KILL":
        # send KILL command
        s.send(str.encode(command))
        break
    s.send(str.encode(command))
    reply = s.recv(1024)
    print(reply.decode('UTF-8'))

s.close()
