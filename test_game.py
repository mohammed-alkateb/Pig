import sys
import csv
import unittest
from unittest import TestCase, mock

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


class TestGame(TestCase):
    @mock.patch('builtins.open', new_callable=mock.mock_open)
    def test_check_player_info(self, mock_file):
        # Set up a mock file with a single line containing a player's name
        mock_file.return_value.__enter__.return_value.readline.return_value = 'Alice, 100\n'

        # Create a game instance and a player instance
        game = Game()
        player = Player('Bob')

        # Add the player to the game's list of players
        game.players.append(player)

        # Call the method under test
        game.check_player_info()

        self.assertIn(player, game.players)
        mock_file.assert_called_once_with(game.GAME_LOG_FILE, 'r')


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
