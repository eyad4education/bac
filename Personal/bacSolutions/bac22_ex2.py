def MinM(M, C, j):
    min = M[j][0]
    for i in range(1, C):
        if M[j][i] < min:
            min = M[j][i]
    return min


def MaxM(M, L, i):
    max = M[0][i]
    for j in range(1, C):
        if M[j][i] > max:
            max = M[j][i]
    return max


def Points_cols(L, C, F_col):
    global M, M_min, M_max
    for j in range(L):
        for i in range(C):
            if MinM(M, C, j) == M[j][i]:
                M_min[j][i] = 1
            else:
                M_min[j][i] = 0
            if MaxM(M, L, i) == M[j][i]:
                M_max[j][i] = 1
            else:
                M_max[j][i] = 0
            if M_min[j][i] + M_max[j][i] == 2:
                ligne = str(M[j][i]) + " " + "(" + str(j+1) + "," + str(i+1) + ")"
                F_col.write(ligne + "\n")


M = [[9, 5, 7, 5], [4, 2, 2, 3], [4, 3, 3, 2], [8, 5, 6, 5], [7, 4, 10, 4]]
M_min = [[int()] * 4 for i in range(5)]
M_max = [[int()] * 4 for i in range(5)]
L = 5
C = 4
F_col = open("F_col.txt", "w")
Points_cols(L, C, F_col)
F_col.close()
