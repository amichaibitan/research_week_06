from fairpy import fairpy
from two_players_fair_division import *
from typing import List, Any, Dict


Alice = fairpy.agents.AdditiveAgent({'a': 1, 'b': 2, 'c': 3, 'd': 4}, name = 'Alice')
George = fairpy.agents.AdditiveAgent({'a': 4, 'c': 2, 'd': 3, 'b': 1}, name = 'George')

"""
A: a b c d
B: b c d a
"""


def test_restricted_simple():
    assert restricted_simple([Alice, George], ['a', 'b', 'c', 'd']) == \
           "[{'a': ['a', 'd'], 'b': ['b', 'c']}, {'a': ['a', 'c'], 'b': ['b', 'd']}]"


def test_singles_doubles():

    assert sequential([Alice, George], ['a', 'b', 'c', 'd']) == \
           "[{'a': ['a', 'c'], 'b': ['b', 'd']}]"


def test_restricted_simple():
    assert restricted_simple([Alice, George], ['a', 'b', 'c', 'd']) == \
           "[{'a': ['a', 'c'], 'b': ['b', 'd']}]"


def test_singles_doubles():
    assert singles_doubles([Alice, George], ['a', 'b', 'c', 'd']) == \
           "[{'a': ['a', 'c'], 'b': ['d', 'b']}]"


def test_iterated_singles_doubles():
    assert iterated_singles_doubles([Alice, George], ['a', 'b', 'c', 'd']) == \
           "[{'a': ['a', 'c'], 'b': ['d', 'b']}]"


def test_s1():
    assert s1([Alice, George], ['a', 'b', 'c', 'd']) == \
           "[{'a': ['a', 'c'], 'b': ['d', 'b']}]"


def test_l1():
    assert l1([Alice, George], ['a', 'b', 'c', 'd']) == \
           "[{'a': ['a', 'c'], 'b': ['d', 'b']}]"


def test_top_down():
    assert top_down([Alice, George], ['a', 'b', 'c', 'd']) == \
           "[{'a': ['a', 'd'], 'b': ['b', 'c']}]"


def test_top_down_alternating():
    assert top_down_alternating([Alice, George], ['a', 'b', 'c', 'd']) == \
           "[{'a': ['a', 'd'], 'b': ['b', 'c']}]"


def test_bottom_up():
    assert bottom_up([Alice, George], ['a', 'b', 'c', 'd']) == \
           "[{'a': ['a', 'c'], 'b': ['d', 'b']}]"


def test_bottom_up_alternating():
    assert bottom_up_alternating([Alice, George], ['a', 'b', 'c', 'd']) == \
        "[{'a': ['a', 'b'], 'b': ['d', 'c']}]"


def test_trump():
    assert trump([Alice, George], ['a', 'b', 'c', 'd']) == \
        "[{'a': ['a', 'c'], 'b': ['b', 'd']}]"

