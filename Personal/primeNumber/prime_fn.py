from math import sqrt


def isPrime(x):
    i = 2
    flag = True
    while i <= int(sqrt(x)) and flag:
        if x % i == 0:
            flag = False
        i += 1
    return flag


print(isPrime(3))
