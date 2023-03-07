
from intelligence import Intelligence

def test_ai_level():
    intelligence = Intelligence(ai_level=1, data_file='dice_values.csv')
    assert intelligence.get_ai_level() == 1

def test_easy_level():
    intelligence = Intelligence(ai_level=1, data_file='dice_values.csv')
    assert intelligence.easy_level() in [0, 1]

def test_hard_level():
    intelligence = Intelligence(ai_level=1, data_file='dice_values.csv')
    assert isinstance(intelligence.hard_level(), int)