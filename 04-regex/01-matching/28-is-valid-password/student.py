import re

def is_valid_password(string):
    if not re.fullmatch(r"^(?!.*(.)\1\1)(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[+\-*/.@]).{12,}$", string):
        return False
    return all(string.count(c) < 4 for c in set(string))
