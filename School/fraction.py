def fraction():
    global a, b
    if a > b:
        max = a
    else:
        max = b
    i = 2
    while (i <= max // 2) and (a != 1) and (b != 1):
        if (a % i == 0) and (b % i == 0):
            a = a // i
            b = b // i
        else:
            i = i + 1


a = 3
b = 9
fraction()
print(a, b)
