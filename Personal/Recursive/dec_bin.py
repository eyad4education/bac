n = 18


def decimal_binaire(n):
    if n == 0:
        return ""
    return decimal_binaire(n//2) + str(n % 2)


print(decimal_binaire(n))
