def sum_numbers(number):
    num = str(abs(number))
    if len(num) <= 1:
        return number
    return int(num[0]) + sum_numbers(int(num[1:]))

print(sum_numbers(-153))