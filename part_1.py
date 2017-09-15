import csv
import random


def get_input_data():
    n = int(input())
    raw_data = []
    prefixes = []
    for index in range(0, n):
        line = input()
        raw_data.append(line.strip().split())
    m = int(input())
    for index in range(0, m):
        line = input()
        prefixes.append(line.strip())
    return raw_data, prefixes


def get_dict_trie(input_data):
    freq_dict = {}
    freq_dict_one = {}
    for raw_data in input_data[0]:
        if len(raw_data[0]) > 1:
            if raw_data[0][0] in freq_dict.keys():
                if raw_data[0][0:2] in freq_dict[raw_data[0][0]].keys():
                    freq_dict[raw_data[0][0]][raw_data[0][0:2]][raw_data[0]] = raw_data[1]
                else:
                    freq_dict[raw_data[0][0]][raw_data[0][0:2]] = {raw_data[0]: raw_data[1]}
            else:
                freq_dict[raw_data[0][0]] = {raw_data[0][0:2]: {raw_data[0]: raw_data[1]}}
        if raw_data[0][0] in freq_dict_one.keys():
            freq_dict_one[raw_data[0][0]][raw_data[0]] = raw_data[1]
        else:
            freq_dict_one[raw_data[0][0]] = {raw_data[0]: raw_data[1]}
    return [freq_dict, freq_dict_one], input_data[1]


def suggest_options(input_data):
    dict_trie = input_data[0]
    prefixes = input_data[1]
    suggest_options_dict = {}
    for prefix in prefixes:
        list_of_options = []
        if len(prefix) > 1:
            for letter in dict_trie[0].keys():
                if prefix[0] == letter:
                    for letters in dict_trie[0][letter].keys():
                        if prefix[0:2] == letters:
                            for word, freq in dict_trie[0][letter][letters].items():
                                if prefix == word[:len(prefix)]:
                                    list_of_options.append((word, int(freq)))
        else:
            for letter in dict_trie[1].keys():
                if prefix == letter:
                    for word, freq in dict_trie[1][letter].items():
                        list_of_options.append((word, int(freq)))
        list_of_options.sort(key=lambda word_info: word_info[1], reverse=True)
        suggest_options_dict[prefix] = list_of_options[:10]
    for top_words in suggest_options_dict.values():
        for words in top_words:
            print(words[0], words[1])
        print('\n')


if __name__ == '__main__':
    suggest_options(get_dict_trie(get_input_data()))
    # print(get_input_data())
