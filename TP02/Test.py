import numpy as np
def diviser_chiffre (nombre):
    if nombre == 0:
        return [0]
    
    resultats = []
    while nombre > 0:
        chiffre = nombre % 10
        resultats.insert(0, chiffre)
        nombre //= 10
    
    return resultats
print(f"Chiffre format diviser : {diviser_chiffre(10)}")

# Exercice01 :
# pour qoui en utilisant la // 10 pour calculer le nombre d'element , car tous les nombre sont sur la base 10
# 153 // 10 = 15 // 10 = 1 // 10 = 0
