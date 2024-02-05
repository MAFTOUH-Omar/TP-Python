# Initialisation du dictionnaire D
D = {
    "nombre_mots": 0,
    "frequence_mots": {},
    "longueur_moyenne": 0,
    "mot_le_plus_long": ""
}

# Demander à l'utilisateur d'entrer un texte
text = input("Entrez un texte : ")

# Compter le nombre de mots dans le texte
nombreMots = text.split()
D['nombre_mots'] = len(nombreMots)

# Calculer la fréquence de chaque mot dans le texte saisi
for mot in nombreMots:
    if mot in D['frequence_mots']:
        D['frequence_mots'][mot] += 1
    else:
        D['frequence_mots'][mot] = 1

# Calculer la longueur moyenne des mots
D['longueur_moyenne'] = sum(len(mot) for mot in nombreMots) / D['nombre_mots']

# Trouver le mot le plus long
D['mot_le_plus_long'] = max(nombreMots, key=len)

# Afficher le dictionnaire résultant
print(D)