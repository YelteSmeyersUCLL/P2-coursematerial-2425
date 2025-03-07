def find_string_with_consecutive_characters(strings):
    for string in strings:
        for index in range(len(string) - 1):
            if string[index] == string[index + 1]:
                return string
    return None

def find()

print(find_string_with_consecutive_characters(["monkey", "banana", "computer", "yellow", "oddish"]))
