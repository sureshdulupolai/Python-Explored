# Hello World Program
print("Hello World")

# Check even or odd
# print("Even" if float(input("Enter Numerical Values: ")) % 2 == 0 else "Odd")

# Sum of two no
# print(f"Sum of Two No: {float(input("Enter Value 1: ")) + float(input("Enter Value 2: "))}")

# Largest of Two No
# a = float(input("Enter Value 1: ")); b = float(input("Enter Value 2: "))
# print(f"Largest of Two No: {'A is Greater' if a > b else ('Equal' if a == b else 'B is Greater')}")

# Positive, Negative or Zero Check
# data = float(input("Enter Value To Check P, N, or Z: "))
# print(f"{data} is {"Positive" if data > 0 else ("Zero" if data == 0 else "Negative")} Value")

# Leap Year Check 
# year = int(input("Enter a year: "))
# print("Leap Year" if (year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)) else "Not a Leap Year")

# Swap two number (with and without third variable)
# 1.
# a = int(input("enter numerical value 1: "))
# b = int(input("enter numerical value 2: "))
# a, b = b, a
# print(f"Swap A = {a}, B = {b}")

# c = b
# b = a
# a = c
# print(f"R-Swap A = {a}, B = {b}")

# Factorial of a Number (iterative)
# num = int(input("Enter a number: "))

# fact = 1
# for i in range(1, num + 1):
#     fact *= i   # same as fact = fact * i

# print(f"Factorial of {num} is {fact}")

# Fibonacci series (first N)
# n = int(input("Enter number of terms: "))

# a, b = 0, 1   # first two terms
# print("Fibonacci Series:", end=" ")

# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b

# Reverse a number
# data = input("enter numerical no to reverse: ")
# print(f"Reversed : {data[::-1]}" if data.isalnum() else "Enter Only Positive Value")

# Palindrome number check
# data = input("enter value to check palindrome: ").lower()
# print(f"{data} is : {"Palindorm"  if data == data[::-1] else "Not Palindorm"}")

# Armstrong number check
# data = input("enter only numerical to check armstrong no: ")
# ln = len(data); print(f"{"Number is Armstrong" if data == str(sum(int(i) ** ln for i in data)) else "Not a Armstrong No"}") if data.isalnum() else "Enter Only Numerical Value"
    
# prime number check
# num = int(input("Enter a number: "))
# print(f"{num} is {'NOT a prime number' if num <= 1 or not all(num % i != 0 for i in range(2, int(num**0.5)+1)) else 'a PRIME number'}")

# print all even number between 1 to N
# data = input("Enter Numerical Value: ")
# print(f"Even numbers: \n{' \n'.join(str(i) for i in range(1, int(data)) if i % 2 == 0)}" if data.isdigit() else "Enter Only Numerical Value")
# print(f"Even numbers: {', '.join(str(i) for i in range(1, int(data)) if i % 2 == 0)}" if data.isdigit() else "Enter Only Numerical Value")

# print number 1 to 100 without loop (using recursion)
# print("\n".join(map(str, range(1, stop+1))))
# def print_numbers(count, stop):
#     if count > stop:
#         return 
#     print(f"{count}")
#     print_numbers(count + 1, stop)
# print_numbers(1, 100)

# sum of digit of a number
# data = "123"
# print(f"The Sum of digit is : {sum([int(i) for i in data])}")

# Find largest and smallest element in an array
# data = [45, 10, 67, 26, 60]
# print(f"Largest Element: {max(data)}\nSmallest Element: {min(data)}")

# Reverse an array
# data = [45, 10, 67, 26, 60]
# print(f"Reversed Array : {list(reversed(data))}")

# find dupliacte elements in an array
# data = [1, 2, 3, 2, 1, 4, 5]
# print(f"Duplicate Data in Side Array Element is : {", ".join(str(i) for i in set([x for x in data if data.count(x) > 1]))}")

