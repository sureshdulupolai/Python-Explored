import numpy as np

# it can store one dime data type string int etc
lst = [1, 2, 3, 4, 5]
print(lst)

print('1D Aaray')
a = np.array([1, 2, 3, 4, 5])
print(a)

print('2D Aaray')
b = np.array([
    [1, 2, 3, 4, 5], [6, 7, 8, 9, 10]
])
print(b)


print('3D Aaray')
c = np.array([
    [
        [1, 2, 3, 4, 5], [6, 7, 8, 9, 10]
    ]
])
print(c)


# size of np -> no of elements in array
print()
print(a.size)
print(b.size)
print(c.size)


# to check shapes
print()
print(a.shape) # (5,) -> 5 column
print(b.shape) # (2, 5) -> 2 row, 5column
print(c.shape) # (1, 3, 5) -> 1 array, 3 rows, 5 column


# to check datatype in np -> dtype
print()
print(a.dtype)
print(b.dtype)
print(c.dtype)


d = np.array([
    [1, 2, 3, 4.2, 5],
    [6, 7, 8.9, 9, 10],
    [11, 12, 13, 14, 15]
])

print(d.dtype) # float62
print(d.transpose()) # Rows ↔ Columns

# Original d:
#  [[1 2 3]
#   [4 5 6]]

# Transposed d:
#  [[1 4]
#   [2 5]
#   [3 6]]
