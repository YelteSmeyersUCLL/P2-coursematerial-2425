import pytest
from pytest import approx
from mystatistics import average

@pytest.mark.parametrize('ns, expected', [
    ([0.1, 0.1, 0.1], 0.1),
    ([1, 2, 3, 4, 5], 3.0),
    ([1, 2, 3], 2.0),
    ([2.5, 3.5, 4.5], 3.5),

    ([5], 5.0),
    ([], 0),
    ([0.0, 0.0], 0.0),

    ([-2, -4, -6], -4.0),
    ([-1, 0, 2], 0.3333333333),

    ([0.333, 0.666, 0.999], 0.666),
    ([10, 20, 30, 40], 25.0),
    ([1.1, 1.2, 1.3, 1.4], 1.25)
])
def test_correct_average(ns, expected):
    assert approx(average(ns), abs=0.01) == expected, f"For {ns}, expected {expected}, got {average(ns)}"
