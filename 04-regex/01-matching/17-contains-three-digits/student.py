import re

def contains_three_digits(string):
    return re.fullmatch(r"(.*[0-9]){3,}", string)