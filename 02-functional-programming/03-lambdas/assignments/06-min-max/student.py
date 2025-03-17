def closest(points, target_point):
    return min(points, key=lambda point: ((point[0]-target_point[0])**2 + (point[1]-target_point[1])**2)**0.5)


points = [
    (1, 5), (3, 8), (6, 2), (7, 4), (2, 9),
    (5, 1), (8, 7), (4, 3), (9, 6), (0, 0),
    (10, 10), (12, 5), (14, 8), (3, 3), (7, 7),
    (11, 2), (6, 9), (2, 4), (8, 1), (13, 6)
]

print(closest(points, (6, 5)))