from high_score import High_score

def test_add_high_score():
    high_scores = High_score()
    assert high_scores.add_high_score(90) == True
    assert high_scores.add_high_score(80) == False
    assert high_scores.add_high_score(95) == True

def test_get_high_scores():
    high_scores = High_score()
    high_scores.add_high_score(90)
    high_scores.add_high_score(95)
    assert high_scores.get_high_scores() == 90