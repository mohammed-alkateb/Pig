""" Imports dice """
from dice import Dice


def test_dice_init():
    """
    Test that creating a new Dice object
    with default constructor works
    :return: None
    """
    dice = Dice()
    assert isinstance(dice, Dice)


def test_get_dice_cast_valid():
    """
    Test that get_dice_cast method returns
    a value between 1 and 6 (inclusive)
    :return: None
    """
    dice = Dice()
    cast = dice.get_dice_cast()
    assert isinstance(cast, int)
    assert 1 <= cast <= 6
