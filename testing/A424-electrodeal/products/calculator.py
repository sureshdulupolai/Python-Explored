import math


class Calculator:
   
    def add(self, a, b):
        return a+b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return a / b

    def power(self, base, exponent):
        return base ** exponent

    def square_root(self, number):
        if number < 0:
            raise ValueError("Cannot calculate square root of a negative number.")
        return math.sqrt(number)


    def modulus(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Modulus by zero is not allowed.")
        return a % b


    def floor_division(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Floor division by zero is not allowed.")
        return a // b


    def absolute(self, number):
        return abs(number)


    def factorial(self, number):
        if not isinstance(number, int):
            raise TypeError("Factorial is only defined for integers.")
        if number < 0:
            raise ValueError("Factorial of a negative number is not allowed.")
        return math.factorial(number)


    def is_even(self, number):
     if not isinstance(number, int):
         raise TypeError("is_even only works with integers.")
     return number % 2 == 0


    def is_odd(self, number):
       if not isinstance(number, int):
           raise TypeError("is_odd only works with integers.")
       return number % 2 != 0


    def is_prime(self, number):
        if not isinstance(number, int):
            raise TypeError("is_prime only works with integers.")
        if number <= 1:
            return False
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return False
        return True



