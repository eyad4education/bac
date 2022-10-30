import numpy as np
from pickle import load,dump

def transferer(ft):
    global n,t
    ligne=ft.readline()
    n=0
    t=np.array([dict()]*100)
    while ligne!='' :
        enrg={}
        enrg['np']=ligne[:ligne.find('-')]
        ligne=ligne[ligne.find('-')+1:]
        enrg['dc1']=float(ligne[:ligne.find('-')])
        ligne=ligne[ligne.find('-')+1:]
        enrg['dc2']=float(ligne[:ligne.find('-')])
        ligne=ligne[ligne.find('-')+1:]
        enrg['ds']=float(ligne)
        enrg['moy']=(enrg['dc1']+enrg['dc2']+2*enrg['ds'])/4
        t[n]=enrg
        n+=1
        ligne=ft.readline()
    ft.close()
        
def tri (t,n):
    sortie=False
    while sortie==False:
        permut=False
        for i in range(n-1):
            if t[i+1]['moy']>t[i]['moy']:
                aux=t[i+1]
                t[i+1]=t[i]
                t[i]=aux
                permut=True
        sortie=(permut==False)
             

def reecrire (t,n,f):
    for i in range(n):
        dump(t[i],f)
    f.close()
def afficher(f):
    fin_fichier=False
    while fin_fichier == False :
        try :
            enrg= load (f)
            print (enrg ["np"],"\t moyenne:",enrg["moy"])
        except :
            fin_fichier = True
    f.close ( )
    
             

######### PP ##########
ft=open('notes.txt','r')
transferer(ft)
tri(t,n)
f=open('notes.dat','wb')
reecrire(t,n,f)
f=open('notes.dat','rb')
afficher(f)