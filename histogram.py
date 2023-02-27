from typing import List


class Histogram:
    def __init__(self):
        self.__data = [0] * 13

    def get_data(self) -> List[int]:
        return self.__data

    def update(self, value):
        self.__data[value] += 1

