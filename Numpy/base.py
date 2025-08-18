import numpy as np


# 1. Rule by brackets


# 1D array → ek hi level ke elements hote hain
arr = np.array([1, 2, 3])
# Sirf ek level []
# Shape: (3,)
# ndim: 1


# 2D array → array ke andar arrays hote hain
arr = np.array([[1, 2, 3], [4, 5, 6]])
# Bahar [] ke andar har element bhi ek []
# Shape: (2, 3)
# ndim: 2



# 3D array → array ke andar arrays of arrays hote hain
arr = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
])
# Bahar [] → andar [] → aur unke andar bhi []
# Shape: (2, 2, 3)
# ndim: 3



# 1D → list of numbers
# 2D → list of lists
# 3D → list of list of lists
