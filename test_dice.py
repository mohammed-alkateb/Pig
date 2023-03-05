from dice import Dice

def test_get_dice_cast():
    dice = Dice()
    cast = dice.get_dice_cast()
    assert 1 <= cast <= 6

def test_init():
    dice = Dice()
    assert isinstance(dice, Dice)