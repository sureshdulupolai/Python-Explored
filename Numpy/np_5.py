import numpy as np

# NumPy Array Copy vs View
# The Difference Between Copy and View
# Copy:

# Make a copy, change the original array, and display both arrays
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x) # The copy SHOULD NOT be affected by the changes made to the original array.


# Make a view, change the original array, and display both arrays
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x) # The view SHOULD be affected by the changes made to the original array.


x[0] = 31 # The original array SHOULD be affected by the changes made to the view.
print(arr)
print(x)



# copies owns the data, and views does not own the data, but how can we check this
# Every NumPy array has the attribute base that returns None if the array owns the data.
# Otherwise, the base  attribute refers to the original object.

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()

print(x.base) # The copy returns None.
print(y.base) # The view returns the original array.



# Shape of an Array
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)


# 
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('shape of array :', arr.shape)

# [[[[[1 2 3 4]]]]]
# shape of array : (1, 1, 1, 1, 4)

# [1, 2, 3, 4] asli mein ek 1D array hai, shape (4,).
# Lekin ndmin=5 ke wajah se numpy 4 extra axes add karta hai, har ek ka size 1 = 0 index.
# Resulting array ki shape: (1, 1, 1, 1, 4).
# Matlab array ab 5-dimensional hai:
# First dimension ka size = 1
# Second dimension ka size = 1
# Third dimension ka size = 1
# Fourth dimension ka size = 1
# Fifth dimension ka size = 4 (original data length)


# arr[0,0,0,0,:]
