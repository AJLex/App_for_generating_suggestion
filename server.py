import socket
import sys


from generate_suggestions import get_data_from_file,  get_freq_dicts, suggest_options


# Function configures the server
def setup_server(port):
    # connection is TCP/IPv4
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ''
    server_adress = (host, port)
    sock.bind(server_adress)
    sock.listen(1)  # client queue length
    return sock


# Function prepares server for client request processing
def preparing_server(path_to_file, sock):
    try:  # if wrong path to file - exit
        # prepare dictionary
        freq_dict, cache = get_freq_dicts(get_data_from_file(path_to_file))
    except:
        print('Не верно указан путь к файлу или ошибка файла.')
        sys.exit()
    conn, addr = sock.accept()  # waiting for client connection
    # getting message from client, when he connected
    data = conn.recv(1024).decode('utf-8')
    print(data, 'from ', addr[0])
    return freq_dict, cache, conn


# Function processing client request
def client_request_processing(freq_dict, cache, conn, max_len):
    while True:
        data = conn.recv(1024).decode('utf-8')
        if data == 'exit':  # if client sends "exit", server turns off
            break
        try:
            command, prefix = data.split()
            if command == 'get':
                prefix = prefix[1: len(prefix) - 1]  # delet "<", ">"
                cache = suggest_options(freq_dict, cache, [prefix], max_len)                
                for word_info in cache[prefix]:
                    # "end" says to client that all data was obtained
                    conn.send(bytes(word_info[0] + 'end', encoding='utf-8'))
                    # server gets answer from client, when client gets all data
                    conn.recv(1024).decode('utf-8')
        except:
            conn.send(bytes('Invalid command' + 'end', encoding='utf-8'))
        # server sending "\n", when request processing is ending
        conn.send(bytes('\n', encoding='utf-8'))


if __name__ == "__main__":
    port = int(sys.argv[1])
    path_to_file = sys.argv[2]
    sock = setup_server(port)
    freq_dict, cache, conn = preparing_server(path_to_file, sock)
    client_request_processing(freq_dict, cache, conn, max_len=10)
    conn.close()
