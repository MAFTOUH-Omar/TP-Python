import numpy as np

# arrD01 = np.array([1 , 2 , 3 , 4 , 5])

# print(type(arrD01)) # <class ’numpy.ndarray’>

# print(np.linspace(0, 1, 5)) # [0.   0.25 0.5  0.75 1.  ]

# """"
#     Data Type : np.int32 , np.float32 , np.bool , np.string , np.dateTime , np.complex64 , np.matrix
# """

# arr = np.array([1, 2, 3])
# print(arr.dtype) # int32
# arr = np.array(['apple', 'banana', 'cherry'])
# print(arr.dtype) # <U6

# # Cr´eation d’un tableau 3x3 int32 de z´eros
# arr2 = np.zeros((3, 3), dtype=np.int32)
# # Cr´eation d’un tableau 2x2 complex128 rempli 1
# arr3 = np.ones((2, 2), dtype=np.complex128)

# arr = np.array([ 1 , '2' , 3 , '4'])
# print(arr.dtype) # <U11

# a = np.array([1, 1, 0, 0], dtype=bool)
# b = np.array([1, 0, 1, 0], dtype=bool)
# c = np.logical_or(a, b)
# print(c) #[ True True True False]
# print(np.logical_and(a,b)) #[ True False False False]

# arr01 = np.array([ [ [1 , 2] , [3 , 4] ] , [ [5 , 6] , [7 , 8] ] ]) 
# print(arr01.shape) # (2 , 2 , 2)
# print(arr01.reshape(4 , -1)) # [[1 2] [3 4] [5 6] [7 8]]
# print(arr01.flatten()) # [1 2 3 4 5 6 7 8]

# arr1 = np.array(([ 1 , 2 , 3 , 4 ] , [ 5 , 6 , 7 , 8 ]))
# arr2 = np.array(([ 9 , 10 , 11 , 12 ] , [ 13 , 14 , 15 , 16 ]))

# print(f"Arr01 : \n{arr1}") # [[1 2 3 4] [5 6 7 8]]
# print(f"Arr02 : \n{arr2}") # [[ 9 10 11 12] [13 14 15 16]]

# print(f"Axis 0 : \n{np.concatenate((arr1 , arr2) , axis=0)}") # [[ 1  2  3  4] [ 5  6  7  8] [ 9 10 11 12] [13 14 15 16]]
# print(f"Axis 1 : \n{np.concatenate((arr1 , arr2) , axis=1)}") # [[ 1  2  3  4  9 10 11 12] [ 5  6  7  8 13 14 15 16]]

# print(f"VStack : \n{np.vstack((arr1 , arr1))}") # [[1 2 3 4] [5 6 7 8] [1 2 3 4] [5 6 7 8]]
# print(f"HStack : \n{np.hstack((arr1 , arr2))}") # [[ 1  2  3  4  9 10 11 12] [ 5  6  7  8 13 14 15 16]]
# print(f"DStack : \n{np.dstack((arr1 , arr2))}") # [[[ 1  9] [ 2 10] [ 3 11] [ 4 12[[ 5 13] [ 6 14] [ 7 15] [ 8 16]]]

# ################################## Split

# print(f"Split 2 : {np.array_split(arr1 , 2)}") # [array([[1, 2, 3, 4]]), array([[5, 6, 7, 8]])]

# ################################## hsplit , dsplit , vsplit
# print(f"hsplit 2 : {np.hsplit(arr1 , 2)}") # [array([[1, 2], [5, 6]]), array([[3, 4], [7, 8]])]
# print(f"vsplit 2 : {np.vsplit(arr1 , 2)}") # [array([[1, 2, 3, 4]]), array([[5, 6, 7, 8]])]


################################## Where
arr = np.array([1, 2, 3, 4, 5, 7])
print(f"{np.searchsorted(arr , 6)}")