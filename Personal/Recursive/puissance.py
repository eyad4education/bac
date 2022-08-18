def puissance(x, y):
    if y == 0:
        return 1
    elif y > 0:
        return x * puissance(x, y-1)
    else:
        return 1 / puissance(x, -y)


print(puissance(2,3))