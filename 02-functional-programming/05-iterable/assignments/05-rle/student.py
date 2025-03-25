def rle_encode(iterable):
    iterator = iter(iterable)
    for current in iterator:
        count = 1
        for next_item in iterator:
            if next_item == current:
                count += 1
            else:
                yield (current, count)
                current = next_item
                count = 1
        yield (current, count)
        break

def rle_decode(data):
    for letter, count in data:
        for i in range(count):
            yield letter

result = list(rle_encode("aaaaaaaabbbbbccccccc"))
print(result)

output = list(rle_decode([('a', 8), ('b', 5), ('c', 7)]))
print(output)