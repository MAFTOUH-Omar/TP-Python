def nombre_chiffres(x):
    # Initialise un compteur de chiffres à 0
    cp = 0
    # Boucle tant que x est différent de zéro
    while x != 0:
        x //= 10
        cp += 1
    # Retourne le nombre de chiffres dans x
    return cp

def calcul_nombre_amstrong(x):
    # Obtient le nombre de chiffres dans x en appelant la fonction nombre_chiffres
    nbrChiffre = nombre_chiffres(x)
    # Initialise une liste pour stocker les chiffres de x
    chiffresEntier = []
    # Boucle tant que x est supérieur à zéro
    while x > 0:
        # Obtient le dernier chiffre de x
        chiffre = x % 10
        # Insère le chiffre au début de la liste des chiffres
        chiffresEntier.insert(0, chiffre)
        # Division entière de x par 10 pour enlever le dernier chiffre
        x //= 10
    # Initialise le nombre d'Armstrong à zéro
    nbrAmstrong = 0
    # Boucle sur chaque chiffre dans la liste des chiffres
    for i in range(0, len(chiffresEntier)):
        # Ajoute la puissance de chaque chiffre au nombre de chiffres de x
        nbrAmstrong += chiffresEntier[i] ** nbrChiffre
    # Retourne le nombre d'Armstrong calculé
    return int(nbrAmstrong)

def est_un_nombre_amstrong(nombre):
    # Calcule le nombre d'Armstrong pour le nombre donné
    nbrAmstrong = calcul_nombre_amstrong(nombre)
    # Vérifie si le nombre est égal à son nombre d'Armstrong
    if nombre == nbrAmstrong:
        return True
    else:
        return False

def afficher_nombres_amstrong(List):
    # Initialise une liste pour stocker les nombres d'Armstrong
    ListNbrAmstrong = []
    # Parcourt chaque élément de la liste donnée
    for i in range(0, len(List)):
        # Vérifie si l'élément est un nombre d'Armstrong en appelant la fonction est_un_nombre_amstrong
        if est_un_nombre_amstrong(List[i]):
            # Ajoute l'élément à la liste des nombres d'Armstrong
            ListNbrAmstrong.append(List[i])
    # Retourne la liste des nombres d'Armstrong trouvés dans la liste donnée
    return ListNbrAmstrong

# Liste de nombres à vérifier
L = [153, 1634, 2, 6, 14]

# Affiche la liste des nombres d'Armstrong trouvés dans la liste L
print(f"Liste contenant des nombres d'Armstrong : {afficher_nombres_amstrong(L)}")

# Affiche le nombre d'Armstrong pour le nombre 23
print(f"Nombre d'Armstrong pour 23 : {calcul_nombre_amstrong(23)}")

# Vérifie si le nombre 14 est un nombre d'Armstrong
print(f"Vérification si 14 est un nombre d'Armstrong : {est_un_nombre_amstrong(14)}")