from typing import List
import matplotlib.pyplot as plt


class Histogram:
    def __init__(self):
        self.__data = [0] * 7

    def get_data(self) -> List[int]:
        return self.__data

    def update(self, value):
        self.__data[value] += 1

    def reset(self):
        self.__data.clear()

    def display(self):
        data = self.get_data()
        labels = [str(i) for i in range(1, 7)]
        plt.bar(labels, data[1:7], align='center')
        plt.title('Histogram of Single Dice Rolls')
        plt.xlabel('Dice Value')
        plt.ylabel('Frequency')
        plt.show()