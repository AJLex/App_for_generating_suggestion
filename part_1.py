from collections import defaultdict


# Function reads a file from given path and makes two lists
def get_data_from_file(path_to_file):
    raw_data = []
    prefixes = []
    with open(path_to_file, 'r', encoding='utf-8') as f:
            input_data = f.readlines()
    number_of_words = int(input_data[0].strip())
    for index in range(1, number_of_words + 1):
        raw_data.append(input_data[index].strip().split())
    for index in range(number_of_words + 2, len(input_data)):
        prefixes.append(input_data[index].strip())
    return raw_data, prefixes


# function puts firsr "number_of_words" words into raw_data list
# and next "number_of_prefixes" prefixes puts into prefixes list
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


# function takes input_data, which contain "raw_data" list and "prefixes" list
# from the "raw_data" list two dictionaries are created for a word from one letter
# and for a word from several letters
# "prefixes" does not change
def get_dict_trie_like(input_data):
    freq_dict = defaultdict(lambda: defaultdict(dict))
    freq_dict_singl_word = defaultdict(dict)
    for raw_data in input_data[0]:
        if len(raw_data[0]) > 1:
            freq_dict[raw_data[0][0]][raw_data[0][:2]][raw_data[0]] = raw_data[1]
        freq_dict_singl_word[raw_data[0][0]][raw_data[0]] = raw_data[1]
    return [freq_dict, freq_dict_singl_word], input_data[1]


# function takes input_data, which contain list of dictionaries and "prefixes" list
# for each prefix from "prefixes" list function searching and then printing
# top 10 most used words and their frequency of repetition
def suggest_options(input_data, printing_option=True):
    dict_trie = input_data[0]
    prefixes = input_data[1]
    prefixes_dict = defaultdict(list)
    for prefix in prefixes:
        list_of_options = []
        if len(prefix) > 1:
            for word, freq in dict_trie[0][prefix[:1]][prefix[:2]].items():
                if prefix == word[:len(prefix)]:
                    list_of_options.append((word, int(freq)*-1))
        else:
            for word, freq in dict_trie[1][prefix[:1]].items():
                if prefix == word[:len(prefix)]:
                    list_of_options.append((word, int(freq)*-1))
        list_of_options.sort(key=lambda word_info: (word_info[1], word_info[0]))
        if printing_option:
            for word_info in list_of_options[:10]:
                print(word_info[0])
            print('\n')
        else:
            prefixes_dict[prefix] = list_of_options[:10]
    return prefixes_dict


if __name__ == '__main__':
    suggest_options(get_dict_trie_like(get_input_data()))
