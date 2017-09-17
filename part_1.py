from collections import defaultdict


# Function reads a file from given path and makes two lists
def get_data_from_file(path_to_file):
    raw_data = []
    with open(path_to_file, 'r', encoding='utf-8') as f:
            for line in f:
                raw_data.append(line.strip().split())
    return raw_data


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
    for raw_data in input_data:
        current_word = raw_data[0]
        word_freq = raw_data[1]
        if len(current_word) > 1:
            freq_dict[current_word[0]][current_word[:2]][current_word] = word_freq
        freq_dict_singl_word[current_word[0]][current_word] = word_freq
    return [freq_dict, freq_dict_singl_word]


# function takes input_data, which contain list of dictionaries and "prefixes" list
# for each prefix from "prefixes" list function searching and then printing
# top 10 most used words and their frequency of repetition
def suggest_options(dict_trie, prefixes, max_len):
    prefixes_list = []
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
        prefixes_list.append([prefix, list_of_options[:10]])
    return prefixes_list


if __name__ == '__main__':
    input_data = get_input_data()
    prefixes_list = suggest_options(get_dict_trie_like(input_data[0]),
        input_data[1], max_len=10)
    for prefix_info in prefixes_list:
        for word_info in prefix_info[1]:
            print(word_info[0])
        print('\n')
