
"""" Imports dice_hand """
from dice_hand import Dice_hand


def test_get_total_values():
    """
    This function creates a new Dice_hand
    object, calls the get_total_values method,
    and then checks that the resulting value is 0.
    """
    dice_hand = Dice_hand()
    assert dice_hand.get_total_values() == 0


def test_get_multiple_cast():
    """
    This function creates a new Dice_hand
    object, calls the get_multiple_cast method multiple times,
    and then checks that the resulting cast
    value is between 1 and 6.
    """
    dice_hand = Dice_hand()
    for i in range(10):  # call get_multiple_cast 10 times
        cast = dice_hand.get_multiple_cast()
        assert cast in [1, 2, 3, 4, 5, 6]

def test_reset_values():
    """
    This function creates a new Dice_hand
    object, calls the reset_values method,
    and then checks that the resulting value
    returned by get_total_values is 0.
    """
    dice_hand = Dice_hand()
    dice_hand.reset_values()
    assert dice_hand.get_total_values() == 0

