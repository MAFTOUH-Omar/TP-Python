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
print(f"Le mois ayant les ventes maximales P1 : {np.argmax(tab2D[ : , 0])}")
print(f"Le mois ayant les ventes maximales P2 : {np.argmax(tab2D[ : , 1])}")
print(f"Le mois ayant les ventes maximales P3 : {np.argmax(tab2D[ : , 2])}")

print('*' * 50)

# Calculer la croissance mensuelle
print(f"Taux de coissance du P1 : \n{( tab2D[ : , 0 ] - np.diff(tab2D[ : , 0 ] , prepend = 0 ) / np.diff(tab2D[ : , 0 ] , prepend = 0 ) ) * 100}")
print(f"Taux de coissance du P2 : \n{( tab2D[ : , 1 ] - np.diff(tab2D[ : , 1 ] , prepend = 0 ) / np.diff(tab2D[ : , 1 ] , prepend = 0 ) ) * 100}")
print(f"Taux de coissance du P3 : \n{( tab2D[ : , 0 ] - np.diff(tab2D[ : , 2 ] , prepend = 0 ) / np.diff(tab2D[ : , 2 ] , prepend = 0 ) ) * 100}")

print('*' * 50)

# Identifier et afficher le mois avec la plus forte croissance pour chaque produit
