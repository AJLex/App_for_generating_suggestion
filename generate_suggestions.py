from collections import defaultdict


# Function reads a file from given path, format: see get_input_data(),
# and returns dictionary and list of prefixes
def get_input_data_from_file(path_to_file):
    dictionary = []
    with open(path_to_file, 'r', encoding='utf-8') as f:
            for line in f:
                items = line.strip().split()
                if len(items) > 1:
                    dictionary.append((items[0], int(items[1])))
    return dictionary


# function reads input data from stdin,
# in following format:
# N - number of words
# word freq
# ...
# N lines
# ...
# M - number of prefixes
# prefix
# ...
# M lines
# ...
# and returns dictionary and list of prefixes
def get_input_data():
    dictionary = []
    prefixes = []
    number_of_words = int(input())
    for index in range(number_of_words):
        line = input()
        items = line.strip().split()
        dictionary.append((items[0], int(items[1])))
    number_of_prefixes = int(input())
    for index in range(number_of_prefixes):
        line = input()
        prefixes.append(line.strip())
    return dictionary, prefixes


#
class SuggestionGenerator():
    """
    SuggestionGenerator suggests a top 10 most used word for incoming prefix.
    """
    def __init__(self, dictionary, max_len=10):
        self.shards = defaultdict(lambda: defaultdict(dict))
        self.cache = defaultdict(list)
        for word, freq in dictionary:
            if len(word) > 1:
                # "-freq" is necessary for correct sort
                # first by freq in descending order then by lexicographical order
                self.shards[word[0]][word[1:2]][word] = -freq
            self.cache[word[0]].append((word, -freq))
        for single_letter_word, word_info in self.cache.items():
            word_info.sort(key=lambda word_info: (word_info[1], word_info[0]))
            self.cache[single_letter_word] = word_info[:max_len]
        top_overall = []
        for single_letter_word, word_info in self.cache.items():
            top_overall.extend(word_info)
        top_overall.sort(key=lambda word_info: (word_info[1], word_info[0]))
        self.cache[''] = top_overall[:10]

    def generate_suggestions(self, prefix, max_len=10):
        # there is no need to seek if prefix already in dict
        if prefix in self.cache:
            return self.cache[prefix]
        suggestions = []
        if prefix[:1] not in self.shards or \
           prefix[1:2] not in self.shards[prefix[:1]]:
            return []
        for word, freq in self.shards[prefix[:1]][prefix[1:2]].items():
            if word.startswith(prefix):
                suggestions.append((word, freq))
        suggestions.sort(key=lambda word_info: (word_info[1], word_info[0]))
        self.cache[prefix] = suggestions[:max_len]
        return self.cache[prefix]


if __name__ == '__main__':
    dictionary, prefixes = get_input_data()
    suggestions_generator = SuggestionGenerator(dictionary)
    for prefix in prefixes:
        for word_info in suggestions_generator.generate_suggestions(prefix):
                print(word_info[0])
        print('')
