n = 5
M = [([int()] * n) for i in range(n)]

for i in range(n):
    for j in range(n):
        if i == j or j == 0:
            M[i][j] = 1
        elif i > j:
            M[i][j] = M[i-1][j] + M[i-1][j-1]

for j in range(n):
    for i in range(n):
        print(M[j][i], end=" ")
    print()
