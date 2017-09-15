import csv
import random


# function append input data to list "limit_index" times
# if input data is prefixes, then varaible "prefix" is True
def append_to_list(limit_index, prefix=False):
    data_list = []
    for index in range(0, limit_index):
        line = input()
        if prefix:
            data_list.append(line.strip())
        else:
            data_list.append(line.strip().split())
    return data_list


# function puts firsr "number_of_words" words into raw_data list
# and next "number_of_prefixes" prefixes puts into prefixes list
def get_input_data():
    number_of_words = int(input())
    raw_data = append_to_list(number_of_words)
    number_of_prefixes = int(input())
    prefixes = append_to_list(number_of_prefixes, prefix=True)
    return raw_data, prefixes


# function takes input_data, which contain "raw_data" list and "prefixes" list
# from the "raw_data" list two dictionaries are created for a word from one letter
# and for a word from several letters
# "prefixes" does not change
def get_dict_trie(input_data):
    freq_dict = {}
    freq_dict_one = {}
    for raw_data in input_data[0]:
        if len(raw_data[0]) > 1:
            if raw_data[0][0] in freq_dict.keys():
                if raw_data[0][0:2] in freq_dict[raw_data[0][0]].keys():
                    freq_dict[raw_data[0][0]][raw_data[0][0:2]][raw_data[0]] = raw_data[1]
            else:
                freq_dict[raw_data[0][0]] = {raw_data[0][0:2]: {raw_data[0]: raw_data[1]}}
        if raw_data[0][0] in freq_dict_one.keys():
            freq_dict_one[raw_data[0][0]][raw_data[0]] = raw_data[1]
        else:
            freq_dict_one[raw_data[0][0]] = {raw_data[0]: raw_data[1]}
    return [freq_dict, freq_dict_one], input_data[1]


# function takes input_data, which contain list of dictionaries and "prefixes" list
# for each prefix from "prefixes" list function searching and then printing
# top 10 most used words and their frequency of repetition
def suggest_options(input_data):
    dict_trie = input_data[0]
    prefixes = input_data[1]
    for prefix in prefixes:
        list_of_options = []
        if len(prefix) > 1:
            for letter in dict_trie[0].keys():
                if prefix[0] == letter:
                    for letters in dict_trie[0][letter].keys():
                        if prefix[0:2] == letters:
                            for word, freq in dict_trie[0][letter][letters].items():
                                if prefix == word[:len(prefix)]:
                                    list_of_options.append((word, int(freq)*-1))
        else:
            for letter in dict_trie[1].keys():
                if prefix == letter:
                    for word, freq in dict_trie[1][letter].items():
                        list_of_options.append((word, int(freq)*-1))
        list_of_options.sort(key=lambda word_info: (word_info[1], word_info[0]))
        if len(list_of_options) > 10:
            for index in range(0, 10):
                print(list_of_options[index][0])
        else:
            for index in range(0, len(list_of_options)):
                print(list_of_options[index][0])
        print('\n')


if __name__ == '__main__':
    suggest_options(get_dict_trie(get_input_data()))
