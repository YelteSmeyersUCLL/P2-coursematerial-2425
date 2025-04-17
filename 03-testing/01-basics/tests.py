from intervals import overlapping_intervals


def test_overlapping_intervals():
    assert overlapping_intervals((1, 5), (3, 6))
    assert not overlapping_intervals((2, 5), (7, 10))
    assert overlapping_intervals((0, 0), (-1, 1))
    assert not overlapping_intervals((4, 1), (1, 5))

    assert overlapping_intervals((1, 10), (3, 7))
    assert overlapping_intervals((2, 4), (1, 5))

    assert overlapping_intervals((1, 5), (5, 10))
    assert overlapping_intervals((5, 10), (1, 5))

    assert overlapping_intervals((2, 2), (2, 2))
    assert not overlapping_intervals((3, 3), (4, 4))

    assert overlapping_intervals((-5, 2), (-2, 4))
    assert not overlapping_intervals((-10, -5), (-4, 0))

    assert overlapping_intervals((-3, 3), (0, 5))
    assert not overlapping_intervals((-5, -1), (1, 5))

    assert overlapping_intervals((0, 10), (2, 3))
    assert overlapping_intervals((-10, 10), (-5, 5))

    assert not overlapping_intervals((5, 2), (3, 4))
    assert not overlapping_intervals((1, 3), (4, 2))
    assert not overlapping_intervals((3, 1), (4, 2))

    assert overlapping_intervals((1000, 2000), (1500, 2500))
    assert not overlapping_intervals((10000, 20000), (30000, 40000))