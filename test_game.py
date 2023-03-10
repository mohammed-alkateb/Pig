import sys
import csv
from typing import List
from io import StringIO
from unittest.mock import patch, MagicMock

import pytest

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
