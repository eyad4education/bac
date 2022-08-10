n = 5
M = [([int()] * n) for i in range(n)]


def pascal(n):
    global M
    for j in range(n):
        M[j][0] = 1
        M[j][j] = 1
        for i in range(1,j):
            M[j][i] = M[j-1][i-1] + M[j-1][i]

pascal(n)

for j in range(n):
    for i in range(n):
        print(M[j][i], end=" ")
    print()
