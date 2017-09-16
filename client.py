import socket
import sys


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input('Enter hostname:\n> ')
server_port =int(input('Enter server port:\n> '))
port = (host, server_port)
s.connect(port)
data = s.recv(1024)
print (data.decode('utf-8'))
data = s.recv(1024)
print (data.decode('utf-8'))
s.send(bytes('Client connected', encoding='utf-8'))
while True:
    data = input("> ")
    s.send(bytes(data, encoding='utf-8'))
    if data == 'exit':
        break
    else:
        while True:
            word = s.recv(2048).decode('utf-8')
            if word[-3:] == 'end':
                print(word[:-3])
                s.send(bytes('ok', encoding='utf-8'))
            if word == "\n":
                print('\n')
                break
s.close()
