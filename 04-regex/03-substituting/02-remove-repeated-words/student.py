import re

def remove_repeated_words(string):
    return re.sub(r'\b(\w+)(\s+\1\b)+', r'\1', string)

print(remove_repeated_words("a a a a bc"))