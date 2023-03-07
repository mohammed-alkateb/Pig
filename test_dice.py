""" Imports dice """
from dice import Dice

def test_get_dice_cast():
    """
        This function creates a new Dice object, calls the get_dice_cast method, and then
        checks that the resulting cast value is between 1 and 6.
        """
    dice = Dice()
    cast = dice.get_dice_cast()
    assert 1 <= cast <= 6

def test_init():
    """
        This function creates a new Dice object using the default constructor, and then
        checks that the resulting object is an instance of the Dice class.
        """
    dice = Dice()
    assert isinstance(dice, Dice)