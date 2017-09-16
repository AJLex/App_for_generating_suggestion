import socket
import sys


from part_1 import get_data_from_file,  get_dict_trie_like, suggest_options


def setup_server(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'localhost'
    server_adress = (host, port)
    s.bind(server_adress)
    s.listen(1)
    return s


def preparing_server():
    conn, addr = s.accept()
    conn.send(bytes("Loading", encoding='utf-8'))
    prefixes_dict = suggest_options(get_dict_trie_like(get_data_from_file(
        path_to_file)), printing_option=False)
    conn.send(bytes("Server is ready", encoding='utf-8'))
    data = conn.recv(1024).decode('utf-8')
    print(data)
    return prefixes_dict, conn


def client_request_processing(conn):
    while True:
        data = conn.recv(1024).decode('utf-8')
        if data == 'exit':
            break
        else:
            for word_info in prefixes_dict.get(data):
                conn.send(bytes(word_info[0] + 'end', encoding='utf-8'))
                conn.recv(1024).decode('utf-8')
            conn.send(bytes('\n', encoding='utf-8'))


if __name__ == "__main__":
    path_to_file = input("Enter path to dictionary:\n> ")
    s = setup_server(int(input("Enter port:\n> ")))
    prefixes_dict, conn = preparing_server()
    client_request_processing(conn)
    conn.close()
