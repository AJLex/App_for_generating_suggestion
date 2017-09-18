import socket
import sys


# Function configures connection parametrs
def setup_connection(host, server_port):
    # connection is TCP/IPv4
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, server_port))
    return sock


# Function gets data from server and print it
def get_data_from_server(sock):
    print('Enter "exit" for exit.')
    while True:
        data = input("> ")
        if data == '':  # protection from entering empty string
            sock.send(bytes('empty', encoding='utf-8'))
        sock.send(bytes(data, encoding='utf-8'))
        if data == 'exit':  # if client wants to disconnect, hi enter "exit"
            break
        while True:
            word = sock.recv(2048).decode('utf-8')
            # server sends "word + end", "end" - means that all message was sended
            if word[-1] == ' ':
                print(word[:-1])
                # client sends message to serve, when gets all data
                sock.send(bytes('ok', encoding='utf-8'))
            if word == "\n":  # data flow ended when server send "\n"
                print('\n')
                break


if __name__ == '__main__':
    host = sys.argv[1]
    server_port = int(sys.argv[2])
    sock = setup_connection(host, server_port)
    get_data_from_server(sock)
    sock.close()
