import re

def only_digits(string):
    return re.fullmatch(r"[1234567890]*", string)