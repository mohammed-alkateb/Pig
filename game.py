from typing import List

from player import Player
from ui import UI
from dice_hand import Dice_hand
from high_score import High_score
from histogram import Histogram
import sys
import os


class Game:
    def __init__(self):
        self.__players: List[Player] = []
        self.__high_score_list: List[High_score] = [High_score() for i in range(2)]
        self.__histograms: List[Histogram] = [Histogram() for i in range(2)]
        self.ui = UI()
        self.threshold = 0
        self.turn = True
        self.turn_looping = True
        self.__won = False
        self.FILE_NAME = "player_info.txt"

    def matchmaking(self):
        while True:
            try:
                action = int(input("How many players would like to play? (max 2)\n"))
                if action in range(1,3):
                    for i in range(action):
                        player = Player(str(input(f"Enter player {i+1} name: ").lower()))
                        self.__players.append(player)
                    break
                else:
                    raise Exception("Out of range")
            except ValueError:
                print("Invalid input. Please enter a valid value.")

    def register_new_player(self, new_player):
        with open(self.FILE_NAME, 'a') as file:
            file.write(f"{new_player.name},0,0,0,0\n")
            print(f"New player with the name '{new_player.name}' registered")

    def check_player_info(self):
        for player in self.__players:
            with open(self.FILE_NAME, 'r') as file:
                found_player = False
                for line in file:
                    name_in_log = line.rstrip().split(",")[0]
                    if player.name == name_in_log:
                        print(f"{player.name} has been confirmed!")
                        found_player = True
                if not found_player:
                    self.register_new_player(player)

    def update_player_info(self, update_name, current_name, new_name, high_score, loser_name):
        with open(self.FILE_NAME, 'r') as file:
            lines = file.readlines()
        if not update_name:
            self.ui.display_info()
        for i, line in enumerate(lines):
            fields = line.rstrip().split(",")
            name = fields[0]
            matches_played = fields[1]
            total_wins = fields[2]
            total_losses = fields[3]
            old_high_score = fields[4]

            if current_name == name:
                if update_name:
                    lines[i] = f"{new_name},{matches_played},{total_wins}," \
                               f"{total_losses},{old_high_score}\n"
                else:
                    if high_score > int(old_high_score):
                        lines[i] = f"{name},{str(int(matches_played) + 1)},{str(int(total_wins) + 1)}," \
                                   f"{total_losses},{high_score}\n"
                    else:
                        lines[i] = f"{name},{str(int(matches_played) + 1)},{str(int(total_wins) + 1)}," \
                                   f"{total_losses},{old_high_score}\n"
                    print(lines[i], end="")
            elif loser_name == name and not update_name:
                lines[i] = f"{name},{str(int(matches_played) + 1)},{total_wins}," \
                           f"{str(int(total_losses) + 1)},{old_high_score}\n"
                print(lines[i], end="")
        with open(self.FILE_NAME, 'w') as file:
            file.writelines(lines)

    def end_turn(self, dice_hand):
        self.turn = not self.turn
        self.turn_looping = False
        dice_hand.reset_values()

    def detect_winner(self, player_index):
        winner = self.__players[player_index]
        global loser
        if player_index % 2 == 0:
            loser = self.__players[1]
        else:
            loser = self.__players[0]
        if winner.get_score() >= self.threshold:
            print(f"The winner is {winner.name}")
            self.__high_score_list[player_index].add_high_score(winner.get_score())
            print("Winner high score list: " + self.__high_score_list[player_index].get_high_scores())
            self.update_player_info(False, winner.name, None, winner.get_score(), loser.name)
            sys.exit()

    def match_loop(self, action, dice_hand, player_index, histogram):
        player = self.__players[player_index]
        if action == 1:
            cast = dice_hand.get_multiple_cast()
            if cast == 1:
                print("A 1 was rolled\n")
                player.reset_score()
                self.end_turn(dice_hand)
            else:
                print(f"You've got {cast}")
                player.increase_score(cast)
                histogram.update(cast)
                self.detect_winner(player_index)
        elif action == 2:
            print(f"{player.name}'s score: {player.get_score()}\n")
            self.end_turn(dice_hand)
        elif action == 3:
            new_name = str(input("Enter the new name: "))
            self.update_player_info(True, player.name, new_name, None)
            player.name = new_name
        elif action == 4:
            histogram.display()
        elif action == 5:
            lambda: os.system('cls')
            self.__players.clear()
            self.game_loop()
        elif action == 6:
            sys.exit()
        else:
            raise Exception("Invalid input!")

    def turn_shift(self, player_index, dice_hand):
        histogram = self.__histograms[player_index]
        self.turn_looping = True
        print(f"It's {self.__players[player_index].name}'s turn..")
        while self.turn_looping:
            player_action = int(input("1. Roll a die\n"
                                      "2. Hold\n"
                                      "3. Rename player\n"
                                      "4. Display Histogram\n"
                                      "5. Restart\n"
                                      "6. Quit\n"))
            self.match_loop(player_action, dice_hand, player_index, histogram)

    def one_vs_one(self):
        self.threshold = int(input("Assign a threshold: "))
        while not self.__won:
            if self.turn:
                dice_hand = Dice_hand()
                player_index = 0
                self.turn_shift(player_index, dice_hand)
            elif not self.turn:
                dice_hand = Dice_hand()
                player_index = 1
                self.turn_shift(player_index, dice_hand)

    def vs_machine(self, level):
        if level == 0:
            pass
        if level == 1:
            pass

    def begin(self):
        if len(self.__players) > 1:
            self.one_vs_one()
        elif len(self.__players) == 1:
            while True:
                level = int(input("Easy level: 0\nHard level: 1\n"))
                if level == 0 or level == 1:
                    break
            self.vs_machine(level)

    def game_loop(self):
        self.matchmaking()
        self.check_player_info()
        self.ui.display_game_rules()
        self.begin()


if __name__ == '__main__':
    main = Game()
    main.game_loop()
