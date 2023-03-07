import sys
from dice_hand import Dice_hand
from player import Player
from game import Game


def test_game_instance():
    game = Game()
    assert isinstance(game, Game)

def test_csv_import():
    assert "csv" in sys.modules

def test_list_import():
    assert "List" not in sys.modules

