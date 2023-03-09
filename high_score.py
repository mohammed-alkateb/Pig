"""
Import list
"""
from typing import List


class High_score:
    """
    It keeps track of the highscores of
    the players along their matches
    """

    def __init__(self):
        """
        constructor with high_score_list
        """
        self.__high_score_list: List[int] = []

    def get_high_scores(self) -> int:
        """
        highscore list getter
        :return: int
        """
        for score in self.__high_score_list:
            return score

    def add_high_score(self, high_score: int) -> bool:
        """
        add new high score to the list
        :param high_score: high score
        :return: bool
        """
        if not self.__high_score_list or \
                high_score > max(self.__high_score_list):
            self.__high_score_list.append(high_score)
            return True
        return False
