from itertools import permutations


def find_shortest_path(distance, city_count):
    cities = list(range(1, city_count))

    shortest_path = None
    shortest_distance = float('inf')

    for perm in permutations(cities):
        path = [0] + list(perm) + [0]
        
        total = 0
        for i in range(len(path) - 1):
            total += distance(path[i], path[i + 1])
        
        if total < shortest_distance:
            shortest_distance = total
            shortest_path = path
    
    return shortest_path

def distance(a, b):
    return abs(a - b)

print(find_shortest_path(distance, 4))