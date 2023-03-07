from histogram import Histogram

def test_update():
    histogram = Histogram()
    histogram.update(1)
    histogram.update(3)
    histogram.update(5)
    assert histogram.get_data() == [0, 1, 0, 1, 0, 1, 0]


def test_reset():
    histogram = Histogram()
    histogram.update(1)
    histogram.update(3)
    histogram.update(5)
    histogram.reset()
    assert len(histogram.get_data()) == 0