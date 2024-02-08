def changer_car( chaine , car1 , car2 , debut , fin) :
    chaineToList = chaine.split()
    for i in range(debut , fin) :
        if chaineToList[i] == car1 :
            chaineToList[i] = car2 
    return str(chaineToList)

text = "omar maftouh ddofs201 khouribga omar"
print(changer_car(text , 'omar' , 'omar01' , 0 , 5))