# pytest
import os
from collections import defaultdict


from angrydev_test.generate_suggestions import SuggestionGenerator


def test_generate_suggestions():
    # test when prefix single letter
    dictionary = [('a', 7), ('b', 8), ('kare', 10), ('kanojo', 20)]
    prefix = 'a'
    test_suggestions_generator = SuggestionGenerator(dictionary)
    assert test_suggestions_generator.generate_suggestions(prefix) == [('a', -7)]
    # test when prefix not a single letter
    prefix = 'ka'
    test_suggestions_generator = SuggestionGenerator(dictionary)
    assert test_suggestions_generator.generate_suggestions(prefix) == [
        ('kanojo', -20), ('kare', -10)]
    # test when incoming prefixes are empty
    prefix = ''
    test_suggestions_generator = SuggestionGenerator(dictionary)
    assert test_suggestions_generator.generate_suggestions(prefix) == []
    # test when incoming dictionary are empty
    dictionary = []
    prefix = 'a'
    test_suggestions_generator = SuggestionGenerator(dictionary)
    assert test_suggestions_generator.generate_suggestions(prefix) == []    
