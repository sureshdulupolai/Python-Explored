# pip install numpy

# Basic 
# [[1,2,3,4,5], [6,7,8,9,10]]
# there are one list inside 2 list, mean 2-d array
# [1,2,3,4,5] -> row one
# [6,7,8,9,10] -> row two
# inside each row there are 5 column len([6,7,8,9,10])


# -------------------------------------------------------------

import numpy as np

# Create a NumPy ndarray Object
arr = np.array([1, 2, 3, 4, 5])

print(type(arr)) # <class 'numpy.ndarray'>
print(arr) # [1, 2, 3, 4, 5]
print(np.__version__) # 2.3.1


# Use a tuple to create a NumPy array
arr_1 = np.array((1, 2, 3, 4, 5))
print(arr_1) # [1, 2, 3, 4, 5]


# 0-D Arrays
arr = np.array(42)
print(arr)


# 1-D Arrays
arr = np.array([1, 2, 3, 4, 5])
print(arr)


# 2-D Arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)


# Create a 3-D array with two 2-D arrays
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)



# Check how many dimensions the arrays have
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


# Higher Dimensional Arrays -> you can define the number of dimensions by using the ndmin argument
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)

