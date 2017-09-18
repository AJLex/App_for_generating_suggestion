from collections import defaultdict


# Function reads a file from given path, format: words freq,
# and makes list with words and their freq
def get_data_from_file(path_to_file):
    raw_data = []
    with open(path_to_file, 'r', encoding='utf-8') as f:
            for line in f:
                raw_data.append(line.strip().split())
    return raw_data



# function сonsistently from standart input reads data, format:
# N - number of words
# word freq
# .....
# N lines
# M - number of prefixes
# prefix
# ...
# M lines
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


# function takes input data , format: word freq
# and creats of 2 dictionaries: for non single words and
# dictionary with 10 most used words for each initial letter of the input dictionary
def get_freq_dicts(input_data):
    freq_dict = defaultdict(lambda: defaultdict(dict))
    cache = defaultdict(list)
    for raw_data in input_data:
        current_word = raw_data[0]
        word_freq = int(raw_data[1])
        if len(current_word) > 1:
            # "-word_freq" is necessary for correct sort
            # first by freq then by lexicographical order
            freq_dict[current_word[0]][current_word[1:2]][current_word] = -word_freq
        cache[current_word[0]].append((current_word, -word_freq))
    for single_word, word_info in cache.items():
        word_info.sort(key=lambda word_info: (word_info[1], word_info[0]))
        cache[single_word] = word_info[:10]
    return freq_dict, cache


# function takes dictionarys with words and their freq, prefixes
# and searching top 10 most used words for given prefixes
def suggest_options(freq_dict, cache, prefixes, max_len):
    for prefix in prefixes:
        # there is no need to seek if prefix already in dict
        if prefix not in cache:
            list_of_options = []
            if len(prefix) > 1:
                if prefix:
                    if prefix[:1] in freq_dict and \
                       prefix[1:2] in freq_dict[prefix[:1]]:
                        for word, freq in freq_dict[prefix[:1]][prefix[1:2]].items():
                            if word.startswith(prefix):
                                list_of_options.append((word, freq))
            list_of_options.sort(key=lambda word_info: (word_info[1], word_info[0]))
            cache[prefix] = list_of_options[:max_len]
    return cache


if __name__ == '__main__':
    input_data = get_input_data()
    freq_dict, cache = get_freq_dicts(input_data[0])
    prefixes_dict = suggest_options(freq_dict, cache, input_data[1], max_len=10)
    for prefix in input_data[1]:
        for word_info in prefixes_dict[prefix]:
                print(word_info[0])
        print('\n')
