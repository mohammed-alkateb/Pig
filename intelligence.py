import random
import numpy as np
from sklearn.ensemble import RandomForestRegressor


class Intelligence:
    def __init__(self, ai_level, data_file):
        self.__random_action = random.randint(0,1)
        self.X, self.y = self.load_data(data_file)
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.model.fit(self.X, self.y)
        self.DATA_FILE = data_file

        if ai_level <= 1:
            self.ai_level = ai_level
        else:
            self.ai_level = 0

    def load_data(self, filename):
        data = np.loadtxt(filename, delimiter=',')
        X = data.reshape(-1, 1)
        y = data

        return X, y

    def get_ai_level(self):
        return self.ai_level

    def ai_action(self):
        if self.ai_level == 0:
            return self.easy_level()
        elif self.ai_level == 1:
            return self.hard_level()

    def easy_level(self):
        return self.__random_action

    def hard_level(self):
        x_test = np.random.randint(1, 7, size=(1, 1))
        predicted_value = round(self.model.predict(x_test)[0])

        print(f"Predicted value: {predicted_value}")
        return predicted_value
