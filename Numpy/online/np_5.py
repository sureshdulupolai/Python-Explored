import numpy as np

a = np.arange(0, 18).reshape((6, 3))
b = np.arange(20, 38).reshape((6, 3))
print(a)
print(b)


print(a + b) # new[0] = a[0] + b[0], new[1] = a[1] + b[1]
print(a - b)
print(a * b)
print(a / b)
print(a ** b)
print(a // b)
print(a % b)

print()
c = np.add(a, b)
d = np.subtract(a, b)
e = np.multiply(a, b)
f = np.divide(a, b)


print(a.shape)
print(b.shape)

b = b.reshape((3, 6))
print(b.shape)
print()
print(a)
print(b)
print(a@b)
g = a.dot(b)


h = b.max()
print(h) # max element present inside that array

b.min() # minimum element present inside that array
b.argmax() # index positon of maximun no of element in that array
b.argmin() # index of min

i = np.sum(b)
print(i) # sum of that array

j = np.sum(b, axis=1) # each and every row sum 
print(j) # [135 171 207]

k = np.sum(b, axis=0) # each and every column
print(k) # [78 81 84 87 90 93]

l = np.mean(b)
print(l) # 28.5

m = np.sqrt(b)
print(m)

n = np.std(b)
print(n)  # standard derivation

o = np.log(b)
print(o)

