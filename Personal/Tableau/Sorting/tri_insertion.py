n = 5
t = [3, 1, 2, 5, 4]


for i in range(1, n):
    a = t[i]
    j = i
    while (j > 0) and (t[j-1] > a):
        t[j] = t[j-1]
        j = j - 1
    t[j] = a


print(t)
