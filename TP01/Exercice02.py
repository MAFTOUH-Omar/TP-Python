# Initialisation du text
text = "La filière D3SI de la FPBM, est une filière d'execellence du nouveau système lancé par le ministére de l'enseignement supérieur. En plus de la filière D3SI, nous trouvons la filière I3DIA, nous trouvons la filière I3DIA et la filière IOR"

# Diviser le text on utiliser la fonction split et stoker la resultat dans liste mots
mots = text.split()

# Initialiser la liste mots_traites
mots_traites = []

# Vérifier si une mot continet vergule ou point a la fin
for i in mots :
    if i[-1] == '.' or i[-1] == ',' :
        motsSontVergule = i.replace('.' , '').replace(',' , '')
        mots_traites.append(motsSontVergule)

# Afficher les mots traites
print(f"Les mots Traiter : {mots_traites[:]}")

# Convertir chaque mot de la liste mots_traites en miniscule et stocker dans mots_min
mots_min = []
for i in mots_traites :
    motsMiniscule = str(i)
    mots_min.append(motsMiniscule.lower())

# Afficher mots_min
print(f"les mots en miniscule : {mots_min[:]}")

# Trier les les mots de la liste mots_in et stoker le résultat dans une nouvelle liste mots_min_len
mots_min_len = []
motsMinLen = sorted(mots_min , key=len , reverse=True)
mots_min_len.append(motsMinLen)
print(f"les mots min len : {mots_min_len[:]}")

# Inialiser le dictinnaire frequence 
frequence = {}

# Initialiser un compteur qui compter le nombre de frequence et stocker dans le dictinnaire frequence 
cp = 0
for i in range(0 , len(mots_min)) :
    for j in range(0 , len(mots_min)):
        if mots_min[i] == mots_min[j] :
            cp += 1
    frequence[mots_min[i]] = cp        
    cp = 0
print(f"le dictionnaire frequence : {frequence}")

# Initisaliser la liste mots_min_frequence
mots_min_frequence = []

# Trier les mots de la liste mots_min par sorted & stocker dans mots_min_frequence
motsMinSorted = sorted(mots_min , key=lambda x : (-frequence[x] , x))
mots_min_frequence.append(motsMinSorted)
print(f"Mots min Frequence : {mots_min_frequence}")