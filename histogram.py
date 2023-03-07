"""
import list and matplotlib.pyplot
"""
from typing import List
import matplotlib.pyplot as plt


class Histogram:
    """
    Contains the data of the dice rolls
    over the match time
    """
    def __init__(self) -> None:
        """
        constructor with instance variable data
        :return: None
        """
        self.__data = [0] * 7

    def get_data(self) -> List[int]:
        """
        data getter
        :return: int
        """
        return self.__data

    def update(self, value) -> None:
        """
        update the data list with index -> value
        :param: the data value we want to update
        :return: None
        """
        self.__data[value] += 1

    def reset(self) -> None:
        """
        reset the histogram data
        :return: None
        """
        self.__data.clear()

    def display(self):
        """
        Display the histogram
        :return: None
        """
        data = self.get_data()
        labels = [str(i) for i in range(1, 7)]
        plt.bar(labels, data[1:7], align='center')
        plt.title('Histogram of Single Dice Rolls')
        plt.xlabel('Dice Value')
        plt.ylabel('Frequency')
        plt.show()
