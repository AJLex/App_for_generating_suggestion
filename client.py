import socket


# Function configures connection parametrs
def setup_connection(host, server_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # connection is TCP/IPv4
    sock.connect((host, server_port))
    sock.send(bytes('Client connected', encoding='utf-8'))
    return sock


# Function gets data from server and print it
def get_data_from_server(sock):
    print('Enter "exit" for exit.')
    while True:
        data = input("> ")
        sock.send(bytes(data, encoding='utf-8'))
        if data == 'exit':  # if client wants to disconnect, hi enter "exit"
            break
        while True:
            word = sock.recv(2048).decode('utf-8')
            if word[-3:] == 'end':
                print(word[:-3])
                sock.send(bytes('ok', encoding='utf-8'))  # client sends message to serve, when gets all data
            if word == "\n":  # data flow ended when server send "\n"
                print('\n')
                break

if __name__ == '__main__':
    host = input('Enter hostname:\n> ')
    server_port = int(input('Enter server port:\n> '))
    sock = setup_connection(host, server_port)
    get_data_from_server(sock)
    sock.close()
