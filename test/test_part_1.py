# pytest
import os
from collections import defaultdict


from angrydev_test.part_1 import get_data_from_file, get_freq_dicts, suggest_options


def test_get_freq_dicts():
    input_data = [['kare', '10'],
                  ['kanojo', '20'],
                  ['karetachi', '1'],
                  ['korosu', '7'],
                  ['sakura', '3']]
    assert get_freq_dicts(input_data)[0]['k']['a'] == {'kare': -10,
                                                       'kanojo': -20,
                                                       'karetachi': -1}
    assert get_freq_dicts(input_data)[1]['k'] == [('kanojo', -20),
                                                  ('kare', -10),
                                                  ('korosu', -7),
                                                  ('karetachi', -1)]


def test_suggest_options():
    input_data = [{'k': {'ko': {'korosu': 7}}}, {'s': {'sakura': 3}}]
    prefixes = []
    max_len = 10
    dict_def = defaultdict(list)
    assert suggest_options(input_data, prefixes, max_len) == {'s': {'sakura': 3}}
    # prefixes = ['ka']
    # assert suggest_options(input_data, prefixes, max_len) == dict_def[prefixes[0]]
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
