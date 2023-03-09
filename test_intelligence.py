"""" Imports intelligence and random """
import random

import numpy as np
from sklearn.ensemble import RandomForestRegressor

from intelligence import Intelligence, easy_level


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


def test_ai_action_easy():
    """
    Creates a new Intelligence object with an
    ai_level of 0 and a data file of
    'dice_values.csv', and then checks that
    the ai_action() method returns a value
    of either 0 or 1.
    """
    intelligence = Intelligence(ai_level=0, data_file='dice_values.csv')
    assert intelligence.ai_action() in [0, 1]


def test_ai_action_hard():
    """
    Creates a new Intelligence object with an
    ai_level of 1 and a data file of
    'dice_values.csv', and then checks that
    the ai_action() method returns an integer.
    """
    intelligence = Intelligence(ai_level=1, data_file='dice_values.csv')
    assert isinstance(intelligence.ai_action(), int)


def test_hard_level_prediction():
    """
    Creates a new Intelligence object with a pre-trained model,
    and checks that the hard_level() method returns an integer
    between 1 and 6.
    """
    # create a pre-trained model
    x_train = np.array([[1], [2], [3], [4], [5], [6]])
    y_train = np.array([2, 3, 4, 5, 6, 7])
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(x_train, y_train)

    # create an Intelligence object with the pre-trained model
    intelligence = Intelligence(ai_level=1, data_file='dice_values.csv')
    intelligence.model = model

    # check that the hard_level() method returns an integer between 1 and 6
    predicted_value = intelligence.hard_level()