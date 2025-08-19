import numpy as np


# Joining NumPy Arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)



print()
# Join two 2-D arrays along rows (axis=1)
# axis=0 → Column-wise operation
# axis=1 → Row-wise operation 
# default axis = 0 always
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)



# 
arr = np.array([
    [1, 2, 3],[4, 5, 6]
])

# Sum column-wise (axis=0)
print(arr.sum(axis=0))  # [5 7 9]

# Sum row-wise (axis=1)
print(arr.sum(axis=1))  # [6 15]




# Joining Arrays Using Stack Functions
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)
print(arr)


# https://www.w3schools.com/python/numpy/numpy_array_join.asp


# she's so good, you never get bored waiting for her.
# spotify peremium ? woh kya hota hai, me roh uski voice sunta hu
# tu kar bhai multiple ladkiyon se baat, me to madam ji ka wait kr lunga