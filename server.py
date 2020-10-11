import socket


s = socket.socket()
hostname = socket.gethostname()

print('Server will start on host:', hostname)

port = 2020
s.bind((hostname, port))
print('Server bounded to host and port successfully')
print('Waiting for incoming connections')

s.listen(1)
conn, addr = s.accept()

print('IP Address', addr, 'connected to the server.')

while True:
    message = input(str('>>> '))
    message = message.encode()
    conn.send(message)
    print()

    incoming_message = conn.recv(1024)
    incoming_message = incoming_message.decode()
    print('Client: ', incoming_message)
    print()
