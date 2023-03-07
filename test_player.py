"""" Imports player """
from player import Player


def test_increase_score():
    """
        Creates a new Player object with a name of "Mohammed", increases the player's score by 10 using
        the increase_score() method, and then checks that the get_score() method returns the expected value of 10.
        """
    p = Player("Mohammed")
    p.increase_score(10)
    assert p.get_score() == 10


def test_reset_score():
    """
        Creates a new Player object with a name of "shuayb", increases the player's score by 5 using
        the increase_score() method, resets the player's score to 0 using the reset_score() method,
        and then checks that the get_score() method returns the expected value of 0.
        """
    p = Player("shuayb")
    p.increase_score(5)
    p.reset_score()
    assert p.get_score() == 0


def test_get_score():
    """
        Creates a new Player object with a name of "Nour", checks that the player's score is initially
        0 using the get_score() method, increases the player's score by 15 using the increase_score()
        method, and then checks that the get_score() method returns the expected value of 15.
        """
    p = Player("Nour")
    assert p.get_score() == 0
    p.increase_score(15)
    assert p.get_score() == 15