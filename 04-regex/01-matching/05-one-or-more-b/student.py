import re

def one_or_more_b(string):
    pattern = r"b+"
    return re.fullmatch(pattern, string)
