import re

def correct_dates(string):
    return re.sub(r"(\d+)/(\d+)", r"\2/\1", string)

print(correct_dates("1/2/2000"))