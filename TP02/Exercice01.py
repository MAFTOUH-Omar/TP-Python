import math

def nombre_chiffres ( x ) :
    cp = 0
    while x != 0 :
        x //= 10
        cp += 1
    return cp

def diviser_chiffre (nombre):
    if nombre == 0:
        return [0]
    
    resultats = []
    while nombre > 0:
        chiffre = nombre % 10
        resultats.insert(0, chiffre)
        nombre //= 10
    
    return resultats

def calcul_nombre_amstrong ( x ) :
    nbrChiffre = nombre_chiffres(x)
    chiffresEntier = diviser_chiffre( x )
    nbrAmstrong = 0
    for i in range(0 , len(chiffresEntier)) :
        nbrAmstrong += math.pow(chiffresEntier[i] , nbrChiffre)
    return int(nbrAmstrong)

def est_un_nombre_amstrong( nombre ) :
    nbrAmstrong = calcul_nombre_amstrong(nombre)
    if nombre == nbrAmstrong :
        return True
    else :
        return False

def afficher_nombres_amstrong ( List ) :
    ListNbrAmstrong = []
    for i in range(0 , len(List)) :
        if est_un_nombre_amstrong(L[i]) :
            ListNbrAmstrong.append(L[i])
    return ListNbrAmstrong
    

L = [ 153 , 1634 , 2 , 6 , 14 ]
print(f"Liste qui continet nombre d\'amstrong : {afficher_nombres_amstrong(L)}")
print(f"Nombre de chiffre : {nombre_chiffres(10)}")
print(f"Nombre de Amstrong : {calcul_nombre_amstrong(153)}")
print(f"Verifier si un nombre d\'amstrong : {est_un_nombre_amstrong(14)}")