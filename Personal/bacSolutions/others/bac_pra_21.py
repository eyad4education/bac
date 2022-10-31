def puissance(x, y):
    if y == 0:
        return 1
    elif y > 0:
        return x * puissance(x, y-1)
    else:
        return 1 / puissance(x, -y)


def Genere(Nb):
    Mot = ""
    v = False
    while not v:
        R = Nb % 3
        # "SELON" ALTERNATIVE FOR PYTHON VERSION LESS THAN 3.10
        if R == 0:
            Y = "Ma"
        elif R == 1:
            Y = "Des"
        elif R == 2:
            Y = "Son"

        # "SELON" (v3.10 or greater)
        # match R:
        #     case 0:
        #         Y = "Ma"
        #     case 1:
        #         Y = "Des"
        #     case 2:
        #         Y = "Son"

        Mot = Y + Mot
        Nb = Nb // 3
        v = Nb == 0
    return Mot


def hex_to_dec(n):
    nb = 0
    for i in range(len(n)):
        if '0' <= n[i] and n[i] <= '9':
            # nb = nb + int(n[i]) * (16**(len(n)-i-1))
            nb = nb + int(n[i]) * puissance(16, len(n)-i-1)
        else:
            # nb = nb + (ord(n[i])-55) * (16**(len(n)-i-1))
            nb = nb + (ord(n[i])-55) * puissance(16, len(n)-i-1)
    return nb


def fch_to_tab(fch1):
    global T, long
    F = open(fch1, "r")
    long = 0
    ch = F.readline()
    while ch != "":
        long = long + 1
        ch = F.readline()
    F.close()

    T = [dict()] * long

    F = open(fch1, "r")

    for i in range(long):
        e = {}
        e["Hex"] = F.readline().rstrip()
        e["Num"] = i+1
        e["Dec"] = hex_to_dec(e["Hex"])
        T[i] = e
    F.close()

    flag = False
    while not flag:
        isSorted = True
        for i in range(long-1):
            if T[i]["Dec"] > T[i+1]["Dec"]:
                tmp = T[i]
                T[i] = T[i+1]
                T[i+1] = tmp
                isSorted = False
        flag = isSorted


def fch2_to_res(fch2):
    F = open(fch2, "w")
    for i in range(long):
        ch = Genere(T[i]["Dec"]) + " " + str(T[i]["Num"])
        F.write(ch + "\n")
    F.close()


fch1 = "ImgHexa.txt"
fch2 = "Resultat.txt"

fch_to_tab(fch1)
fch2_to_res(fch2)
