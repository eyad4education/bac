import math
n = 3
T = [str()] * n

for i in range(3):
    v1 = False
    while not v1:
        ch = str(input(f"saisir l'identifiant numero {i+1} : "))
        v2 = False
        j = -1
        while not v2:
            j = j + 1
            v2 = not (ch[j] == "0" or ch[j] == "1") or (j == len(ch)-1)
        v1 = ch[j] == "0" or ch[j] == "1"
        
    T[i] = ch

    


print(T)
