n = 5
M = [([int()] * n) for i in range(n)]

for j in range(n):
    for i in range(n):
        if i == j or j == 0:
            M[j][i] = 1
        elif j > i:
            M[j][i] = M[j-1][i] + M[j-1][i-1]

for j in range(n):
    for i in range(n):
        print(M[j][i], end=" ")
    print()
