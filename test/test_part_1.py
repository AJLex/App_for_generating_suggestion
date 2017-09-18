# pytest
import os
from collections import defaultdict


from angrydev_test.part_1 import suggest_options



def test_suggest_options():
    # test when incoming prefixes are empty
    input_data = [{'k': {'ko': {'korosu': 7}}}, {'s': {'sakura': 3}}]
    prefixes = []
    max_len = 10
    dict_def = defaultdict(list)
    assert suggest_options(input_data, prefixes, max_len) == {'s': {'sakura': 3}}
    #
    # prefixes = ['ka']
    # assert suggest_options(input_data, prefixes, max_len) == dict_def[prefixes[0]]
    # test when dictionary is empty
    # input_data = []
    # prefixes = ['ka']
    # assert suggest_options(input_data, prefixes, max_len) == dict_def
    # input_data = [{'k': {'ko': {'korosu': 7}}}, {'k': {'kare': 10,
    #                                                    'kanojo': 20,
    #                                                    'karetachi': 10,
    #                                                    'korosu': 7}}]
    prefixes = ['ko', 'a']
    input_data = [{'k':{'a':{'kanojo': -20, 'kare': -10, 'karetachi': -1},
                   'o': {'korosu': -7}}, 's':{'a':{'sakura': -3}}},
                   {'a': [('aba', -10), ('a', -7)]}]
    assert suggest_options(input_data, prefixes, max_len) == {
        'ko': [('korosu', -7)],
        'a': [('aba', -10), ('a', -7)]
    }
