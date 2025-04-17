import pytest
from parentheses import *

@pytest.mark.parametrize('string', [
    (''),
    ('()'),
    ('((((((((((((((((((((((((()))))))))))))))))))))))))'),
    ('((((()))))'),
    ('((()))')
])

def test_matching_parentheses(string):
    assert matching_parentheses(string), f"String {string} has matching parentheses"

@pytest.mark.parametrize('string', [
    ("((()))))"),
    ("("),
    ("(()"),
    (')('),
    (')()')
])

def test_non_matching_parentheses(string):
    assert not matching_parentheses(string), f"String {string} does not have matching parentheses"
