def verifie_ordre ( list ) :
    D = {
        1 : -1,
        2 : -1,
        3 : -1
    }
    j = 0
    for i in list :
        if i == 1 or i == 2 or i == 2 :
            D[i] = j
            j += 1
    for i in range( 1 , 3 ) :
        return D[ i ] < D[ i + 1 ]

L00 = [ -1 , 6 , 7 , 1 , 2 , 3 , 5 ]
L01 = [ 9 , 1 , 7 , 4 , 2 , 5 , 3 ]
L02 = [ 6 , 3 , 12 , 2 , -4 , 5 , 1 ]

print(verifie_ordre(L01))