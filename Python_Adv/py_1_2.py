"""

list Comprehensions
Dictionary Comprehensions
Set Comprehensions
Generator Comprehensions

"""

# 1
# [expression for item in iterable if condition]

nums = [1, 2, 3, 4, 5]
squares = [n**2 for n in nums]
print(squares)  # 👉 [1, 4, 9, 16, 25]

nums = [1, 2, 3, 4, 5, 6]
evens = [n for n in nums if n % 2 == 0]
print(evens)  # 👉 [2, 4, 6]

word = "python"
chars = [ch for ch in word]
print(chars)  # 👉 ['p', 'y', 't', 'h', 'o', 'n']

nums = [1, 2, 3, 4, 5]
result = ["Even" if n % 2 == 0 else "Odd" for n in nums]
print(result)  # 👉 ['Odd', 'Even', 'Odd', 'Even', 'Odd']

pairs = [(x, y) for x in [1, 2] for y in [10, 20]]
print(pairs)  
# 👉 [(1, 10), (1, 20), (2, 10), (2, 20)]

matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
print(flat)  # 👉 [1, 2, 3, 4, 5, 6]

a1, a2 = [list(x) for x in zip(*[(n, n**2) for n in range(5)])]
print("A1: ",a1)  # 👉 [0, 1, 2, 3, 4]
print("A2: ",a2)  # 👉 [0, 1, 4, 9, 16] 
# [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)] -> [(n, n**2) for n in range(5)]
# (0, 1, 2, 3, 4), (0, 1, 4, 9, 16) -> zip(*...) -> next convert tuple to list =



# Dictionary & Set Comprehensions
nums = [1, 2, 3, 4]
square_dict = {n: n**2 for n in nums}
print(square_dict)  # 👉 {1: 1, 2: 4, 3: 9, 4: 16}

nums = [1, 2, 2, 3, 3, 4]
unique_squares = {n**2 for n in nums}
print(unique_squares)  # 👉 {16, 1, 4, 9}



# 
nums = range(20)
filtered = [n for n in nums if n % 2 == 0 if n % 5 == 0]
print(filtered)  # 👉 [0, 10]
"""
result = []
for n in nums:
    if n % 2 == 0:
        if n % 5 == 0:
            result.append(n)
"""


def square(x): return x*x
nums = [1, 2, 3, 4]
result = [square(n) for n in nums]
print(result)  # 👉 [1, 4, 9, 16]

names = ["Ram", "Shyam", "Mohan"]
scores = [85, 92, 78]
students = [f"{n} scored {s}" for n, s in zip(names, scores)]
print(students)
# 👉 ['Ram scored 85', 'Shyam scored 92', 'Mohan scored 78']


# 4
# isme mai value ek sath nhi banta hai, jaise list mai ek sath value bana ke usko store karta hai
# isme waise nhi hai jitne bar next() use karoge utna value generate karte jayega
nums = range(10)
gen = (n**2 for n in nums)  # notice () instead of []
print("Gen: ", gen) # Object: <generator object <genexpr> at 0x00000197FB7EA5A0>
print(next(gen))  # 👉 0
print(next(gen))  # 👉 1