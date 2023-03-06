from typing import List

from player import Player
from ui import UI
from dice_hand import Dice_hand
from high_score import High_score
from histogram import Histogram
from intelligence import Intelligence
import sys
import os
import csv


class Game:
    def __init__(self):
        self.players: List[Player] = []
        self.high_score_list: List[High_score] = [High_score() for i in range(2)]
        self.histograms: List[Histogram] = [Histogram() for i in range(2)]
        self.__intelligence = None
        self.ui = UI()
        self.threshold = 0
        self.turn = True
        self.turn_looping = True
        self.__won = False
        self.GAME_LOG_FILE = "player_info.txt"
        self.DATA_FILE = "dice_values.csv"

    def matchmaking(self):
        while True:
            action = int(input("How many players would like to play? (max 2)\n"))
            if action in range(1, 3):
                for i in range(action):
                    while True:
                        name = str(input(f"Enter player {i + 1} name: ").lower())
                        if name.isalpha():
                            player = Player(name)
                            self.players.append(player)
                            break
                        else:
                            print("The name should contain only alphabet!\n")
                break
            else:
                print("Out of range\n")

    def register_new_player(self, player):
        with open(self.GAME_LOG_FILE, 'a') as file:
            file.write(f"{player.name},0,0,0,0\n")
            print(f"New player with the name '{player.name}' registered")

    def check_player_info(self):
        for player in self.players:
            with open(self.GAME_LOG_FILE, 'r') as file:
                player_found = False
                for line in file:
                    name_in_log = line.rstrip().split(",")[0]
                    if player.name == name_in_log:
                        print(f"{player.name} has been confirmed!")
                        player_found = True
                if not player_found:
                    self.register_new_player(player)

    def update_player_info(self, update_name, current_name, new_name, high_score, loser_name):
        with open(self.GAME_LOG_FILE, 'r') as file:
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
                    lines[i] = f"{str(new_name)},{matches_played},{total_wins}," \
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
        with open(self.GAME_LOG_FILE, 'w') as file:
            file.writelines(lines)

    def end_turn(self, dice_hand):
        self.turn = not self.turn
        self.turn_looping = False
        dice_hand.reset_values()

    def exit_confirmation(self):
        play_again = input("Do you want to play again? [YES/NO]\n").lower()
        while True:
            if play_again == "yes":
                self.restart_match()
                break
            elif play_again == "no":
                sys.exit()
                break
            else:
                print("Invalid input")

    def detect_winner(self, player_index):
        winner = self.players[player_index]
        loser = self.players[(player_index+1) % 2]

        if winner.get_score() >= self.threshold:
            print(f"The winner is {winner.name}")
            self.high_score_list[player_index].add_high_score(winner.get_score())
            print(f"Winner high score list: {self.high_score_list[player_index].get_high_scores()}")
            self.update_player_info(False, winner.name, None, winner.get_score(), loser.name)
            self.exit_confirmation()

    def check_cast(self, histogram, player_index, dice_hand):
        player = self.players[player_index]
        cast = dice_hand.get_multiple_cast()

        with open(self.DATA_FILE, mode='a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([cast])
        if cast == 1:
            print("A 1 was rolled\n")
            player.reset_score()
            self.end_turn(dice_hand)
        else:
            print(f"{player.name} have got {cast}")
            player.increase_score(cast)
            histogram.update(cast)
            self.detect_winner(player_index)

    def restart_match(self):
        for player in self.players:
            player.reset_score()
        if self.__intelligence is None:
            self.one_vs_one()
        else:
            self.one_vs_machine()

    def match_loop(self, player_action, dice_hand, player_index, histogram):
        player = self.players[player_index]
        action = int(player_action)
        if action == 1:
            self.check_cast(histogram, player_index, dice_hand)
        elif action == 2:
            print(f"{player.name}'s score: {player.get_score()}\n")
            self.end_turn(dice_hand)
        elif action == 3:
            while True:
                new_name = input("Enter the new name: ")
                if new_name.isalpha():
                    self.update_player_info(True, player.name, new_name.lower(), None, None)
                    break
                else:
                    print("The name should contain only alphabet!\n")
            player.name = new_name
        elif action == 4:
            histogram.display()
        elif action == 5:
            lambda: os.system('cls')
            self.restart_match()
        elif action == 6:
            sys.exit()

    def turn_shift(self, player_index, dice_hand):
        histogram = self.histograms[player_index]
        self.turn_looping = True
        print(f"It's {self.players[player_index].name}'s turn..")
        while self.turn_looping:
            while True:
                player_action = input("1. Roll a die\n"
                                          "2. Hold\n"
                                          "3. Rename player\n"
                                          "4. Display Histogram\n"
                                          "5. Restart\n"
                                          "6. Quit\n")
                if player_action.isdigit() and int(player_action) in range(1, 7):
                    break
                else:
                    print("It should contain only digits [1-6]\n")
            self.match_loop(player_action, dice_hand, player_index, histogram)

    def machine_turn(self, player_index, dice_hand):
        histogram = self.histograms[1]
        player = self.players[player_index]
        self.turn_looping = True
        print(f"It's machine's turn..")
        while self.turn_looping:
            ai_level = self.__intelligence.get_ai_level()
            ai_action = self.__intelligence.ai_action()
            if ai_level == 0:
                if ai_action == 0:
                    self.check_cast(histogram, player_index, dice_hand)
                elif ai_action == 1:
                    print(f"{player.name}'s score: {player.get_score()}\n")
                    self.end_turn(dice_hand)
            elif ai_level == 1:
                if ai_action != 1:
                    self.check_cast(histogram, player_index, dice_hand)
                else:
                    print(f"{player.name}'s score: {player.get_score()}\n")
                    self.end_turn(dice_hand)

    def select_threshold(self):
        while True:
            self.threshold = input("Assign a threshold: ")
            if self.threshold.isdigit():
                self.threshold = int(self.threshold)
                break
            else:
                print("It should contain only digits\n")

    def one_vs_one(self):
        self.select_threshold()
        while not self.__won:
            if self.turn:
                dice_hand = Dice_hand()
                player_index = 0
                self.turn_shift(player_index, dice_hand)
            elif not self.turn:
                dice_hand = Dice_hand()
                player_index = 1
                self.turn_shift(player_index, dice_hand)

    def one_vs_machine(self):
        self.select_threshold()
        player = Player("Machine")
        self.players.append(player)
        while not self.__won:
            if self.turn:
                dice_hand = Dice_hand()
                player_index = 0
                self.turn_shift(player_index, dice_hand)
            elif not self.turn:
                dice_hand = Dice_hand()
                player_index = 1
                self.players[player_index].name = "Machine"
                self.machine_turn(player_index, dice_hand)

    def begin(self):
        if len(self.players) > 1:
            self.one_vs_one()
        elif len(self.players) == 1:
            while True:
                level = int(input("Easy level: 0\nHard level: 1\n"))
                self.__intelligence = Intelligence(level, self.DATA_FILE)
                self.one_vs_machine()
                break

    def game_loop(self):
        self.matchmaking()
        self.check_player_info()
        self.ui.display_game_rules()
        self.begin()


if __name__ == '__main__':
    main = Game()
    main.game_loop()
