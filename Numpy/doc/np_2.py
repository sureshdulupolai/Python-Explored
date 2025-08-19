import numpy as np

# Access Array Elements
arr = np.array([1, 2, 3, 4])
print(arr[0])
print(arr[2] + arr[3])


# Access 2-D Arrays -> Access the element on the first row, second column

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', arr[0, 1])
print('5th element on 2nd row: ', arr[1, 4])


# Access the third element of the second array of the first array

# | Col1 | Col2 | Col3 |
# | ---- | ---- | ---- |
# | 1    | 2    | 3    |
# | 4    | 5    | 6    |

# | Col1 | Col2 | Col3 |
# | ---- | ---- | ---- |
# | 7    | 8    | 9    |
# | 10   | 11   | 12   |

arr = np.array([
    [[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]
])

print(arr[0, 1, 2])



# Print the last element from the 2nd dim
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[1, -1])


# example
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr[1, 1, 0])
