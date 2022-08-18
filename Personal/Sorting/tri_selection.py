n = 5
t = [3, 1, 2, 5, 4]

for i in range(n):
    index = i
    for j in range(i+1, n):
        if t[j] < t[index]:
            index = j
    if i != index:
        t[i] = t[i] + t[index]
        t[index] = t[i] - t[index]
        t[i] = t[i] - t[index]

print(t)
