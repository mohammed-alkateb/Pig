"""" import list, dice """
from typing import List
from dice import Dice


class Dice_hand:
    """
    This class represents the dice hand of the player
    It contains a dice object to roll dice, dice
    values, and the total of these values
    """
    def __init__(self):
        """
        constructor that contain class instance variables
        dice_object, dice_values, and total_values
        """
        self.__dice_object = Dice()
        self.__dice_values: List[int] = []
        self.__total_values = 0

    def get_total_values(self):
        """
        :return: dice hand total_values
        """
        return self.__total_values

    def get_multiple_cast(self) -> int:
        """
        get dice cast and reset the values if the
        cast equal to 1. otherwise, add the cast
        value to the dice hand and increase total values
        :return: cast
        """
        cast = self.__dice_object.get_dice_cast()
        if cast == 1:
            self.__dice_values.clear()
            self.__total_values = 0
        else:
            self.__dice_values.append(cast)
            self.__total_values += cast
        return cast

    def reset_values(self):
        """
        reset dice_hand
        """
        self.__dice_values: List[int] = []
        self.__total_values = 0
