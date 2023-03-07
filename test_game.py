

from dice_hand import Dice_hand
from player import Player
from game import Game


def test_matchmaking():
    game = Game()
    game.matchmaking()
    assert len(game.players) == 2

def test_register_new_player():
    game = Game()
    player = Player("John")
    game.register_new_player(player)
    with open(game.GAME_LOG_FILE, 'r') as file:
        assert "John" in file.read()

def test_check_player_info():
    game = Game()
    player1 = Player("John")
    player2 = Player("Alice")
    game.players = [player1, player2]
    game.check_player_info()
    with open(game.GAME_LOG_FILE, 'r') as file:
        assert "John" in file.read()
        assert "Alice" in file.read()

def test_update_player_info():
    game = Game()
    player1 = Player("John")
    game.players = [player1]
    game.register_new_player(player1)
    game.update_player_info(False, player1.name, None, 100, "Alice")
    with open(game.GAME_LOG_FILE, 'r') as file:
        assert "John,1,1,0,100" in file.read()

def test_end_turn():
    game = Game()
    dice_hand = Dice_hand()
    game.end_turn(dice_hand)
    assert game.turn == False
    assert game.turn_looping == False

def test_roll_dice():
    game = Game()
    dice_hand = Dice_hand()
    game.roll_dice(dice_hand)
    assert len(dice_hand.dice) == 5

def test_calculate_score():
    game = Game()
    dice_hand = Dice_hand()
    dice_hand.roll_all_dice()
    score = game.calculate_score(dice_hand)
    assert isinstance(score, int)

def test_update_player_info_win():
    game = Game()
    player1 = Player("John")
    game.players = [player1]
    game.register_new_player(player1)
    game.update_player_info(True, player1.name, None, 1000, "Alice")
    with open(game.GAME_LOG_FILE, 'r') as file:
        assert "John,1,1,1,1000" in file.read()

def test_end_game():
    game = Game()
    game.players = [Player("John"), Player("Alice")]
    game.end_game()
    assert game.game_over == True

def test_save_game():
    game = Game()
    player1 = Player("John")
    player2 = Player("Alice")
    game.players = [player1, player2]
    game.register_new_player(player1)
    game.register_new_player(player2)
    game.update_player_info(False, player1.name, None, 100, player2.name)
    game.update_player_info(False, player2.name, None, 200, player1.name)
    game.save_game()
    with open(game.GAME_SAVE_FILE, 'r') as file:
        assert "John,0,0,0,100" in file.read()
        assert "Alice,0,0,0,200" in file.read()

def test_load_game():
    game = Game()
    game.load_game()
    assert len(game.players) == 2
    assert game.players[0].name == "John"
    assert game.players[1].name == "Alice"
