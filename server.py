import socket
import sys


from part_1 import get_data_from_file,  get_dict_trie_like, suggest_options


if __name__ == "__main__":
    path_to_file = input("Enter path to dictionary:\n> ")
    server_port = int(input("Enter port:\n> "))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.50.50.1'
    port = (host, server_port)
    s.bind(port)
    s.listen(1)
    conn, addr = s.accept()
    conn.send(bytes("Loading", encoding='utf-8'))
    prefixes_dict = suggest_options(get_dict_trie_like(get_data_from_file(
        path_to_file)), printing_option=False)
    conn.send(bytes("Server is ready", encoding='utf-8'))
    data = conn.recv(1024).decode('utf-8')
    print(data)
    while True:
        data = conn.recv(1024).decode('utf-8')
        if data == 'exit':
            break
        else:
            for word_info in prefixes_dict.get(data):
                conn.send(bytes(word_info[0] + 'end', encoding='utf-8'))
                conn.recv(1024).decode('utf-8')
            conn.send(bytes('\n', encoding='utf-8'))
    conn.close()
