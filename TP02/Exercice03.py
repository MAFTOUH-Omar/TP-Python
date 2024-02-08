def verifie_ordre ( list ) :
    order = False
    cle01 , cle02 , cle03 = 0 , 0  ,0
    for i in range(0 , len(list)) :
        if list[i] == 1 :
            cle01 = i
        elif list[i] == 2 :
            cle02 = i
        elif list[i] == 3 :
            cle03 = i
    if ( cle01 < cle02 and cle01 < cle03 ) or ( cle02 > cle01 and cle02 < cle03 ) :
        order = True

    return order

L00 = [ -1 , 6 , 7 , 1 , 2 , 3 , 5 ]
L01 = [ 9 , 1 , 7 , 4 , 2 , 5 , 3 ]
L02 = [ 6 , 3 , 12 , 2 , -4 , 5 , 1 ]

print(verifie_ordre(L01))