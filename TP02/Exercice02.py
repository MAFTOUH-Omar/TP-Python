def changer_car(chaine, car1, car2, debut=None, fin=None):
    # Si debut n'est pas spécifié, on le définit 0
    if debut is None:
        debut = 0
    # Si fin n'est pas spécifié, on le définit le dernier caractère de la chaîne
    if fin is None:
        fin = len(chaine) - 1
    
    # Initialise une nouvelle chaîne vide pour stocker le résultat du remplacement
    nouvelle_chaine = ''
    
    # Parcours de chaque caractère de la chaîne originale
    for i in range(len(chaine)):
        # Vérifie si l'indice actuel est compris entre debut et fin
        if debut <= i <= fin:
            # Si le caractère à l'indice i est égal à car1, le remplace par car2
            if chaine[i] == car1:
                nouvelle_chaine += car2
            # Si le caractère n'est pas égal à car1, le conserve tel quel
            else:
                nouvelle_chaine += chaine[i]
        # Si l'indice n'est pas dans la plage spécifiée, conserve le caractère tel quel
        else:
            nouvelle_chaine += chaine[i]
    
    # Retourne la nouvelle chaîne avec les remplacements effectués
    return nouvelle_chaine

# Exemple d'utilisation
chaine = "Le Lorem Ipsum est simplement"
# Appelle la fonction changer_car avec les arguments spécifiés
nouvelle_chaine = changer_car(chaine, 'o', 'a', 3, 10)
# Affiche la nouvelle chaîne obtenue après le remplacement
print(nouvelle_chaine)