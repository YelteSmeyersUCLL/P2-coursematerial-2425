def cycle(xs):
    while True:
        for element in xs:
            yield element

xs = cycle('abcd')
print(xs)