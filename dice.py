import random


class Dice:

    def __init__(self):
        pass

    def get_dice_cast(self) -> int:
        return random.randint(1, 6)