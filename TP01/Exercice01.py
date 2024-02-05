# Initialisation deux listes vides L & P
L = []
P = []

# Proposer a l'utilisateur de saisi le nombre d'elements qu'il doit etre dans la list
n = int(input("Saisir le nombre d'éléments :"))

# Remplir la liste L par nombre d'element n
for i in range(1 , n+1) :
    element = int(input(f"Saisir l'elemnt nombre {i} : "))
    # La remplissage de la liste L par éléments
    L.append(element)
print(f"Votre Liste est : {L[:]}")

# Le trie par insertion sur la liste L
for i in range(1 , len(L)) :
    cle = L[i]
    j = i - 1
    while j >= 0 and cle < L[j]: 
        temp = L[j]
        L[j] = L[j + 1]
        L[j + 1] = temp
        j -= 1

# La liste après le trie par insertion
print(f"La liste triée : {L[:]}")

# Identification du les nombre premier dans la liste P & supprimer apartir la list L
i = 0
while i < len(L) :
    nombre = L[i]
    if nombre > 1 :
        premier = True
        for j in range(2 , nombre):
            if nombre % j == 0 :
                premier = False
                break
        if premier :
            P.append(nombre)
            L.pop(i)
        else :
            i += 1
    else :
        i += 1
# L'affichage de la liste P & L
print(f"La liste P : {P[:]}")
print(f"La liste L : {L[:]}")