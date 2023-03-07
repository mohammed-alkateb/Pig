
from intelligence import Intelligence

def test_ai_level():
    intelligence = Intelligence(ai_level=0, data_file='data.txt')
    assert intelligence.get_ai_level() == 0

def test_easy_level():
    intelligence = Intelligence(ai_level=0, data_file='data.txt')
    assert intelligence.easy_level() in [0, 1]

def test_hard_level():
    intelligence = Intelligence(ai_level=1, data_file='data.txt')
    assert isinstance(intelligence.hard_level(), int)