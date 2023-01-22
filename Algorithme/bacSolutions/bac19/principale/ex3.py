import pickle as pic
from random import randint


def fraction():
    f = open("fraction.dat", "rb")
    g = open("irreduct.dat", "wb")
    ffch = False
    while not ffch:
        try:
            e = pic.load(f)
            a = e["Num"]
            b = e["Denum"]
            r = a % b
            while r != 0:
                a = b
                b = r
                r = a % b
            e["Num"] = e["Num"] // b
            e["Denum"] = e["Denum"] // b
            pic.dump(e, g)
        except:
            ffch = True

    f.close()
    g.close()


nbFraction = 10
f = open("fraction.dat", "wb")
for i in range(nbFraction):
    e = dict()
    e["Num"] = randint(1, 100)
    e["Denum"] = randint(1, 100)
    pic.dump(e, f)
f.close()
fraction()
g = open("irreduct.dat", "rb")
f = open("fraction.dat", "rb")
for i in range(nbFraction):
    e = pic.load(g)
    e1 = pic.load(f)
    print(str(e1["Num"]) + "÷" + str(e1["Denum"]) +
          "\t->   " + str(e["Num"]) + "÷" + str(e["Denum"]))
g.close()
