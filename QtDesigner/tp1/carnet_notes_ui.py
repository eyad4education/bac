from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import numpy as  np   
import pickle as pic



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
        pic.dump(t[i],f)
    f.close()
def afficher(fchb):
    f=open(fchb,'rb')
    fin_fichier=False
    n = 0
    while fin_fichier == False :
        try:
            e = pic.load(f)
            n=n+1
        except:
            fin_fichier = True
    print(n)
    """
    f.close()
    f=open(fchb,'rb')
    for i in range(n):
        enrg = load(f)
        print(enrg)
        fen.tblNotes.setRowCount(long)
        fen.tblNotes.setItem(0, i, QTableWidgetItem(enrg["np"]))
        fen.tblNotes.setItem(0, i+1, QTableWidgetItem(str(12.50)))
        fen.tblNotes.setItem(0, i+2, QTableWidgetItem(str(9.35)))
        fen.tblNotes.setItem(0, i+3, QTableWidgetItem(str(13)))
        fen.tblNotes.setItem(0, i+4, QTableWidgetItem(str(12.50)))
    
    f.close()
"""

    
    
ft=open('notes.txt','r')
transferer(ft)
tri(t,n)
f=open('notes.dat','wb')
reecrire(t,n,f)
fchb = "notes.dat"


app=QApplication([])
fen=loadUi("interface.ui")
fen.show()
fen.btnAfficher.clicked.connect(afficher)


app.exec_() 




