import numpy as np

# Définir la moyenne et l'écart-type
moyenne = 3
ecart_type = 2

# Générer le tableau de valeurs aléatoires suivant une distribution normale
tab_random = np.random.normal(moyenne, ecart_type, 12)
print(f"tab_random : \n{tab_random}")

# Redimensionner tab_random en une matrice(mat1) de taille 3,4
mat1 = tab_random.reshape(3 , 4)  
print(f"mat1 : \n{mat1}")

# Remplacez toutes les valeurs de la matrice mat1 par leur valeur entière inférieure
print(f"valeur entière inférieure du matrice mat1 : \n{np.floor(mat1)}")

# Convertir les éléments de mat1 en int
mat1 = np.int64(mat1)
# Ou mat1 = mat1.astype(int)
print(f"les elements du mat1 format int : \n{mat1}")

# Creation du matrice mat2 de taille 4,3 avec des valeur entre 2 et 14
mat2 = np.arange(2 , 14)
mat2_reshaped = mat2.reshape(4 , 3)
print(f"mat2 : {mat2_reshaped}")

# Calculer la multiplication matricielle de mat1 et mat2
print(f"La multiplication du mat1 & mat2 : \n{np.dot(mat2_reshaped , mat1)}")

# Calculer la transposée de la première matrice mat1
print(f"Transpose du mat1 : \n{mat1.T}")

# Creation d'une nouvelle matrice carrée 3x3 en excluant la dernière colonne de la matrice mat1
matCarree = np.array([mat1[ : , :-1]])
print(f"Matrice Carree 3*3 : \n{matCarree}")
inverseMat1 = None
# Trouver l'inverse de la matrice mat1
if np.linalg.det(matCarree) != 0 :
    inverseMat1 = np.linalg.inv(matCarree)
    inverseMat1 = np.round(inverseMat1 , 2)
    print(f"Inverse du mat1 : \n{inverseMat1}")
else :
    print("Determinant egale 0")

# Multipliez la matrice résultante de l'inversion par la matrice originale
if inverseMat1 is not None :
    idnt = np.dot(inverseMat1 , matCarree)
    idnt = np.round( idnt , 2 ) 
    print(f"Matrice identité : \n{idnt}")
else :
    print("Invalide inversse")