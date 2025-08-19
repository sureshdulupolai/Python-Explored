import numpy as np

a = np.arange(1, 51)
a = a.reshape(10, 5)
print(a)

print(a[0])
print(a[2])
print(a[0, 3])
print(a[0, 1:3])
print(a[2:5])
print(a[:, 2]) # all rows 2 column data in one list
print(a[2:5, 4]) # certain row particular column
print(a[:, :]) # all row and all the column
print(a[:, 2:5])
print(a[:, 2:5].dtype) # Check datatype of particular column