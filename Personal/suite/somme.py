def somme_suite(n):
    if n == 0:
        return 6
    else:
        U = 6
        for i in range(1, n+1):
            U = 4 * U + 10
        return U


print(somme_suite(33))
