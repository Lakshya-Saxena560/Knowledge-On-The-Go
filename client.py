import socket

s = socket.socket()
host = input(str('Enter Server IP Address: '))
port = 2020

s.connect((host, port))

while True:
    incoming_message = s.recv(1024)
    incoming_message = incoming_message.decode()
    print('Host:', incoming_message)
    print()

    message = input(str('>>> '))
    message = message.encode()
    s.send(message)
    print()
