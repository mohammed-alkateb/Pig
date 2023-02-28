from typing import List

from player import Player
from ui import UI
from dice_hand import Dice_hand
import sys
import os


class Game:
    def __init__(self):
        self.__players: List[Player] = []
        self.ui = UI()
        self.threshold = 0
        self.turn = True
        self.turn_looping = True
        self.__won = False

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
        with open('player_info.txt', 'a') as file:
            file.write(f"{new_player.name},0\n")
            print(f"New player with the name '{new_player.name}' registered")

    def check_player_info(self):
        for player in self.__players:
            with open('player_info.txt', 'r') as file:
                found_player = False
                for line in file:
                    name_in_log = line.rstrip().split(",")[0]
                    if player.name == name_in_log:
                        print(f"{player.name} has been confirmed!")
                        found_player = True
                if not found_player:
                    self.register_new_player(player)

    def update_player_info(self, update_name: bool, current_name, new_name, high_score):
        if update_name:
            with open('player_info.txt', 'r') as file:
                lines = file.readlines()
            for i, line in enumerate(lines):
                if current_name in line:
                    if update_name:
                        lines[i] = line.replace(current_name, new_name)
                        break
                    else:
                        old_score = int(lines[i].rstrip().split(",")[1])
                        if high_score > old_score:
                            lines[i] = line.replace(old_score, high_score)
                            break
            with open('player_info.txt', 'w') as file:
                file.writelines(lines)

    def end_turn(self, dice_hand):
        self.turn = not self.turn
        self.turn_looping = False
        dice_hand.reset_values()

    def detect_winner(self, player):
        if player.get_score() >= self.threshold:
            print(f"The winner is {player.name}")
            self.update_player_info(False, player.name, None, player.get_score())
            sys.exit()

    def match_loop(self, action, dice_hand, player):
        if action == 1:
            cast = dice_hand.get_multiple_cast()
            if cast == 1:
                print("A 1 was rolled\n")
                player.reset_score()
                self.end_turn(dice_hand)
            else:
                print(f"You've got {cast}")
                player.increase_score(cast)
                self.detect_winner(player)
        elif action == 2:
            print(f"{player.name}'s score: {player.get_score()}\n")
            self.end_turn(dice_hand)
        elif action == 3:
            new_name = str(input("Enter the new name: "))
            self.update_player_info(True, player.name, new_name, None, None)
            player.name = new_name
        elif action == 4:
            lambda: os.system('cls')
            self.__players.clear()
            self.game_loop()
        elif action == 5:
            sys.exit()
        else:
            raise Exception("Invalid input!")

    def turn_shift(self, player, dice_hand):
        self.turn_looping = True
        print(f"It's {player.name}'s turn..")
        while self.turn_looping:
            player_action = int(input("1. Roll a die\n"
                                      "2. Hold\n"
                                      "3. Rename player\n"
                                      "4. Restart\n"
                                      "5. Quit\n"))
            self.match_loop(player_action, dice_hand, player)

    def one_to_one(self):
        self.threshold = int(input("Assign a threshold: "))
        while not self.__won:
            if self.turn:
                dice_hand = Dice_hand()
                player = self.__players[0]
                self.turn_shift(player, dice_hand)
            elif not self.turn:
                dice_hand = Dice_hand()
                player = self.__players[1]
                self.turn_shift(player, dice_hand)

    def one_to_machine(self):
        pass

    def begin(self):
        if len(self.__players) > 1:
            self.one_to_one()
        elif len(self.__players) == 1:
            self.one_to_machine()

    def game_loop(self):
        self.matchmaking()
        self.check_player_info()
        self.ui.display_game_rules()
        self.begin()


if __name__ == '__main__':
    main = Game()
    main.game_loop()
