""" Imports high_score """
from high_score import High_score


def test_add_high_score():
    """
    This function creates a new High_score
    object, calls the add_high_score method
    with several scores, and then checks
    that the method returns True when a new high
    score is added and False otherwise.
    """
    high_scores = High_score()
    assert high_scores.add_high_score(90) is True
    assert high_scores.add_high_score(80) is False
    assert high_scores.add_high_score(95) is True


def test_get_high_scores():
    """
    This function creates a new High_score
    object, adds some high scores to it,
    and then checks that the method returns
    the highest score.
    """
    high_scores = High_score()
    high_scores.add_high_score(90)
    high_scores.add_high_score(95)
    assert high_scores.get_high_scores() == 90
