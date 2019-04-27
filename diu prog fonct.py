#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jp
#
# Created:     26/04/2019
# Copyright:   (c) jp 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import json

def saisie():
    r=[]
    liste=[]

    nbq=int(input("Nombre de question(s): "))
    j=0

    while j<nbq:
        a="Titre de la question n°"+str(j+1)+": "
        t=input(a)
        ty=input("Type de la question: (ouverte (o) / choix multiple (c) ")
        q="Entrez la question n°"+str(j+1)+": "
        q=input(q)
        cc=1
        i=0

        if ty=="c":
            n=int(input("Nombre de réponse(s): "))
            cc=int(input("Nombre de réponse(s) correcte(s): "))
        else:
            n=1

        while i<n:
            a="Entrez la réponse n°"+str(i+1)
            a=input(a)

            ind=0
            if ty=="c":
                v=input("Cette réponse est-elle juste? (o/n): ")
                if v=="o":
                    ind=1

            if ty=="o":
                ind=1

            r.append((a,ind))


            i+=1

        k=0
        while k<=(5-len(r)):
            r.append((0,0))
            k+=1



        liste.append({"titre":t,"type":ty,"question":q,"nb_repc":cc,
                   "rep1":r[0],"rep2":r[1],"rep3":r[2],"rep4":r[3]})

        r=[]
        j+=1
    return (liste)



def sauver_json ( mf , liste ):
    with open( mf ,"w", newline ="", encoding ="utf -8") as jsonfile :
        json . dump (liste , jsonfile )

def lire_json ( mf ):
    with open( mf ,"r", newline ="", encoding ="utf -8") as jsonfile :
        l = json . load ( jsonfile )
    return l

liste=saisie()
print (liste)

mf="fi.json"
sauver_json ( mf , liste )

lis=lire_json ( mf )
