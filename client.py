import socket


# Function configures connection parametrs
def setup_connection(host, server_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # connection is TCP/IPv4
    s.connect((host, server_port))
    return s


# Function checks server status
def check_server_status():
    data = s.recv(1024)
    print(data.decode('utf-8'))
    data = s.recv(1024)
    print(data.decode('utf-8'))
    s.send(bytes('Client connected', encoding='utf-8'))  # sending to server, that client connected


# Function gets data from server and print it
def get_data_from_server(s):
    while True:
        data = input("> ")
        s.send(bytes(data, encoding='utf-8'))
        if data == 'exit':  # if client wants to disconnect, hi enter "exit"
            break
        else:
            while True:
                word = s.recv(2048).decode('utf-8')
                if word[-3:] == 'end':
                    print(word[:-3])
                    s.send(bytes('ok', encoding='utf-8'))  # client sends message to serve, when gets all data
                if word == "\n":  # data flow ended when server send "\n"
                    print('\n')
                    break

if __name__ == '__main__':
    host = input('Enter hostname:\n> ')
    server_port = int(input('Enter server port:\n> '))
    s = setup_connection(host, server_port)
    check_server_status()
    get_data_from_server(s)
    s.close()
