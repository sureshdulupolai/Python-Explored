# lambda arguments: expression

hello = lambda : "Hello World!"
print(hello())     # Hello World!

add = lambda x, y: x + y
print(add(5, 3))   # Output: 8

data = [(1, 'b'), (3, 'a'), (2, 'c')]
data.sort(key=lambda x: x[1])
print(data)  
# Output: [(3, 'a'), (1, 'b'), (2, 'c')]

nums = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, nums))
print(squares)  
# Output: [1, 4, 9, 16]

nums = [10, 15, 20, 25, 30]
even = list(filter(lambda x: x % 2 == 0, nums))
print(even)  
# Output: [10, 20, 30]

from functools import reduce

nums = [1, 2, 3, 4]
total = reduce(lambda a, b: a + b, nums)
print(total)  
# Output: 10


# -----------------------------------------------------------------------------------------------------------------

