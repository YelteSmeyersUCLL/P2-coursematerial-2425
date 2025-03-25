def fizzbuzz():
    count = 0
    while True:
        count += 1
        if count % 3 == 0 and count % 5 == 0:
            yield "fizzbuzz"
        elif count % 3 == 0:
            yield "fizz"
        elif count % 5 == 0:
            yield "buzz"
        else:
            yield f'{count}'

