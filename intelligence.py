"""
import random, Tuple, numpy, and RandomForestRegressor
"""
import random
from typing import Tuple

import numpy as np
from sklearn.ensemble import RandomForestRegressor


def load_data(filename) -> Tuple[np.ndarray, np.ndarray]:
    """
    load data from the file and return it as numpy arrays
    :param filename: the name of the file to load
    :return: numpy arrays -> x and y
    """
    data = np.loadtxt(filename, delimiter=',')
    arr_x = data.reshape(-1, 1)
    arr_y = data

    return arr_x, arr_y


def easy_level() -> int:
    """
    decision making using a random integer
    :return: int
    """
    return random.randint(0, 1)


class Intelligence:
    """
    This class handle the functionality of
    machine's intelligence during the gameplay
    """
    def __init__(self, ai_level, data_file) -> None:
        """
        constructor with variables random_action, x, y,
        model, DATA_FILE, ai_level.
        Gets the data from the file and make the module train on them
        :param ai_level: the level of machine's intelligence
        that the player wants to play against
        :param data_file: the name of the data file
        """
        self.arr_x, self.arr_y = load_data(data_file)
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.model.fit(self.arr_x, self.arr_y)
        self.DATA_FILE = data_file

        if ai_level <= 1:
            self.ai_level = ai_level
        else:
            self.ai_level = 0

    def get_ai_level(self) -> int:
        """
        ai_level getter
        :return: int
        """
        return self.ai_level

    def ai_action(self) -> int:
        """
        returns machine's made decision/choice
        :return:
        """
        if self.ai_level == 0:
            return easy_level()
        if self.ai_level == 1:
            return self.hard_level()

    def hard_level(self) -> int:
        """
        predict the next dice cast value using the trained module
        :return: int
        """
        x_test = np.random.randint(1, 6, size=(1, 1))
        predicted_value = round(self.model.predict(x_test)[0])

        print(f"Predicted value: {predicted_value}")
        return predicted_value
