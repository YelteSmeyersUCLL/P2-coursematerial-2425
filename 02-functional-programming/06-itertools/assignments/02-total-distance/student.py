from itertools import pairwise

def total_distance(path, distance):
    total = 0
    for city_a, city_b in pairwise(path):
        total += distance(city_a, city_b)
    return total

def distance(a, b):
    return abs(a - b)

path = iter([0, 2, 4])
print(total_distance(path, distance))