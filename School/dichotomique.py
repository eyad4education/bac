def binary_search(t, x, d, f):
    m = (d+f) // 2
    if d > f:
        return False
    elif t[m] == x:
        return True
    elif t[m] > x:
        return binary_search(t, x, d, m-1)
    else:
        return binary_search(t, x, m+1, f)


t = [-2, 3, 6, 10, 12]
n = 5
res = binary_search(t, 6, 0, n-1)
print(res)
