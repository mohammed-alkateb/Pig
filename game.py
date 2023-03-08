"""
import List, Player, UI, Dice_hand, High_score,
Histogram, Intelligence, sys, and csv
"""
import sys
import csv
import time
from typing import List
from player import Player
from ui import UI
from dice_hand import Dice_hand
from high_score import High_score
from histogram import Histogram
from intelligence import Intelligence
from rich.progress import track


def progress_bar() -> None:
    """
    Game loading Progress bar
    :return: None
    """
    for i in track(range(10), description="Processing..."):
        print(f"working {i}")
        time.sleep(0.5)
    print()


class Game:
    """
    This class connects all classes to each other
    and here the game starts, ends, and restarts
    """
    def __init__(self) -> None:
        """
        Constructor contains all instance variables such as
        players, high_score_list, histograms, intelligence,
        ui, threshold. turn, turn_looping, won, GAME_LOG_FILE,
        DATA_FILE
        :return: None
        """
        self.players: List[Player] = []
        self.high_score_list: \
            List[High_score] = \
            [High_score() for i in range(2)]
        self.histograms: \
            List[Histogram] = \
            [Histogram() for i in range(2)]
        self.__intelligence = None
        self.ui = UI()
        self.threshold = 0
        self.turn = True
        self.turn_looping = True
        self.__won = False
        self.GAME_LOG_FILE = "player_info.txt"
        self.DATA_FILE = "dice_values.csv"

    def matchmaking(self) -> None:
        """
        Matchmaking is the method where
        every player enters his name
        to be added to the player list
        :return: None
        """
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
                break

    def register_new_player(self, player: Player) -> None:
        """
        register a new player that has no saved information in the game log
        :return: None
        """
        with open(self.GAME_LOG_FILE, 'a') as file:
            file.write(f"{player.name},0,0,0,0\n")
            self.ui.player_registered(player.name)

    def check_player_info(self) -> None:
        """
        If the player is already registered gets a confirmation msg,
        otherwise, it'll be registered
        :return: None
        """
        for player in self.players:
            with open(self.GAME_LOG_FILE, 'r') as file:
                player_found = False
                for line in file:
                    name_in_log = line.rstrip().split(",")[0]
                    if player.name == name_in_log:
                        self.ui.player_confirmed(player.name)
                        player_found = True
                if not player_found:
                    self.register_new_player(player)

    def update_player_info(self, update_name: bool,
                           current_name: str,
                           new_name: str,
                           high_score: int,
                           loser_name: str) -> None:
        """
        Update the player information in the game log file.

        :param update_name: A bool that indicates whether to update the player name or not.
        :param current_name: The player's current name.
        :param new_name: The name the player wants to change to.
        :param high_score: The player's high score.
        :param loser_name: The name of the loser, if applicable.
        :return: None
        """
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
                        lines[i] = f"{name},{str(int(matches_played) + 1)}," \
                                   f"{str(int(total_wins) + 1)}," \
                                   f"{total_losses},{high_score}\n"
                    else:
                        lines[i] = f"{name},{str(int(matches_played) + 1)}," \
                                   f"{str(int(total_wins) + 1)}," \
                                   f"{total_losses},{old_high_score}\n"
                    print(lines[i], end="")
            elif loser_name == name and not update_name:
                lines[i] = f"{name},{str(int(matches_played) + 1)},{total_wins}," \
                           f"{str(int(total_losses) + 1)},{old_high_score}\n"
                print(lines[i], end="")
        with open(self.GAME_LOG_FILE, 'w') as file:
            file.writelines(lines)

    def end_turn(self, dice_hand: Dice_hand) -> None:
        """
        end player turn and reset the dice hand object
        :param dice_hand: dice hand object
        :return: None
        """
        self.turn = not self.turn
        self.turn_looping = False
        dice_hand.reset_values()

    def exit_confirmation(self) -> None:
        """
        Confirm that the player really wants to exit the game
        :return: None
        """
        play_again = input("Do you want to play again? [YES/NO]\n").lower()
        while True:
            if play_again == "yes":
                self.restart_match()
                break
            elif play_again == "no":
                sys.exit()
            else:
                self.ui.invalid_input_exception()

    def detect_winner(self, player_index: int) -> None:
        """
        Checks for winner and if it finds one the players results will be displayed
        :param player_index: player object index in the players list
        :return: None
        """
        winner = self.players[player_index]
        loser = self.players[(player_index+1) % 2]

        if winner.get_score() >= self.threshold:
            print(f"The winner is {winner.name}")
            self.high_score_list[player_index].\
                add_high_score(winner.get_score())
            print(f"Winner high score list: "
                  f"{self.high_score_list[player_index].get_high_scores()}")
            self.update_player_info(False, winner.name,
                                    None, winner.get_score(),
                                    loser.name)
            self.exit_confirmation()

    def check_cast(self, histogram: Histogram, player_index: int, dice_hand: Dice_hand) -> None:
        """
        Write the new cast value in the data file
        which the AI module train on.
        if the cast value is one, we reset
        player's score and end the turn
        Otherwise, we increase the score,
        add the new cast to the histogram
        and check for a winner
        :param histogram: Histogram object
        :param player_index:
        :param dice_hand:
        :return: None
        """
        player = self.players[player_index]
        cast = dice_hand.get_multiple_cast()

        with open(self.DATA_FILE, mode='a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([cast])
        if cast == 1:
            self.ui.one_was_rolled()
            player.reset_score()
            self.end_turn(dice_hand)
        else:
            self.ui.display_dice_cast(player.name, cast)
            player.increase_score(cast)
            histogram.update(cast)
            self.detect_winner(player_index)

    def restart_match(self) -> None:
        """
        Reset player score and histogram, then restart the match
        :return: None
        """
        for player in self.players:
            player.reset_score()
        for histogram in self.histograms:
            histogram.reset()
        if self.__intelligence is None:
            self.one_vs_one()
        else:
            self.one_vs_machine()

    def match_loop(self, player_action: int, dice_hand: Dice_hand,
                   player_index: int, histogram: Histogram) -> None:
        """
        The match loop represents the alternative game choices
        roll a die, hold, rename player, display histogram,
        restart, and quit during the match
        :param player_action: player input/alternative choice
        :param dice_hand: dice hand object
        :param player_index: player index in the players list
        :param histogram: the histogram object
        :return: None
        """
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
                    self.ui.only_alphabet_exception()
            player.name = new_name
        elif action == 4:
            histogram.display()
        elif action == 5:
            self.restart_match()
        elif action == 6:
            sys.exit()

    def turn_shift(self, player_index: int, dice_hand: Dice_hand) -> None:
        """
        The start point of player turn
        :param player_index: player index in the players list
        :param dice_hand: dice hand object
        :return: None
        """
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
                    self.ui.only_digits_exception()
            self.match_loop(player_action, dice_hand, player_index, histogram)

    def machine_turn(self, player_index: int, dice_hand: Dice_hand) -> None:
        """
        Machine's turn playing according to the chosen ai level by the player
        :param player_index: player index in the players list
        :param dice_hand: dice hand object
        :return: None
        """
        histogram = self.histograms[1]
        player = self.players[player_index]
        self.turn_looping = True
        print("It's machine's turn..")
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

    def select_threshold(self) -> None:
        """
        select the threshold, which is the amount points
        the players need to achieve in order to win
        :return: None
        """
        progress_bar()
        while True:
            self.threshold = input("Assign a threshold: ")
            if self.threshold.isdigit():
                self.threshold = int(self.threshold)
                break

    def one_vs_one(self) -> None:
        """
        The start point of one_vs_one game mode
        :return: None
        """
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

    def one_vs_machine(self) -> None:
        """
        The starting point of one_vs_machine game mode
        :return: None
        """
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

    def begin(self) -> None:
        """
        Selecting a game mode based on amount players
        :return: None
        """
        if len(self.players) > 1:
            self.one_vs_one()
        elif len(self.players) == 1:
            while True:
                level = int(input("Easy level: 0\nHard level: 1\n"))
                self.__intelligence = Intelligence(level, self.DATA_FILE)
                self.one_vs_machine()
                break

    def game_loop(self) -> None:
        """
        The game loop contains all main methods that
        are responsible to process the game
        :return: None
        """
        self.matchmaking()
        self.check_player_info()
        self.ui.display_game_rules()
        self.begin()


if __name__ == '__main__':
    main = Game()
    main.game_loop()
