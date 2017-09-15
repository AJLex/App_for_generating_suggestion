import csv
import random


"""
input fils is csv dictionary from link http://dict.ruslang.ru/Freq2011.zip
function reads dictionary and takes column 'Lemma' and 'Doc'
return dict where key is a word from 'Lemma' and value is a freq from 'Doc',
list of prefix(like 'прив', 'аб', 'эконо') with a different lengths
"""


def get_input_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        fields = ['word', 'PoS', 'Freq', 'R', 'D', 'Doc']
        reader = csv.DictReader(f, fields, delimiter='	')
        rus_freq_dict = {}
        rus_freq_dict_one = {}
        prefixes = []
        for raw in reader:
            raw_data = [raw.get('word').lower(), raw.get('Doc')]
            if len(raw_data[0]) > 1:
                if raw_data[0][0] in rus_freq_dict.keys():
                    if raw_data[0][0:2] in rus_freq_dict[raw_data[0][0]].keys():
                        rus_freq_dict[raw_data[0][0]][raw_data[0][0:2]][raw_data[0]] = raw_data[1]
                    else:
                        rus_freq_dict[raw_data[0][0]][raw_data[0][0:2]] = {raw_data[0]: raw_data[1]}
                else:
                    rus_freq_dict[raw_data[0][0]] = {raw_data[0][0:2]: {raw_data[0]: raw_data[1]}}
            if raw_data[0][0] in rus_freq_dict_one.keys():
                rus_freq_dict_one[raw_data[0][0]][raw_data[0]] = raw_data[1]
            else:
                rus_freq_dict_one[raw_data[0][0]] = {raw_data[0]: raw_data[1]}
            prefixes.append(raw_data[0][:random.randint(1, len(raw_data[0]))])
    return rus_freq_dict, prefixes[:15000], rus_freq_dict_one


def suggest_options(input_data):
    suggest_options_dict = {}
    for prefix in input_data[1]:
        list_of_options = []
        if len(prefix) > 1:
            for letter in input_data[0].keys():
                if prefix[0] == letter:
                    for letters in input_data[0][letter].keys():
                        if prefix[0:2] == letters:
                            for word, freq in input_data[0][letter][letters].items():
                                if prefix == word[:len(prefix)]:
                                    list_of_options.append((word, int(freq)))
        else:
            for letter in input_data[2].keys():
                if prefix == letter:
                    for word, freq in input_data[2][letter].items():
                        list_of_options.append((word, int(freq)))
        list_of_options.sort(key=lambda word_info: word_info[1], reverse=True)
        suggest_options_dict[prefix] = list_of_options[:10]
    return suggest_options_dict


def seach_right_continuation(suggest_options_dict):
    prefix = input('> ')
    for key, value in suggest_options_dict.items():
        if prefix == key and len(prefix) == len(key):
            value.sort(key=lambda word_info: (word_info[1], word_info[0]), reverse=True)
            for word_info in value:
                print(word_info[0], word_info[1])


if __name__ == '__main__':
    seach_right_continuation(suggest_options(get_input_data('freqrnc2011.csv')))
    print(get_input_data('freqrnc2011.csv')[1][-1])
    # print(suggest_options(get_input_data('freqrnc2011.csv')))
