import numpy as np

array1 = np.array([[1 , 2] , [3 , 4]])
array2 = np.array([[9 , 10] , [11 , 12]])

# Concatenate
# print(f"Axe 01 : \n{np.concatenate((array1 , array2) , axis = 1)}") # [[1 2 5 6] [3 4 7 8]]
# print(f"Axe 00 : \n{np.concatenate((array1 , array2) , axis = 0)}") # [[1 2]   [3 4]   [5 6]   [7 8]]  

#Stack
# print(f"stack axis 1 : \n{np.stack((array1 , array2) , axis=1)}")
# print(f"stack axis 0 : \n{np.stack((array1 , array2) , axis=0)}")

# HStack
# print(f"Hstack : \n{np.hstack((array1 , array2))}")
# print(f"Vstack : \n{np.vstack((array1 , array2))}")
# print(f"Dstack : \n{np.dstack((array1 , array2))}")


test = np.array([[7 , 5 , 7] 
                , [8 , 2 , 1] 
                , [7 , 2 , 7] 
                ])

print(np.unique(test , axis=1 , return_counts=True))
