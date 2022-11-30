def Codage(F, FC):
    ch = F.readline().rstrip()
    while ch != "":
        n = len(ch)
        T = [str()] * 26
        for i in range(26):
            T[i] = chr(65+i)
        X = [int()] * n
        Y = [int()] * n
        for j in range(n):
            for i in range(26):
                if T[i] == ch[j]:
                    X[j] = i
        for i in range(n):
            Y[i] = (22 * X[i]) % 26
        ch = ""
        for i in range(n):
            ch = ch + T[Y[i]]
        FC.write(ch + "\n")
        ch = F.readline().rstrip()


F = open("fch1.txt", "r")
FC = open("fch2.txt", "w")
Codage(F, FC)
F.close()
FC.close()
