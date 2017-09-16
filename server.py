import socket


from part_1 import get_data_from_file,  get_dict_trie_like, suggest_options


# Function configures the server
def setup_server(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # connection is TCP/IPv4
    host = 'localhost'
    server_adress = (host, port)
    s.bind(server_adress)
    s.listen(1)
    return s


# Function prepares server for client request processing
def preparing_server(path_to_file):
    conn = s.accept()[0]  # waiting for client connection
    conn.send(bytes("Loading", encoding='utf-8'))  # sending server status to the client
    prefixes_dict = suggest_options(get_dict_trie_like(get_data_from_file(
        path_to_file)), printing_option=False)  # prepare dictionary
    conn.send(bytes("Server is ready", encoding='utf-8'))  # sending server status to the client
    data = conn.recv(1024).decode('utf-8')  # getting message from client, when he connected
    print(data)
    return prefixes_dict, conn


# Function processing client request
def client_request_processing(conn):
    while True:
        data = conn.recv(1024).decode('utf-8')
        if data == 'exit':  # if client sends "exit", server turn off
            break
        else:
            for word_info in prefixes_dict.get(data):
                conn.send(bytes(word_info[0] + 'end', encoding='utf-8'))  # "end" says to client that all data was obtained
                conn.recv(1024).decode('utf-8')  # server gets answer from client, when client gets all data
            conn.send(bytes('\n', encoding='utf-8'))  # server sending "\n", when request processing is ending


if __name__ == "__main__":
    path_to_file = input("Enter path to dictionary:\n> ")
    s = setup_server(int(input("Enter port:\n> ")))
    prefixes_dict, conn = preparing_server(path_to_file)
    client_request_processing(conn)
    conn.close()
