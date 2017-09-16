from collections import defaultdict


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
def get_dict_trie(input_data):
    freq_dict = defaultdict(lambda: defaultdict(dict))
    freq_dict_one = defaultdict(dict)
    for raw_data in input_data[0]:
        if len(raw_data[0]) > 1:
            freq_dict[raw_data[0][0]][raw_data[0][:2]][raw_data[0]] = raw_data[1]
        freq_dict_one[raw_data[0][0]][raw_data[0]] = raw_data[1]
    return [freq_dict, freq_dict_one], input_data[1]


# function takes input_data, which contain list of dictionaries and "prefixes" list
# for each prefix from "prefixes" list function searching and then printing
# top 10 most used words and their frequency of repetition
def print_suggest_options(input_data):
    dict_trie = input_data[0]
    prefixes = input_data[1]
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
        for word_info in list_of_options[:10]:
            print(word_info[0])
        print('\n')


if __name__ == '__main__':
    print_suggest_options(get_dict_trie(get_input_data()))
