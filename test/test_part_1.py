import os
from collections import defaultdict


from angrydev_test.part_1 import get_data_from_file, get_dict_trie_like, suggest_options


def test_get_data_from_file():
    path_to_file = os.path.join(__file__, '..', 'test_input.txt')
    assert(get_data_from_file(path_to_file)) == [['kare', '10'],
                                                 ['kanojo', '20'],
                                                 ['karetachi', '1'],
                                                 ['korosu', '7'],
                                                 ['sakura', '3']]


def test_get_dict_trie_like_part_1():
    input_data = [['kare', '10'],
                  ['kanojo', '20'],
                  ['karetachi', '1'],
                  ['korosu', '7'],
                  ['sakura', '3']]
    assert get_dict_trie_like(input_data)[0]['k']['ka'] == {'kare': 10,
                                                            'kanojo': 20,
                                                            'karetachi': 1}
    assert get_dict_trie_like(input_data)[1]['k'] == {'kare': 10,
                                                      'kanojo': 20,
                                                      'karetachi': 1,
                                                      'korosu': 7}


def test_suggest_options():
    input_data = [{'k': {'ko': {'korosu': 7}}}, {'s': {'sakura': 3}}]
    prefixes = []
    max_len = 10
    assert suggest_options(input_data, prefixes, max_len) == []
    prefixes = ['ka']
    assert suggest_options(input_data, prefixes, max_len) == []
    input_data = []
    prefixes = ['ka']
    assert suggest_options(input_data, prefixes, max_len) == []
    input_data = [{'k': {'ko': {'korosu': 7}}}, {'k': {'kare': 10,
                                                       'kanojo': 20,
                                                       'karetachi': 10,
                                                       'korosu': 7}}]
    prefixes = ['ko', 'k']
    assert suggest_options(input_data, prefixes, max_len) ==
    [
        ['ko', [('korosu', -7)]],
        ['k', [('kanojo', -20), ('kare', -10), ('karetachi', -10), ('korosu', -7)]]
    ]
