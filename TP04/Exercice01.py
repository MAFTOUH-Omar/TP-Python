import numpy as np

# Creation d'un tab Numpy 2d qui continer 12 ligne 3 colone , avce des valeur aléatoire entre 100 & 1000
tab2D = np.random.randint(100 , 1000 , size=(12 , 3))
print(f"Tab 2D : \n{tab2D}")

print('*' * 50)

# Calculer et afficher le total des ventes pour chaque produit sur l'ensemble de l'année
print(f"Total des ventes du P1 : {np.sum(tab2D[ : , 0])}")
print(f"Total des ventes du P2 : {np.sum(tab2D[ : , 1])}")
print(f"Total des ventes du P3 : {np.sum(tab2D[ : , 2])}")

print('*' * 50)

# Calculer et afficher la moyenne des ventes mensuelles pour chaque produit
print(f"Moyenne des ventes du P1 : {np.round(np.mean(tab2D[ : , 0]) , 2)}")
print(f"Moyenne des ventes du P2 : {np.round(np.mean(tab2D[ : , 1]) , 2)}")
print(f"Moyenne des ventes du P3 : {np.round(np.mean(tab2D[ : , 2]) , 2)}")

print('*' * 50)

# L'indentification le mois ayant les ventes maximales pour chaque produit
print(f"Le mois ayant les ventes maximales P1 : {np.argmax(tab2D[ : , 0]) + 1}")
print(f"Le mois ayant les ventes maximales P2 : {np.argmax(tab2D[ : , 1]) + 1}")
print(f"Le mois ayant les ventes maximales P3 : {np.argmax(tab2D[ : , 2]) + 1}")

print('*' * 50)

# Calculer la croissance mensuelle
TauxCroissance = ( np.diff(tab2D , axis=0) / tab2D[:-1] ) * 100
print(f"Taux de coissance du 3 Produits : \n{ np.int64(TauxCroissance) }")

print('*' * 50)

# Identifier et afficher le mois avec la plus forte croissance pour chaque produit
print(f"le mois le plus forte croissance pour P1 : { np.argmax(TauxCroissance[ : , 0])+1 }")
print(f"le mois le plus forte croissance pour P2 : { np.argmax(TauxCroissance[ : , 1])+1 }")
print(f"le mois le plus forte croissance pour P3 : { np.argmax(TauxCroissance[ : , 2])+1 }")

print('*' * 50)

# La creation d'un tableau 1D contenant la somme des ventes pour chaque mois
tab1D = np.array(np.sum(tab2D , axis=1))
print(f"Somme des ventes pour chaque mois : \n{tab1D}")