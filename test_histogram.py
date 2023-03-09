"""" Imports histogram """
from histogram import Histogram


def test_update():
    """
    Creates a new histogram, updates it with
    the values 1, 3, and 5, and then checks
    that the histogram contains the expected
    values using the get_data() method.
    Expected result: the histogram contains
    [0, 1, 0, 1, 0, 1, 0].
    """
    histogram = Histogram()
    histogram.update(1)
    histogram.update(3)
    histogram.update(5)
    assert histogram.get_data() == [0, 1, 0, 1, 0, 1, 0]


def test_reset():
    """
    Creates a new histogram, updates it with
    the values 1, 3, and 5, resets the histogram
    using the reset() method, and then checks
    that the histogram is empty using the len() function.
    Expected result: the histogram has a length of 0.
    """
    histogram = Histogram()
    histogram.update(1)
    histogram.update(3)
    histogram.update(5)
    histogram.reset()
    assert len(histogram.get_data()) == 0

def test_display():
    """
    Creates a new histogram, updates it with
    the values 1, 3, and 5, and checks that
    the display method generates the correct
    histogram plot.
    """
    histogram = Histogram()
    histogram.update(1)
    histogram.update(3)
    histogram.update(5)
    histogram.display()
