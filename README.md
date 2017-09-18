### App for generating suggestion.
App consists of two parts.

First part is a generate_suggestions.py. This is console program, which prints
top 10 most used words from frequency dictionary for each given prefix.

Second part is a client/server interaction.
After connection client can use command like "get <prefix>" to get top 10
most used words with given prefix.
Client can use "exit" command to close connection.

### Requirements

python 3.4.4 or higher

### Usage
To generate suggestions for given dictionary and prefixes:
```bash
path_to_program\python generate_suggestions.py < path_to_file\filename
```
To run server you need to pass port number and path to dictionary:
```bash
path_to_program\python server.py 5000 path_to_dictionary\input_data.txt
```
To run client you need to pass hostname or IP and port number, for example:
```bash
path_to_program\python client.py localhost 5000
```
To be able to run tests you need to install pytest:
```bash
pip install -U pytest
```
And then to run tests use following command:
```bash
path_to_file\pytest
```
