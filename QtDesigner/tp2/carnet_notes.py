# Pour manipuler les fichiers binaires
import pickle as pic
# Importations à faire pour réaliser une interface graphique
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtGui  # ????????


def lblMsg(ch):
    f.lblMsg.setText(ch)


def boxMsg(msg, boxMsgType):
    bMsg = QMessageBox()

    if boxMsgType == "information":
        bMsg.setIcon(QMessageBox.Information)
    else:
        bMsg.setIcon(QMessageBox.Warning)

    bMsg.setText(msg)
    bMsg.exec()


def init():
    # ajout des elements dans les comboBox
    for i in range(1, 32):
        f.cmbJ.addItem(str(i))
    for i in range(1, 13):
        f.cmbM.addItem(str(i))
    for i in range(2013, 1989, -1):
        f.cmbA.addItem(str(i))
    # cocher le button radio "Croissant"
    f.rdoCroi.setChecked(True)
    # chargement des niveaux a partir du fichier texte "niveaux.txt"

    try:
        ft = open("niveaux.txt", "r")
        ligne = ft.readline().rstrip()
        while ligne != "":
            f.lstNiveaux.addItem(ligne)
            ligne = ft.readline().rstrip()
    except:
        #boxMsg("Fichier inexistant","alert")
        # décommentez si vous voulez afficher les messages dans un label
        lblMsg("Fichier \"niveaux.txt\" inéxistant !!!")
    

def controle_date():
    nbj = 31
    mois = f.cmbM.currentIndex()+1
    if mois in {4, 6, 9, 11}:
        nbj = 30
    elif mois == 2:
        a = int(f.cmbA.currentText())
        if a % 4 == 0:
            nbj = 29
        else:
            nbj = 28
    f.cmbJ.clear()
    for i in range(1, nbj+1):
        f.cmbJ.addItem(str(i))


def controle_Formulaire():
    if f.txtNom.text() == "" or f.txtPren.text() == "":
        boxMsg("veuillez remplir tous les champs", "information")
    elif f.lstNiveaux.count() == 0:
        boxMsg("liste de niveau vide", "information")
    elif f.lstNiveaux.currentRow() == -1:
        boxMsg("aucune niveaux n'est choisi", "information")
    elif (not f.chkA.isChecked() and not f.chkE.isChecked() and not f.chkI.isChecked()):
        boxMsg("Selectioner une option", "")
    elif (f.chkA.isChecked() and f.chkE.isChecked()) or (f.chkA.isChecked() and f.chkI.isChecked()) or (f.chkE.isChecked() and f.chkI.isChecked()):
        boxMsg("Selectioner une seule option", "")
    else:
        Ajouter()


def Ajouter():
    global taille

    taille += 1
    if f.rdoM.isChecked():
        sexe = 'M'
    else:
        sexe = 'F'
    date = f.cmbJ.currentText() + "/" + f.cmbM.currentText() + \
        "/" + f.cmbA.currentText()
    if f.chkA.isChecked():
        option = "Allemand"
    elif f.chkE.isChecked():
        option = "Espagnol"
    else:
        option = "Italien"

    f.tblFiches.rowCount()
    f.tblFiches.setRowCount(taille)
    f.tblFiches.setItem(taille-1, 0, QTableWidgetItem(f.txtNom.text()))
    f.tblFiches.setItem(taille-1, 1, QTableWidgetItem(f.txtPren.text()))
    f.tblFiches.setItem(taille-1, 2, QTableWidgetItem(sexe))
    f.tblFiches.setItem(taille-1, 3, QTableWidgetItem(date))
    f.tblFiches.setItem(taille-1, 4, QTableWidgetItem(f.lstNiveaux.currentItem().text()))
    f.tblFiches.setItem(taille-1, 5, QTableWidgetItem(option))

    boxMsg("Ajouter avec succes", "information")


def Enregistrer():
    fch = open("fiches.dat", "ab")
    e = dict()
    nbRows = f.tblFiches.rowCount()
    for i in range(nbRows):
        e["nom"] = f.tblFiches.item(i, 0).text()
        e["prenom"] = f.tblFiches.item(i, 1).text()
        e["sexe"] = f.tblFiches.item(i, 2).text()
        e["date"] = f.tblFiches.item(i, 3).text()
        e["niv"] = f.tblFiches.item(i, 4).text()
        e["option"] = f.tblFiches.item(i, 5).text()

        pic.dump(e, fch)

    fch.close()

    fch = open("fiches.dat", "rb")
    end = False
    while not end:
        try:
            e = pic.load(fch)
            print(e)
        except:
            end = True

    boxMsg("Enregistrer avec succes", "")
def Trier(t, n, sb):
    pas = 0
    while pas < n:
        pas = pas * 3 + 1
    valid = False
    while not valid:
        pas = pas // 3
        for i in range(pas, n):
            aux = t[i]
            p = i - pas
            while p >= 0 and str(t[p][sb])[0] > str(aux[sb])[0]:
                t[p+pas] = t[p]
                p = p - pas
            
            t[p+pas] = aux
        valid = pas == 1
    
def Tri():
    global t
    if f.rdoCroi.isChecked():
        n = f.tblFiches.rowCount()
        t = [dict()] * n
        for i in range(n):
            e = dict()
            e["nom"] = f.tblFiches.item(i, 0).text()
            e["prenom"] = f.tblFiches.item(i, 1).text()
            e["sexe"] = f.tblFiches.item(i, 2).text()
            e["date"] = f.tblFiches.item(i, 3).text()
            e["niv"] = f.tblFiches.item(i, 4).text()
            e["option"] = f.tblFiches.item(i, 5).text()
            t[i] = e
        sortBy = f.cmbTri.currentText()
        Trier(t,n, sortBy)
        f.tblFiches.setRowCount(n)
        for i in range(1,n):
            f.tblFiches.setItem(i, 0, QTableWidgetItem(t[i-1]["nom"]))
            f.tblFiches.setItem(i, 1, QTableWidgetItem(t[i-1]["prenom"]))
            f.tblFiches.setItem(i, 2, QTableWidgetItem(t[i-1]["sexe"]))
            f.tblFiches.setItem(i, 3, QTableWidgetItem(t[i-1]["date"]))
            f.tblFiches.setItem(i, 4, QTableWidgetItem(t[i-1]["niv"]))
            f.tblFiches.setItem(i, 5, QTableWidgetItem(t[i-1]["option"]))
    else:
        n = f.tblFiches.rowCount()
        t = [dict()] * n
        for i in range(n):
            e = dict()
            e["nom"] = f.tblFiches.item(i, 0).text()
            e["prenom"] = f.tblFiches.item(i, 1).text()
            e["sexe"] = f.tblFiches.item(i, 2).text()
            e["date"] = f.tblFiches.item(i, 3).text()
            e["niv"] = f.tblFiches.item(i, 4).text()
            e["option"] = f.tblFiches.item(i, 5).text()
            t[i] = e
        sortBy = f.cmbTri.currentText()
        Trier(t, n, sortBy)
        f.tblFiches.setRowCount(n)
        for i in range(1,n):
            f.tblFiches.setItem(i, 0, QTableWidgetItem(t[n-i-1]["nom"]))
            f.tblFiches.setItem(i, 1, QTableWidgetItem(t[n-i-1]["prenom"]))
            f.tblFiches.setItem(i, 2, QTableWidgetItem(t[n-i-1]["sexe"]))
            f.tblFiches.setItem(i, 3, QTableWidgetItem(t[n-i-1]["date"]))
            f.tblFiches.setItem(i, 4, QTableWidgetItem(t[n-i-1]["niv"]))
            f.tblFiches.setItem(i, 5, QTableWidgetItem(t[n-i-1]["option"]))

app = QApplication([])       # Création d'une instance d'application
f = loadUi("interface.ui")      # charger le fichier crée par Qt Designer
f.show()  # Afficher la fenêtre
taille = 0
init()

f.btnAjouter.clicked.connect(controle_Formulaire)
# le module contole_date est appelé à tous changement de mois ou d'année
f.cmbM.currentIndexChanged.connect(controle_date)
f.cmbA.currentIndexChanged.connect(controle_date)
f.btnEng.clicked.connect(Enregistrer)
f.cmbTri.currentIndexChanged.connect(Tri)
f.rdoCroi.clicked.connect(Tri)
f.rdoDecroi.clicked.connect(Tri)
app.exec_()                            # exécution de l'application
