def findMaximum(list):
    if not list:
        raise IndexError("list is empty")
    if len(list) == 1:
        return list[0]
    return max(findMaximum(list[1:]), list[0])

print(findMaximum([1, 6, 30, 4, 5, 10, 6, 7]))