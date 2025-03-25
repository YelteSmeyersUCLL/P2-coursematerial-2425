from itertools import groupby, repeat


def rle_encode(iterable):
    result = []
    for key, group in groupby(iterable):
        result.append((f"{key}", sum(1 for _ in group)))
    return result

def rle_decode(data):
    result = ""
    for letter, count in data:
        result += "".join(repeat(letter, count))
    return result

# output = list(rle_encode("aaaaabbbbbbccccc"))
# print(output)

print(rle_decode([('a', 8), ('b', 5), ('c', 7)]))