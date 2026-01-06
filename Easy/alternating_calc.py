def Calculate(a, b):
    total = 0
    length = len(b)

    for i in range(length):
        # Add if index is even, subtract if odd
        if i % 2 == 0:
            total += b[i]
        else:
            total -= b[i]

        # Check divisibility and multiply accordingly
        if total % 6 == 0:
            total *= 6
        elif total % 3 == 0:
            total *= 3
        elif total % 2 == 0:
            total *= 2

    return total


n = 3
my_list = [1, 2, 3]
result = Calculate(n, my_list)
print(result)
