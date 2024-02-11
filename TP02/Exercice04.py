def verifie_dimensions():
    # Fonction pour vérifier si les dimensions des matrices sont compatibles pour le produit matriciel.
    while True:
        m = int(input("Entrez le nombre de lignes de la matrice A : "))
        n = int(input("Entrez le nombre de colonnes de la matrice A et le nombre de lignes de la matrice B : "))
        p = int(input("Entrez le nombre de colonnes de la matrice B : "))
        
        # Vérifie si le nombre de colonnes de A est égal au nombre de lignes de B
        if n == p:
            # Si les dimensions sont compatibles, retourne les valeurs m, n, p
            return m, n, p
        else:
            # Si les dimensions ne sont pas compatibles, demande à l'utilisateur de réessayer
            print("Les dimensions des matrices ne sont pas compatibles. Veuillez réessayer.")


def initialiser_matrice(R, C):
    # Initialise une liste vide pour stocker les lignes de la matrice
    matrice = []
    
    # Boucle sur le nombre de lignes R
    for _ in range(R):
        # Initialise une liste vide pour stocker les éléments de chaque ligne
        ligne = []
        # Boucle sur le nombre de colonnes C
        for _ in range(C):
            # Ajoute un zéro à la ligne pour chaque colonne
            ligne.append(0)
        # Ajoute la ligne complète à la matrice
        matrice.append(ligne)
    
    return matrice

def remplir_matrice(R, C):
    # Remplit une liste bidimensionnelle pour représenter une matrice avec les entrées de l'utilisateur.
    matrice = initialiser_matrice(R, C)
    print("Entrez les éléments de la matrice :")
    for i in range(R):
        for j in range(C):
            matrice[i][j] = float(input(f"Entrez l'élément [{i + 1},{j + 1}] : "))
    return matrice


def calcul_produit_matriciel(A, B, m, n, p):
    # Calcule le produit matriciel de A et B.
    # Initialise la matrice résultante C avec des zéros
    C = initialiser_matrice(m, p)
    
    # Effectue le produit matriciel
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    
    return C


# Main code
# Demande à l'utilisateur de saisir les dimensions des matrices et les vérifie
m, n, p = verifie_dimensions()

# Remplit les matrices A et B avec les entrées de l'utilisateur
print("Pour la matrice A :")
A = remplir_matrice(m, n)
print("Pour la matrice B :")
B = remplir_matrice(n, p)

# Calcule le produit matriciel de A et B
produit_matriciel = calcul_produit_matriciel(A, B, m, n, p)

# Affiche la matrice résultante
print("Le produit matriciel de A et B est :")
for row in produit_matriciel:
    print(row)