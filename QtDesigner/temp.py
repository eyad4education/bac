def saisie():
    global n
    test=False
    while test==False:
        n=int(input('Enter la taille du tableau 3-20:'))
        test=3<=n<=20

def remplir(n):
    global t
    t=[0]*n
    for i in range(n):
        t[i]=int(input())


def tri_shell(t,n):
    pas=0
    while pas<n:
        pas=3*pas+1
    while pas!=0:
        pas=pas//3
        for i in range (pas,n):
            aux=t[i]
            p=i-pas
            while p>=0 and t[p]>aux:
                t[p+pas]=t[p]
                p=p-pas
            t[p+pas]=aux
            
def afficher(t,n):
    print('*********** Après Le Tri *********')
    for i in range(n):
        print(t[i],end=' | ')
############ Programme Principale ##########
print('------------ Tri Shell -----------')         
saisie()
remplir(n)
tri_shell(t,n)
afficher(t,n)