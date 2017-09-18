### App for generating suggestion.

### Requirements

python 3.4.4 or higher

### Usage
for run generate_suggestions.py
```bash
path_to_program\python generate_suggestions.py < path_to_file\filename
```
for run server.py needs input port and path_to_dictionary
```bash
path_to_program\python server.py 5000 path_to_dictionary\input_data.txt
```
or run client needs input hostname or IP and port, for example:
```bash
path_to_program\python client.py localhost 5000
```

App consist of two part.

First part is a generate_suggestions.py. This is console program, which print
top 10(or less) most used word from frequency dictionary for each given prefixes spaced by "\n".

Second part is a client/server interaction.
After connection client to server, client sends command containing prefix,
server processes request and returns top 10(or less) most used words row by row
for this prefix.
Server.py is a console program, which start server.
Сlient is a console program. After connection with server, client
client can use command like "get <prefixes>" to get top 10(or less) most used word
for entering prefix. For close connection client can enter "exit".
