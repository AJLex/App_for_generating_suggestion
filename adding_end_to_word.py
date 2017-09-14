import csv
import random


"""
input fils is csv dictionary from link http://dict.ruslang.ru/Freq2011.zip
function reads dictionary and takes column 'Lemma' and 'Doc'
return dict where key is a word from 'Lemma' and value is a freq from 'Doc',
list of prefixes(like 'прив', 'аб', 'эконо') with a different lengths
"""
def get_input_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        fields = ['word', 'PoS', 'Freq', 'R', 'D', 'Doc']
        reader = csv.DictReader(f, fields, delimiter='	')
        rus_freq_dict = {}
        prefixes = []
        for raw in reader:
            raw_data = [raw.get('word').lower(), raw.get('Doc')]
            rus_freq_dict[raw_data[0]] = raw_data[1]
            prefixes.append(raw_data[0][:random.randint(1, len(raw_data[0]))])
    return rus_freq_dict, prefixes[:100]


def suggest_options(input_data):
    suggest_options_dict = {}
    words = []
    for key in input_data[0].keys():
        words.append(key)
    words.sort()
    for prefix in input_data[1]:
        list_of_options = []
        left_limit = 0
        right_limit = len(words)
        middle = int(left_limit/2 + right_limit/2)
        for word_index in range(left_limit, right_limit):
            if words[word_index].startswith(prefix):
                if word_index > middle:
                    left_limit = middle
                else:
                    right_limit = middle
        for index in range(left_limit, right_limit):
            if prefix == words[index][:len(prefix)]:
                list_of_options.append((words[index], input_data[0].get(words[index])))
        suggest_options_dict[prefix] = list_of_options[:10]
    return suggest_options_dict


if __name__ == '__main__':
    print(suggest_options(get_input_data('freqrnc2011.csv')))
    # print(get_input_data('freqrnc2011.csv'))
