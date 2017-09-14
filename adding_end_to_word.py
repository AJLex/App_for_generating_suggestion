import csv
import random


"""
input fils is csv dictionary from link http://dict.ruslang.ru/Freq2011.zip
function reads dictionary and takes column 'Lemma' and 'Doc'
return dict where key is a word from 'Lemma' and value is a freq from 'Doc',
list of words beginning(like 'прив', 'аб', 'эконо') with a different lengths
"""
def get_input_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        fields = ['word', 'PoS', 'Freq', 'R', 'D', 'Doc']
        reader = csv.DictReader(f, fields, delimiter='	')
        rus_freq_dict = {}
        words_beginning = []
        for raw in reader:
            raw_data = [raw.get('word').lower(), raw.get('Doc')]
            if raw_data[0][0] in rus_freq_dict.keys():
                rus_freq_dict[raw_data[0][0]][raw_data[0]] =  raw_data[1]
            else:
                rus_freq_dict[raw_data[0][0]] = {raw_data[0]: raw_data[1]}
            words_beginning.append(raw_data[0][:random.randint(1, len(raw_data[0]))])
    return rus_freq_dict, words_beginning[:10000]


def suggest_options(input_data):
    suggest_options_dict = {}
    count = 0
    for words_beginning in input_data[1]:
        count += 1
        print(count, len(input_data[1]))
        list_of_options = []
        for letter in input_data[0].keys():
            if words_beginning[0] == letter:
                for word, freq in input_data[0][letter].items():
                    if words_beginning == word[:len(words_beginning)]:
                        list_of_options.append((word, freq))
        list_of_options.sort(key=lambda word_info: word_info[1], reverse=True)
        suggest_options_dict[words_beginning] = list_of_options[:10]
    return suggest_options_dict


if __name__ == '__main__':
    print(suggest_options(get_input_data('freqrnc2011.csv')))
    # for letter, word_info in get_input_data('freqrnc2011.csv')[0].items():
    #     print(letter, word_info)
