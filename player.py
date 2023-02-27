class Player:
    def __init__(self, name):
        self.name = name
        self.__score = 0

    def increase_score(self, amount):
        self.__score += amount

    def reset_score(self):
        self.__score = 0

    def get_score(self):
        return self.__score
