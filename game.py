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
            file.write(f"{new_player.name},0,0\n")
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

    def update_player_info(self):
        pass

    def end_turn(self, dice_hand):
        self.turn = not self.turn
        self.turn_looping = False
        dice_hand.reset_values()

    def match_loop(self, action, dice_hand, player_index):
        player = self.__players[player_index]
        if action == 1:
            cast = dice_hand.get_multiple_cast()
            if cast == 1:
                print("A 1 was rolled\n")
                player.reset_score()
                self.end_turn(dice_hand)
            else:
                print(f"You've got {cast}")
        elif action == 2:
            player.increase_score(dice_hand.get_total_values())
            print(f"{player.name}'s score: {player.get_score()}\n")
            self.end_turn(dice_hand)
        elif action == 3:
            new_name = str(input("Enter the new name: "))
            player.name = new_name
        elif action == 4:
            lambda: os.system('cls')
            self.__players.clear()
            self.game_loop()
        elif action == 5:
            sys.exit()
        else:
            raise Exception("Invalid input!")

    def turn_shift(self, player_index, dice_hand):
        self.turn_looping = True
        print(f"It's {self.__players[player_index].name}'s turn..")
        while self.turn_looping:
            player_action = int(input("1. Roll a die\n"
                                      "2. Hold\n"
                                      "3. Rename player\n"
                                      "4. Restart\n"
                                      "5. Quit\n"))
            self.match_loop(player_action, dice_hand, player_index)

    def one_to_one(self):
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
