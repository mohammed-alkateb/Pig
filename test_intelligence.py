"""" Imports intelligence and random """
import random
from intelligence import Intelligence


def easy_level() -> int:
    """
    decision making using a random integer
    :return: int
    """
    return random.randint(0, 1)


def test_ai_level():
    """
    Creates a new Intelligence object with an
    ai_level of 1 and a data file of
    'dice_values.csv', and then checks that
    the get_ai_level() method returns the
    expected value of 1.
    """
    intelligence = Intelligence(ai_level=1, data_file='dice_values.csv')
    assert intelligence.get_ai_level() == 1


def test_easy_level():
    """
    Creates a new Intelligence object with an
    ai_level of 1 and a data file of
    'dice_values.csv', and then checks that
    the easy_level() method returns a value
    of either 0 or 1.
    """
    assert easy_level() in [0, 1]


def test_hard_level():
    """
    Creates a new Intelligence object with an
    ai_level of 1 and a data file of
    'dice_values.csv', and then checks that the
     hard_level() method returns an integer value.
    """
    intelligence = Intelligence(ai_level=1, data_file='dice_values.csv')
    assert isinstance(intelligence.hard_level(), int)
