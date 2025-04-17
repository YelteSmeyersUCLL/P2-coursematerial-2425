import re

def only_letters(string):
    return re.fullmatch(r"([a-z]|[A-Z])*", string)