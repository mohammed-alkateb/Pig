from player import Player


def test_increase_score():
    p = Player("Mohammed")
    p.increase_score(10)
    assert p.get_score() == 10


def test_reset_score():
    p = Player("shuayb")
    p.increase_score(5)
    p.reset_score()
    assert p.get_score() == 0


def test_get_score():
    p = Player("Nour")
    assert p.get_score() == 0
    p.increase_score(15)
    assert p.get_score() == 15