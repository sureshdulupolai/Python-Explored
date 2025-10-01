# Har iterable (list, tuple, string, etc.) ko iter() se iterator bana sakte ho.

# Normal iterator
numbers = [10, 20, 30, 40]

it = iter(numbers)   # iterator ban gaya

print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30
print(next(it))  # 40
# print(next(it))  # StopIteration error dega (khatam ho gaya)


# yield use karke function ko iterator jaisa bana dete hain.
def my_range(start, end):
    while start <= end:
        yield start   # ye ek ek value return karega
        start += 1

# Use
for n in my_range(1, 5):
    print(n)


# Advanced Example – Fibonacci Generator
def fibonacci(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

for num in fibonacci(50):
    print(num)
