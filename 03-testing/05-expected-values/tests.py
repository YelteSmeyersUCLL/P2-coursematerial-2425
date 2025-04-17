import pytest
from mergesort import *
from pytest import approx
import itertools


@pytest.mark.parametrize('ns', [
    list(range(i + 1)) for i in range(100)
])
def test_split_in_two(ns):
    left, right = split_in_two(ns)
    assert left + right == ns
    assert approx(len(left), abs=1) == len(right)

@pytest.mark.parametrize('left', [
    [],
    [1, 2, 3],
    [4, 10, 15],
    [2, 5, 5, 9],
    [-3, 0, 5, 10]
])
@pytest.mark.parametrize('right', [
    [],
    [4, 5, 6],
    [1, 8, 20],
    [3, 3, 7, 10],
    [-1, 2, 4, 8]
])
def test_merge_sorted(left, right):
    assert merge_sorted(left, right) == sorted(left + right)

@pytest.mark.parametrize(
    "expected, ns", 
    [( [1, 2, 3], list(perm) ) for perm in itertools.permutations([1, 2, 3]) ] +
    [( [], list(perm) ) for perm in itertools.permutations([]) ] +
    [( [1, 2, 2, 2, 3], list(perm) ) for perm in itertools.permutations([1, 2, 2, 3, 2]) ] +
    [( [1], list(perm) ) for perm in itertools.permutations([1]) ] +
    [( [3, 10, 20, 24], list(perm) ) for perm in itertools.permutations([10, 3, 20, 24]) ]
)
def test_merge_sort(expected, ns):
    assert merge_sort(ns) == expected