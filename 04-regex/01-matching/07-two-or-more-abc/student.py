import re

def two_or_more_abc(string):
    pattern = r"(abc){2,}"
    return re.fullmatch(pattern, string)