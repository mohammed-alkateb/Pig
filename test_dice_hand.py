from dice import Dice
from dice_hand import Dice_hand

def test_get_total_values():
    dice_hand = Dice_hand()
    assert dice_hand.get_total_values() == 0

def test_get_multiple_cast():
    dice_hand = Dice_hand()
    cast = dice_hand.get_multiple_cast()
    assert cast in [1, 2, 3, 4, 5, 6]

def test_reset_values():
    dice_hand = Dice_hand()
    dice_hand.reset_values()
    assert dice_hand.get_total_values() == 0