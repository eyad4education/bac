import pickle as pic
from random import randint


def chaine_chance(fch2):
    F = open(fch2, "r")
    ch = F.readline().rstrip()
    ch1 = ""
    while ch != "":
        ch1 += ch
        ch = F.readline().rstrip()
    F.close()
    return ch1


def remplir(fch1):
    global p
    F = open(fch1, "wb")
    p = randint(4, 10)
    for i in range(p):
        e = {}
        v = False
        while not v:
            e["Identifiant"] = str(
                input("donner Identifiant de client numero " + str(i+1) + ": "))
            v = e["Identifiant"].isnumeric() and len(e["Identifiant"]) == 10
        v = False
        while not v:
            e["NTel"] = str(
                input("donner la numero de client numero " + str(i+1) + ": "))
            v = e["NTel"].isnumeric() and len(e["NTel"]) == 8
        pic.dump(e, F)
    F.close()


def Calcul_CC(ch):
    while len(ch) > 1:
        sum = 0
        for i in range(len(ch)):
            sum += int(ch[i])
        ch = str(sum)

    return ch


def gagnant(fch1, ch_chance):
    F = open(fch1, "rb")
    endF = False
    while not endF:
        try:

            e = pic.load(F)
            for i in range(len(ch_chance)):
                if ch_chance[i] == Calcul_CC(e["NTel"]):
                    print("Identifiant: " + e["Identifiant"] + " --- " + "Numero Telephone : " + e["NTel"])
        except:
            endF = True

    F.close()


fch1 = "Clients.dat"
fch2 = "Chance.txt"
ch_chance = chaine_chance(fch2)
p = 0
remplir(fch1)
gagnant(fch1, ch_chance)


# FOR DEBUGGING (TESTING)
"""
id:
0001998810
numero:
65405003

"""

# File "Chance.txt" Content

"""
2
6
4
5
1
9

"""
