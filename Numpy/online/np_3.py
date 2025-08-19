import numpy as np

# np.arange(start, end, step)
a = np.arange(1, 20)
print(a)

b = np.arange(1, 20, 2)
print(b)


# np.reshape((row, col))
c = np.arange(12)
d = c.reshape((3, 4))
print(d)


# with big array
e = np.arange(1, 100, 2)
f = e.reshape((10, 5))
print(f)


#
g = f.flatten()
print(g) # convert into 1D -> one row and multiple column

# 
h = c.ravel()
print(h)


"""
Ravel() -> update in real, like shallow copy
Flatten() -> copy, dont change in orginal, but take memory space
"""

# Ek 2D array bana rahe hain  
arr = np.array([[1, 2, 3], [4, 5, 6]])  

# ---------- RAVEL ----------
# ravel() mostly copy nahi banata, balki original array ka "view" return karta hai
# Matlab agar tum ravel() se banaye gaye array ko modify karoge,
# toh original array bhi change ho sakta hai (agar possible hua toh).
r = arr.ravel()  
print("Ravel output:", r)  

r[0] = 100  # Ravel ke array ka first element change kar diya
print("Modified Ravel:", r)  
print("Original after Ravel modify:", arr)  # Original bhi change ho gaya  

# ---------- FLATTEN ----------
# flatten() hamesha ek "copy" return karta hai
# Matlab agar tum flatten() ka array modify karoge,
# toh original array bilkul bhi effect nahi hoga.
f = arr.flatten()  
print("Flatten output:", f)  

f[0] = 200  # Flatten ke array ka first element change kar diya
print("Modified Flatten:", f)  
print("Original after Flatten modify:", arr)  # Original unchanged raha  

