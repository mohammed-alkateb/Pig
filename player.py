"""
No imports exists
"""


class Player:
    """
    player class
    """
    def __init__(self, name) -> None:
        """
        constructor contains player name and score
        :param name: player name
        :return: None
        """
        self.name = name
        self.__score = 0

    def increase_score(self, amount) -> None:
        """
        increase score by amount of points
        :param amount: amount points to add
        :return: None
        """
        self.__score += amount

    def reset_score(self) -> None:
        """
        reset the score
        :return: None
        """
        self.__score = 0

    def get_score(self) -> int:
        """
        score getter
        :return: int
        """
        return self.__score
