# pytest
import random
import time
from collections import defaultdict


from angrydev_test.generate_suggestions import SuggestionGenerator


def test_generate_suggestions():
    # test when prefix single letter
    dictionary = [('a', 7), ('b', 8), ('k', 50),
                  ('kare', 20), ('kanojo', 20), ('korosu', 7)]
    test_suggestions_generator = SuggestionGenerator(dictionary)
    assert test_suggestions_generator.generate_suggestions('k') == [
        ('k', -50), ('kanojo', -20),
        ('kare', -20), ('korosu', -7)]
    # test when prefix not a single letter
    assert test_suggestions_generator.generate_suggestions('ka') == [
        ('kanojo', -20), ('kare', -20)]
    # test when incoming prefixes are empty
    assert test_suggestions_generator.generate_suggestions('') == [
        ('k', -50), ('kanojo', -20), ('kare', -20), ('b', -8), ('a', -7),
        ('korosu', -7)]
    # test when incoming dictionary are empty
    test_suggestions_generator = SuggestionGenerator([])
    assert test_suggestions_generator.generate_suggestions('a') == []


def test_generate_suggestions_stress_test():
    dictionary = []
    prefixes = []
    for index in range(0, 50000):
        rand_word = ''
        for length in range(1, random.randint(2, 10)):
            rand_word += random.choice('asdfgqwertyui')
        dictionary.append((rand_word, random.randint(1, 10000)))
    for index in range(0, 15000):
        word_index = random.randint(0, 49999)
        rand_word = dictionary[word_index][0]
        prefix = rand_word[:random.randint(1, len(rand_word))]
        prefixes.append(prefix)
    start_time = time.time()
    suggestions_generator = SuggestionGenerator(dictionary)
    for prefix in prefixes:
        suggestions_generator.generate_suggestions(prefix)
    assert time.time() - start_time < 5
