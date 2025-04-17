import re

def one_or_more_abc(string):
    pattern = r"(abc)+"
    return re.fullmatch(pattern, string)