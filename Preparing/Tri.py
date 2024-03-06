import array as arr

tab = arr.array('i')

n = int(input('Entrez nombre d\'element pour tab : '))

for i in range (n) :
    x = int(input(f"Entrez l\'element num {i+1} : "))
    tab.append(x)

for i in range (len(tab)):
    print(f"{tab[i]} , ", end=" ")

# Trie par selection
for i in range(n-1) :
    min = i
    for j in range(i+1 , n):
        if tab[j] < tab[min] :
            min = j
    if min != i :
        tab[i] , tab[min] = tab[min] , tab[i]

# Trie par bull
for i in range(n , -1 , -1) :
    for j in range(1 , i) :
        if tab[j] < tab[j-1] :
            tab[j] , tab[j-1] = tab[j-1] , tab[j]

# Trie par insertion
for i in range (1 , n) :
    key = tab[i]
    j = i - 1
    while j >= 0 and key < tab[j] :
        tab[j + 1] = tab[j]
        j -= 1
    tab[j + 1] = key

# Recherche sequenciel
rech = int(input("Rech : "))
pos = -1
for i in range(n) :
    if tab[i] == rech :
        pos = i

# recherche dicho
debut = 0
fin  = n-1
arret = False
while debut <= fin and arret == False :
    milieu = (debut + fin) // 2
    if rech == tab[milieu] :
        pos = milieu
        arret = True
    else :
        if rech < tab[milieu] :
            fin = milieu - 1
        else : 
            debut = milieu + 1