from typing import List


class High_score:
    def __init__(self):
        self.__high_score_list: List[int] = []

    def get_high_scores(self) -> int:
        for score in self.__high_score_list:
            return score

    def add_high_score(self, high_score: int) -> bool:
        if not self.__high_score_list or high_score > max(self.__high_score_list):
            self.__high_score_list.append(high_score)
            return True
        return False
