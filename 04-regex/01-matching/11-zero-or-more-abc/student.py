import re

def zero_or_more_abc(string):
    return re.fullmatch(r"(abc)*", string)