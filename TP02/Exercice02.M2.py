def changer_car( chaine , car1 , car2 , debut , fin = None) :
    if fin == None or fin == -1 :
        fin = len(chaine) - 1
    chaineToList = chaine.split()
    for i in range(debut , fin) :
        if chaineToList[i] == car1 :
            chaineToList[i] = car2 
    return str(chaineToList)

text = input('Entrez : ')
car01Input = input('Entrez car01 : ')
car02Input = input('Entrez car02 : ')
debutInput = int(input('Entrez la point du debut : '))
finInput = int(input('Entrez la point du fin : '))
 
print(changer_car(text , car01Input , car02Input , debutInput , finInput))