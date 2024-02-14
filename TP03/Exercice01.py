# Importation du bibliothèque NumPy en utilisant l'alias np
import numpy as np

# Creation un tableau 1D appelé tab1 avec les entiers de 0 à 5
tab1 = np.array([0 , 1 , 2 , 3 , 4 , 5])

# Creation d'un tableau 2D de taille 3,3 , remplit avec des entiers aléatoires(entre 1 et 10)
tab2 = np.random.randint(1 , 11 , size=(3,3))

# Ajouter 2 à chaque élément du tab1
np.add(tab1 , 2)

# Multiplier chaque élément de tab2 par 2
np.multiply(tab2 , 2)

# Afficher la forme et la dimension des deux tableaux
print(f"Forme du tab1 : {tab1} , dimension du tab1 : {tab1.ndim}") # tab 01
print(f"Forme du tab2 : {tab2} , dimension du tab2 : {tab2.ndim}") # tab 02

# Afficher le nombre des lignes et des colonnes de tab2
print(f"Nombre du ligne du tab2 : {tab2.shape[0]} , Nombre du colone du tab2 : {tab2.shape[1]}")

# Afficher la deuxième ligne de tab2
print(f"la deuxième ligne de tab2 : {tab2[1]}")

# Afficher un sous-tableau 2x2 de tab2 en excluant la première ligne et la première colonne
print(f"tab2 sans ligne 1 & colone 1 : {tab2[ 1 : , 1 : ]}")

# les indices des valeurs maximales & minimales le long de l'axe 0 dans le tableau tab2.
print(f"Les indices des valeurs maximales de le long axe 0 : {np.argmax(tab2 , axis=0)}")
print(f"Les indices des valeurs minimales de le long axe 0 : {np.argmin(tab2 , axis=0)}")

# les indices des valeurs maximales & minimales le long de l'axe1 dans le tableau tab2.
print(f"Les indices des valeurs maximales de le long axe 1 : {np.argmax(tab2 , axis=1)}")
print(f"Les indices des valeurs minimales de le long axe 1 : {np.argmin(tab2 , axis=1)}")

"""
        Creation du tableau booléen sup_a_3 de même taille que tab1, où chaque élément est égal à
    True si l’élément correspond dans tab1 est supérieur à 3, sinon la valeur est False
"""
sup_a_3 = np.array(tab1 > 3 , ndmin=(tab1.ndim))
print(f"Superieur a 3 : {sup_a_3}")

# les éléments de tab1 qui sont supérieurs à 3 , en utilisant le masque
print(f"Les elements sup que 3 dans tab1 : {tab1[sup_a_3]}")

# Redimensionner tab1 en un tableau2D de taille 2x3.
tab1_reshaped = tab1.reshape(2 , 3)
print(f"Tab1 en format 2D et de taille 2*3 : {tab1_reshaped}")

# La creation du tableau tab3 de la forme suivante : [4, -5, 2]
tab3 = np.array([4 , -5 , 2])

# Ajouter le tableau tab3 comme nouvelle ligne au tableau tab1
tab4 = np.vstack((tab1_reshaped , tab3))
print(f"Tab4 : {tab4}")

# Calculer la somme des éléments de tab4
print(f"La somme d\'element du tab4 : {np.sum(tab4)}")

# Calculez la moyenne de chaque colonne de tab2
print(f"Calculer la moyenne des element du tab2 de chaque colonne : {np.round(np.mean(tab2 , axis=1) , 2)}")