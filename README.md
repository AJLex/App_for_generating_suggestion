App consist of two part.
Requirements is python 3.4.4 or higher


First part is a generate_suggestions.py. This is console program, which print
top 10(or less) most used word from frequency dictionary for each given prefixes.

Format of input file should be like that:
N - first string is number of strings with word, frequency
... - next N strings should contain words, frequency
word frequency - Warning, between word and his frequency must be just one space
...
M - next string after N+1 strings is number of strings with prefixes
...
prefix - prefix should contain at least one letter

For run program needs to redirect standard input, for example:
path_to_program\python generate_suggestions.py < path_to_file\filename

After processing of input file program print 10(or less) most used word for
each prefixes, spaced by "\n"


Second part is a client/server interaction.
After connection client to server, client sending command containing prefix,
server processes request and return top 10(or less) most used words row by row
for this prefix.
Server.py is a console program, which start server. At startup, server processes
input dictionary and awaiting connection of client.
Dictionary should be like that:

word frequency - Warning, between word and his frequency must be just one space

For run server needs input port and path_to_dictionary, for example:
path_to_program\python server.py 5000 path_to_dictionary\input_data.txt

Сlient is a console program. After connection with server, client
client can use command like "get <prefixes>" to get top 10(or less) most used word
for entering prefix. For close connection client can enter "exit".

For run client needs input hostname or IP and hort, for example:
path_to_program\python client.py localhost 5000
