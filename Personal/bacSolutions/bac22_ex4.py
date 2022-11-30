from math import sqrt


def Premier(p):
    flag = True
    i = 2
    while i <= int(sqrt(p)) and flag:
        if p % i == 0:
            flag = False
        i = i + 1
    return flag


def Quadruplets():
    global T, len
    len = 0
    for i in range(2, 201):
        if Premier(i):
            e = {}
            e["p0"] = i
            e["p1"] = i + 2
            e["p2"] = i + 6
            e["p3"] = i + 8
            T[len] = e
            len = len + 1


def Calcul_B(T, len):
    B = 0
    for i in range(len):
        e = T[i]
        B = B + ((1 / e["p0"])+(1 / e["p1"])+(1 / e["p2"])+(1 / e["p3"]))
    return B


T = [dict()] * 200
Quadruplets()
print(Calcul_B(T, len))
