import numpy as np


# Data Types in Python

# strings - used to represent text data, the text is given under quote marks. e.g. "ABCD"
# integer - used to represent integer numbers. e.g. -1, -2, -3
# float - used to represent real numbers. e.g. 1.2, 42.42
# boolean - used to represent True or False.
# complex - used to represent complex numbers. e.g. 1.0 + 2.0j, 1.5 + 2.5j


# Data Types in NumPy -> (machine-dependent)

# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )



# Checking the Data Type of an Array
arr = np.array([1, 2, 3, 4])
print(arr.dtype) # int64


arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype) # <U6
# < → little-endian byte order
# U → Unicode string
# 6 → max length 6 characters (longest word "banana" → 6 letters)


# Create an array with data type string
arr = np.array([1, 2, 3, 4], dtype='U')
print(arr)        # ['1' '2' '3' '4']
print(arr.dtype)  # <U1


# Create an array with data type 4 bytes integer
arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype)


# Change data type from float to integer by using 'i' as parameter value
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)
print(len(newarr))
print(newarr.dtype) # dtype ka koi length nahi hota



# Change data type from float to integer by using int as parameter value
newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)


# Change data type from integer to boolean
arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)


print()
for i in newarr:
    print(type(i)) # <class 'numpy.bool'>