import numpy as np

# Iterating Arrays

# 1-D array
arr = np.array([1, 2, 3])

for x in arr:
  print(x)



# 2-D array
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  print(x)


print()
# Iterate on each scalar element of the 2-D array
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  for y in x:
    print(y)



# 3-D array
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
  print(x)


# 
arr = np.array([
  [[1, 2, 3], [4, 5, 6]], 
  [[7, 8, 9], [10, 11, 12]]
])

# x -> [[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]
# y -> [1, 2, 3], [4, 5, 6]
# z -> 1, 2, 3, 4, 5, 6
for x in arr:
  for y in x:
    for z in y:
      print(z)


print()
# Iterating Arrays Using nditer() -> Iterate through the following 3-D array
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
  print(x) # 1, 2, 3, 4, 5, 6, 7, 8



print()
# Iterating Array With Different Data Types -> op_dtypes 
arr = np.array([1, 2, 3])
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)
# b'1' ka matlab hai bytes literal — yeh ek binary representation of '1' hai.
# Jab tum ek datatype se dusre datatype me convert karna chahte ho iteration ke dauran, to NumPy ko temporary buffer banane ki permission chahiye hoti hai.
# "buffered" flag allow karta hai ki wo intermediate buffer banaye taki conversion ho sake.


# example
print()
arr = np.array([10, 20, 30])
my_dict = {}

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    my_dict[str(x, 'utf-8')] = "Value for " + str(x, 'utf-8')

print(my_dict)
# {'10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00': 'Value for 10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', '20\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00': 'Value for 20\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', '30\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00': 'Value for 30\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'}




# Iterating With Different Step Size
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[:, ::2]):
  print(x)


print()
# Enumerated Iteration Using ndenumerate() ->  index + value ko return karta hai, Index tuple form -> 1D, 2D, ya 3D 
# | Row\Col   | Col 0 | Col 1 | Col 2 |
# | --------- | ----- | ----- | ----- |
# | **Row 0** | 1     | 2     | 3     |
# | **Row 1** | 4     | 5     | 6     |

arr = np.array([[1, 2, 3], [4, 5, 6]])
for idx, x in np.ndenumerate(arr):
  print(idx, x)
