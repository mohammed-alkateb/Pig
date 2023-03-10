import sys
import csv
import unittest
import pytest
from typing import List
from io import StringIO
from unittest.mock import patch, MagicMock
from dice import Dice
from dice_hand import Dice_hand
from player import Player
from game import Game
from histogram import Histogram
from high_score import High_score


def test_game_instance():
    game = Game()
    assert isinstance(game, Game)


def test_csv_import():
    assert "csv" in sys.modules


def test_list_import():
    assert "List" not in sys.modules


def test_matchmaking():
    with patch('builtins.input', side_effect=['2', 'player1', 'player2']):
        game = Game()
        game.players.append(Player("player1"))
        game.players.append(Player("player2"))
        assert len(game.players) == 2
        assert game.players[0].name == 'player1'
        assert game.players[1].name == 'player2'


def test_register_new_player():
    game = Game()
    game.GAME_LOG_FILE = "player_info.txt"

    player = Player("Alice")
    game.register_new_player(player)

    # Verify that the game log file was updated with the new player
    with open(game.GAME_LOG_FILE, 'r') as file:
        lines = file.readlines()
    assert lines[len(lines)-1].strip() == "Alice,0,0,0,0"

"""
class TestCheckPlayerInfo(unittest.TestCase):

    game = Game()
    game.players = [{'name': 'John', 'age': 25}, {'name': 'Alice', 'age': 30}]
    mock_file_content = "John,25\n"
    game.ui = MagicMock()

    def test_player_already_registered(self):
        # Arrange
        with open('player_info.txt', 'w') as file:
            file.write(self.mock_file_content)
        self.game.GAME_LOG_FILE = 'player_info.txt'

        # Act
        self.game.check_player_info()

        # Assert
        self.ui.player_confirmed.assert_called_once_with('John')
        self.ui.player_confirmed.assert_not_called_with('Alice')
        self.game.register_new_player.assert_not_called()

    def test_player_not_registered(self):
        # Arrange
        with open('player_info.txt', 'a') as file:
            file.write('')
        self.game.GAME_LOG_FILE = 'player_info.txt'

        # Act
        self.game.check_player_info()
        self.game.register_new_player.assert_called_once_with({'name': 'John', 'age': 25})"""


def test_game_loop_methods_are_called(mocker):
    """
    Test that the game loop calls the necessary methods.
    """
    # Create a mock object for the Game class
    game = Game()

    # Create mock objects for the methods that the game loop should call
    matchmaking_mock = mocker.patch.object(game, 'matchmaking')
    check_player_info_mock = mocker.patch.object(game, 'check_player_info')
    display_game_rules_mock = mocker.patch.object(game.ui, 'display_game_rules')
    begin_mock = mocker.patch.object(game, 'begin')

    # Call the game loop method
    game.game_loop()

    # Check that the necessary methods were called
    matchmaking_mock.assert_called_once()
    check_player_info_mock.assert_called_once()
    display_game_rules_mock.assert_called_once()
    begin_mock.assert_called_once()
