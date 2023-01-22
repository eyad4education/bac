def saisie_base():
    v=False
    while not v:
        bch = input()
        valid = bch.isdecimal() and bch in ['2','8','10','16']
    return int(bch)
def saisie_controlee(b):
    v = False
    while not v:
        nb = input()
        v = verif(nb,b)
    return nb
def verif(nb : str,b : int):
    ok = True
    i = 0
    v = False
    while not v:
        if b == 16:
            if not ("0" <= nb[i] <= "9" or "A" <= nb[i].upper() <= "F"):
                ok = False
        else:
            if int(nb[i]) > b - 1:
                ok = False
        i = i + 1
        valid = (ok == False) or (i == len(nb))
    return ok
def convb1_b2(nb1,b1,b2):
    dec = 0
    for i in range(len(nb1)-1, -1, -1):
        if nb[i].upper() in ["A","B","C","D","E","F"]:
            x = ord(nb1[i].upper()) - 55
        else:
            x = int(nb1[i])
        dec = dec + x * puissance(b1,long(nb1)-1-i)
    nb2 = ""
    v = False
    while not v:
        r = dec % b2
        if r > 9:
            rch = chr(r+55)
        else:
            rch = str(r)
        nb2 = rch  + nb2
        dec = dec // b2
        v = dec == 0
    return nb2
        

print("Entrer la base initiale: ",end="")
b1 = saisie_base()
print("Entrer la base cible: ",end="")
b2 = saisie_base()
print("Entrer la base initiale "+str(b1)+" : ",end="")
nb1 = saisie_controlee(b1)
nb2 = convb1_b2(nb1,b1,b2)
print("(",nb1,")",b1,"=(",nb2,")",b2)

