# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 08:23:26 2020

@author: erwan
"""
import random



DataBaseMots = ["bouillabaisse","tomate","tronc", "exploiter","astuce","usine","mannequin","eluder","appartement","dictionnaire","militaires","tranborder","photos","mortel","prehistorique","plume","speculos","morne","menacer","frontiere","histoire","bouquet","diamant","divorce","macis","caillot","revendeur","proverbe","paroles","courageux","transatlantique"]



def fTriTailleMots(L):
    Ltri = sorted(L,key=len)
    return(Ltri)

def fTriAlphabMots(L):
    Ltri = sorted(L)
    return Ltri

def fTri(L):
    Ltri = fTriTailleMots(fTriAlphabMots(L))
    return(Ltri)

def fChoixMot(L):
    
    i_alea = random.randint(0,len(L)-1)
    m_alea = L[i_alea]
    return(m_alea)

def fAffichageInitMot(mot):
    affichage_init=""
    mot=str(mot)
    lettre1 = mot[0]
    for l in mot:
        if l == lettre1:
            affichage_init+=l
        else:
            affichage_init+="_"
    return(affichage_init)
    
def fDemandeLettre():
    l = input("Essayez de deviner une lettre : ")
    lettre = str(l)
    return(lettre)
    
def fVerifPresenceLettre(l,mot,motcrypeactuel):
    l=str(l)
    nouveaumotcrypte = motcrypeactuel
    for i,val in enumerate(mot):
        if l==val:
            nouveaumotcrypte = nouveaumotcrypte[0:i]+l+nouveaumotcrypte[i+1:]

    return(nouveaumotcrypte)

    
    
def fJeuPendu():
    
    tentatives = 8
    Lmots = fTri(DataBaseMots)
    mot = fChoixMot(Lmots)
    motcrypte = fAffichageInitMot(mot)
    ancienmotcrypte = motcrypte
    LStockLettre=[]
    
    while tentatives>0:
        
    
        
        print("Vous devez deviner  : ", ancienmotcrypte)
        l = fDemandeLettre()
        if l not in LStockLettre:
            
            LStockLettre.append(l)
            nouveaumotcrypte = fVerifPresenceLettre(l,mot,ancienmotcrypte)
            if ancienmotcrypte != nouveaumotcrypte:
                print("Bien joué")
                ancienmotcrypte = nouveaumotcrypte
                if ancienmotcrypte == mot:
                    print("Vous avez gagné, le mot était : ", mot)
                    break

                
    
            else:
                tentatives-=1
                print("Dommage")
                print("Nombre de tentatives restantes : ",tentatives)
        else: print("Lettre deja tentée")
    
    if tentatives==0:
        print("Vous avez perdu")

    q = input("Voulez-vous rejouer ? (y/n)")
    if q=="n": 
            False
    elif q == "y":
        fJeuPendu()
    
    
    
    
    
fJeuPendu()
