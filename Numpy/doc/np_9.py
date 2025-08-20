# Joining NumPy Arrays

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# 1D Array
arr = np.concatenate((arr1, arr2))
print(arr)


# 2D Array -> rows (axis=1)
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)
print(arr)
# [[1 2 5 6]
#  [3 4 7 8]]


arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# If axis is not explicitly passed it is taken as 0.
arr = np.stack((arr1, arr2), axis=1)
print(arr)
# [[1 4]
#  [2 5]
#  [3 6]]


# hstack() to stack along rows
arr = np.hstack((arr1, arr2))
print(arr) 
# [1 2 3 4 5 6]


# vstack()  to stack along columns.
arr = np.vstack((arr1, arr2))
print(arr)
# [[1 2 3]
#  [4 5 6]]



# Stacking Along Height (depth)
# dstack() to stack along height, which is the same as depth.
arr = np.dstack((arr1, arr2))
print(arr)
# [[[1 4]
#   [2 5]
#   [3 6]]]

