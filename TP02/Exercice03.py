def verifie_ordre(liste):
    # Initialise une variable pour stocker si l'ordre est vérifié, initialement à False
    order = False
    # Initialise les clés pour les nombres 1, 2 et 3 à 0
    cle01, cle02, cle03 = 0, 0, 0
    
    # Parcourt chaque élément dans la liste
    for i in range(0, len(liste)):
        # Si l'élément est égal à 1, met à jour la clé pour 1
        if liste[i] == 1:
            cle01 = i
        # Si l'élément est égal à 2, met à jour la clé pour 2
        elif liste[i] == 2:
            cle02 = i
        # Si l'élément est égal à 3, met à jour la clé pour 3
        elif liste[i] == 3:
            cle03 = i
            
    # Vérifie si l'ordre est vérifié
    if (cle01 < cle02 and cle01 < cle03) or (cle02 > cle01 and cle02 < cle03):
        # Si les conditions sont satisfaites, met à jour la variable order à True
        order = True

    # Retourne l'indicateur d'ordre
    return order

# Définit trois listes pour tester la fonction
L00 = [-1, 6, 7, 1, 2, 3, 5]
L01 = [9, 1, 7, 4, 2, 5, 3]
L02 = [6, 3, 12, 2, -4, 5, 1]

# Appelle la fonction pour tester avec la liste L01 et affiche le résultat
print(verifie_ordre(L01))  # Output: True