n = 5


def increase(n):
    if n != 0:
        increase(n-1)
        print(n, end=" ")
    


def decrease(n):
    if n != 0:
        print(n, end=" ")
        decrease(n-1)
    


increase(n)
print()
decrease(n)
