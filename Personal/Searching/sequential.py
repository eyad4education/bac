n = 5
t = [1, 2, 3, 4, 5]

e = 3


found = False
i = 0
while not found and i < n:
    if t[i] == e:
        found = True
    i = i + 1


print("found =", found)
