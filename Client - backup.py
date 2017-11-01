import socket

host = '192.168.2.1'
port = 5560

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:
    command = input("Enter your command: ")
    if command == "alarm":
        # send EXIT request to other end
        s.send(str.encode(command))
        break
    elif command == "vals alarm":
        # send KILL command
        s.send(str.encode(command))
        break
    s.send(str.encode(command))
    reply = s.recv(1024)
    print(reply.decode('UTF-8'))

s.close()
