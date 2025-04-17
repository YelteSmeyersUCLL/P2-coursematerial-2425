def split_in_two(ns):
    half = int(len(ns) // 2)
    output = []
    output.append(ns[:half])
    output.append(ns[half:])
    return output

def merge_sorted(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def merge_sort(ns):
    if len(ns) <= 1:
        return ns    
    left, right = split_in_two(ns)

    sorted_left = merge_sort(left)  # Recursively sort left half
    sorted_right = merge_sort(right)  # Recursively sort right half

    return merge_sorted(sorted_left, sorted_right)

print(split_in_two([1, 2, 3, 4, 5, 6, 7]))

# output = [[i for i in range(item + 1)] for item in range(50)]
# print(output)
left, right = split_in_two([0, 5, 6, 6, 9, 10, 20])
print(merge_sorted([10, 20], [1, 2]))
# output = list(list(range(i + 1)) for i in range(5))
# print(output)
import itertools
output = [list(perm) for perm in itertools.permutations([1, 2, 3])]
print(output)
