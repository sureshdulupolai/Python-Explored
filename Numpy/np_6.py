import numpy as np

# Reshaping arrays

# Reshape From 1-D to 2-D
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)


# Reshape From 1-D to 3-D
# [[[ 1  2]
#   [ 3  4]
#   [ 5  6]]

#  [[ 7  8]
#   [ 9 10]
#   [11 12]]]
newarr = arr.reshape(2, 3, 2)
print(newarr)


# 
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr.reshape(2, 4).base) # The example above returns the original array, so it is a view.


print()
# Unknown Dimension
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print(newarr)



# Reshape = 2×3×2=12 -> (2, 3, 2) Defining all thing
# Reshape = formula -> ( -1 ) this mean automatically calculate


# Flattening the arrays -> converting a multidimensional array into a 1D array
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)


# ----------------------------------------------------------------------------------------------------------------------------
# Note: There are a lot of functions for changing the shapes of arrays in numpy flatten, ravel and also for rearranging the elements rot90, flip, fliplr, flipud etc. These fall under Intermediate to Advanced section of numpy.