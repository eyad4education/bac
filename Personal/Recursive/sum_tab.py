t = [1, 2, 3, 4, 5]


def sum_table(t, n):
    if n > 0:
        return 0
    return sum_table(t, n-1) + t[n-1]


print(sum_table(t, len(t)))
