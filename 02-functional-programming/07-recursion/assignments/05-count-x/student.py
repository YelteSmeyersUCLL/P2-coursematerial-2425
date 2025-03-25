def countX(text):
    if len(text) <= 0:
        return 0
    if text[0] == 'x':
        return countX(text[1:]) + 1
    else:
        return countX(text[1:])

print(countX("xTextxxx"))