from typing import List
from dice import Dice


class Dice_hand:
    def __init__(self):
        self.__dice_object = Dice()
        self.__dice_values: List[int] = []
        self.__total_values = 0

    def get_multiple_cast(self) -> int:
        cast = self.__dice_object.get_dice_cast()
        if cast == 1:
            self.__dice_values.clear()
            self.__total_values = 0
        else:
            self.__dice_values.append(cast)
            self.__total_values += cast
        return cast

