from math import sqrt


def estPremier(n):
    flag = True
    i = 2
    while i <= sqrt(n) and flag:
        if n % i == 0:
            flag = False
        i += 1
    return flag


def dec_to_bin(n):
    ch = ""
    while n != 0:
        ch = str(n % 2) + ch
        n = n // 2
    return ch


def valider(code):
    bin = dec_to_bin(int(code[3:8]))
    nbz = 0
    for i in range(len(bin)):
        if bin[i] == "0":
            nbz += 1
    if estPremier(int(code[0:3])) and nbz > 8 and (int(code[8:]) % int(code[0:3])) == 0:
        flag = True
    else:
        flag = False
    return flag


def saisir():
    global T
    v = False
    while not v:
        code = str(input("donner code: "))
        v = code.isnumeric() and len(code) == 13

    if not valider(code):
        print("Code non valide")
    elif code not in T:
        print("Code deja utilise")
    else:
        print("Code Valide")
        # REMOVING THE USED CODE.
        remove_used_code(fch, T, long, code)


def num_lignes(fch):
    F = open(fch, "r")
    long = 0
    ch = F.readline()
    while ch != "":
        long = long + 1
        ch = F.readline()
    F.close()
    return long


def file_tab(fch, long):
    global T
    F = open(fch, "r")
    for i in range(long):
        T[i] = F.readline().rstrip()
    F.close()


# ADDITION... SHOULDN'T THE CODE USED BE REMOVED FROM THE "Codes.txt" file?


def remove_used_code(fch, T, long, code):
    F = open(fch, "w")
    for i in range(long):
        if not (T[i] == code):
            F.write(T[i] + "\n")
    F.close()


fch = "Codes.txt"
long = num_lignes(fch)
T = [str()] * long
file_tab(fch, long)
saisir()

# The Codes which you have to put in "Codes.txt"
"""
1017856230401
1133468948025
1632560010595
2114512367731
2279115922246
2414560037596
3372102075151
4619456019823
5993674058702
9119072089278

"""
