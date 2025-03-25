def is_prime(n):
    return 2 == len([number for number in range(1, n + 1) if n % number == 0])
    
def primes():
    count = 2
    while True:
        if is_prime(count):
            yield count
        count += 1

print(is_prime(5))

print(is_prime(6))

ps = primes()
print(next(ps))

print(next(ps))

print(next(ps))

print(next(ps))