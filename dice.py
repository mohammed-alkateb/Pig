"""" import random from the standard library """
import random


class Dice:
    """
    A class that represents a standard six-sided dice.
    """

    def __init__(self):
        """
        constructor
        """
        pass

    def get_dice_cast(self) -> int:
        """
        returns random number between 1 and 6
        """
        return random.randint(1, 6)
