import pickle as pic


def verify(ch):
    if ch == "":
        return True
    if ch[len(ch)-1] < "A" or ch[len(ch)-1] > "Z":
        return False
    return verify(ch[:len(ch)-1])


def remplir1(fch, n):
    F = open(fch, "wb")
    for i in range(n):
        e = {}
        e["nom"] = str(input("donner nom: "))
        e["pr"] = str(input("donner prenom: "))
        e["age"] = int(input("donner age: "))
        v = False
        while not v:
            e["con"] = str(input("donner confidentiel: "))
            v = verify(e["con"])
        pic.dump(e, F)
    F.close()


def remplir2(fch1, fch2):
    F = open(fch1, "rb")
    G = open(fch2, "w")
    Fin_Fichier = False
    while not Fin_Fichier:
        try:
            e = pic.load(F)
            nom = e["nom"][0].upper() + e["nom"][1:]
            pr = e["pr"][0].upper() + e["pr"][1:]
            np = nom + " " + pr
            G.write(np + "\n")
        except:
            Fin_Fichier = True
    F.close()
    G.close()


def rep(x, c):
    ch = ""
    for i in range(x):
        ch = ch + c
    return ch


def remplirM(c1):
    global m, a, b

    F = open(c1, "rb")

    a = 1
    e = pic.load(F)
    b = len(e["con"])
    fin_fichier = False
    while not fin_fichier:
        try:
            e = pic.load(F)
            a = a + 1
            if len(e["con"]) > b:
                b = len(e["con"])
        except:
            fin_fichier = True
    F.close()
    m = [[str()] * b for i in range(a)]
    F = open(c1, "rb")
    for j in range(a):
        e = pic.load(F)
        length = len(e["con"])
        ch = e["con"] + rep(b-length, "#")
        for i in range(len(ch)):
            m[j][i] = ch[i]

    F.close()


def afficher(fch1, fch2, m, a, b):
    F = open(fch1, "rb")
    G = open(fch2, "r")
    print()
    fin_fichier = False
    while not fin_fichier:
        try:
            e = pic.load(F)
            print(e["nom"], "   ", e["pr"], "   ", e["age"], "   ", e["con"])
        except:
            fin_fichier = True
    print()
    ch = G.readline().rstrip()
    while ch != "":
        print(ch)
        ch = G.readline().rstrip()

    G.close()
    print()
    for j in range(a):
        for i in range(b):
            print(m[j][i], end=" ")
        print()


n = int(input("donner n: "))
c1 = "clients.dat"
c2 = "clients.txt"

remplir1(c1, n)
remplir2(c1, c2)
remplirM(c1)
afficher(c1, c2, m, a, b)
