""" Imports dice """
from dice import Dice


def test_dice_init():
    # Test that creating a new Dice object with default constructor works
    dice = Dice()
    assert isinstance(dice, Dice)


def test_get_dice_cast_valid():
    # Test that get_dice_cast method returns a value between 1 and 6 (inclusive)
    dice = Dice()
    cast = dice.get_dice_cast()
    assert isinstance(cast, int)
    assert 1 <= cast <= 6

<<<<<<< HEAD
=======

def test_dice_constructor():
    # Test that the constructor does not raise an error
    try:
        dice = Dice()
    except Exception as e:
        assert False, f"Creating a Dice object raised an exception: {e}"
>>>>>>> 8d0d4f78923d7c39553fbbc7a00afe84eb650d07


