import numpy as np

# np.empty((row, col), dtype)
# get random data that inserted into dtype, with given row and column
e = np.empty((4,4), dtype=int)
# print(e)

x = np.ones(6)
print(x) # [1. 1. 1. 1. 1. 1.], get 6 element given in ones() as parameter, by default it is float

y = np.ones((3, 5))
print(y)

z = np.ones((3, 5), dtype=int)
print(z)

# this same with zeros()
np.zeros(3) # funtion

# you can do with data type with str, bool
# str you will get '1' but for zeros(), you will get only empty str ''
# in bool ones() you get True
# but in zeros() you get False