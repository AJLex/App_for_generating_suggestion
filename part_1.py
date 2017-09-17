from collections import defaultdict


# Function reads a file from given path and makes list
def get_data_from_file(path_to_file):
    raw_data = []
    with open(path_to_file, 'r', encoding='utf-8') as f:
            for line in f:
                raw_data.append(line.strip().split())
    return raw_data



# function reads input data, format: words and their frequency, prefixes
# and makes fist list with words and their frequency, second - list of prefixes
def get_input_data():
    raw_data = []
    prefixes = []
    number_of_words = int(input())
    for index in range(number_of_words):
        line = input()
        raw_data.append(line.strip().split())
    number_of_prefixes = int(input())
    for index in range(number_of_prefixes):
        line = input()
        prefixes.append(line.strip())
    return raw_data, prefixes


# function takes input data and creats kist of 2 dictionaries
def get_dict_trie_like(input_data):
    freq_dict = defaultdict(lambda: defaultdict(dict))
    freq_dict_singl_word = defaultdict(dict)
    for raw_data in input_data:
        current_word = raw_data[0]
        word_freq = int(raw_data[1])
        if len(current_word) > 1:
            freq_dict[current_word[0]][current_word[:2]][current_word] = word_freq
        freq_dict_singl_word[current_word[0]][current_word] = word_freq
    return [freq_dict, freq_dict_singl_word]


# function takes input data and searching top 10 most used words for given prefix
def suggest_options(dict_trie, prefixes, max_len):
    cash = defaultdict(list)
    for prefix in prefixes:
        if prefix not in cash:  # there is no need to seek if prefix already in dict 
            try:
                list_of_options = []
                if len(prefix) > 1:
                    for word, freq in dict_trie[0][prefix[:1]][prefix[:2]].items():
                        if prefix == word[:len(prefix)]:
                            # it's necessary for correct sort
                            list_of_options.append((word, freq*-1))
                else:
                    for word, freq in dict_trie[1][prefix[:1]].items():
                        if prefix == word[:len(prefix)]:
                            # it's necessary for correct sort
                            list_of_options.append((word, freq*-1))
                list_of_options.sort(key=lambda word_info: (word_info[1], word_info[0]))
                cash[prefix] = list_of_options[:max_len]
            except KeyError:
                print('Нет такого префикса')
            except IndexError:
                print('Пустой словарь')
    return cash


if __name__ == '__main__':
    input_data = get_input_data()
    prefixes_dict = suggest_options(get_dict_trie_like(input_data[0]),
        input_data[1], max_len=10)
    for prefix in input_data[1]:
        for word_info in prefixes_dict[prefix]:
                print(word_info[0])
        print('\n')
