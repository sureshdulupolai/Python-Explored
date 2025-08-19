import numpy as np

a = np.random.random(1) # one is pass for how many element present in array len(a) = 1
print(a)

b = np.random.random(2)
print(b)

# 2D array
c = np.random.random((2, 2))
print(c)

d = np.random.randint(1, 10) # between 1 to 10
print(d)

e = np.random.randint(1, 10, (2, 2)) # 2D array betweeen 1 to 10
print(e)

f = np.random.randint(1, 10, (3, 4, 5)) # 3D array, 4 row and 5 column
print(f)

g = np.random.rand(2, 2) # float value, 2D array
print(g)

h = np.random.randn(2, 2) # negative + positive value in 2D array
print(h)

#
print()
i = np.arange(1, 10)
j = np.random.choice(i)
print(j)