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
# arr = np.array([1, 2, 3, 4, 5, 7])
# print(f"{np.searchsorted(arr , 6)}")

############# union1d & intersect1d
# arr01 = np.array([1 , 2 , 3 , 4])
# arr02 = np.array([1 , 5 , 3 , 6])
# print(f"Union : {np.union1d(arr01 , arr02)}") # [1 2 3 4 5 6]
# print(f"Intersect : {np.intersect1d(arr01 , arr02)}") # [1 3]
# arr03 = np.concatenate((arr01 , arr02))
# uniqueElement , indices = np.unique(arr03 , return_index=True) # return_inverse , return_count
# print(f"Unique Elemenet on Arr03 : {uniqueElement}") # [1 2 3 4 5 6]
# print(f"Index odfunique element on arr03 : {indices}") # [0 1 2 3 5 7]

# tab = np.array([[1, 2, 3],
#     [4, 2, 6],
#     [7, 8, 9],
#     [1, 2, 3]])

# print(f"Unique elements Axis0 : {np.unique(tab , axis=0)}")
# print(f"Unique elements Axis1 : {np.unique(tab , axis=0)}")

########################### Random
demo01 = np.random.randint(10 , 101 , size=(3))
demo02 = np.random.rand(3)
demo03 = np.random.choice([1 , 3 , 6 , 8 , 19] , size=3)
demo04 = np.random.shuffle([1 , 3 , 6 , 8 , 19] , size=3) # melange