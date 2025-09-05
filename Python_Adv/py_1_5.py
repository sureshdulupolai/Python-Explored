"""

What is a Decorator?
👉 A decorator ek function hota hai jo dusre function ko modify ya enhance karta hai bina uske actual code ko change kiye.
Basically, functions ko input leke ek new function return karta hai.
Ye closures pe based hota hai.

Decorator = function jo dusre function ko enhance karta hai
Based on closures
@decorator_name syntax use hota hai
Useful in logging, authentication, caching, timing, frameworks (Flask/Django)

"""

def greet():
    return "Hello!"
print(greet())  # 👉 Hello!


def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def speak(func):
    return func("Python is awesome")

print(speak(shout))   # 👉 PYTHON IS AWESOME
print(speak(whisper)) # 👉 python is awesome


# Simple Decorator (manual way)
def decorator(func):
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")
    return wrapper

def say_hello():
    print("Hello!")

decorated = decorator(say_hello)
decorated()


# Python Shortcut: @ Syntax
def decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@decorator
def say_hi():
    print("Hi!")

say_hi()


# Decorator with Arguments
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Function start")
        result = func(*args, **kwargs)
        print("Function end")
        return result
    return wrapper

@decorator
def add(a, b):
    return a + b

print(add(3, 4))  


# Multiple Decorators
def bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper

def italic(func):
    def wrapper():
        return "<i>" + func() + "</i>"
    return wrapper

@bold
@italic
def text():
    return "Python"

print(text())  # 👉 <b><i>Python</i></b>


# Real-Life Use Cases

# 1. Logging
def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log
def multiply(x, y):
    return x * y

multiply(3, 4)  
# 👉 Calling multiply with (3, 4) {}
# 👉 12


# 2. Authentication (e.g. Flask/Django)
def require_login(func):
    def wrapper(*args, **kwargs):
        user_logged_in = True  # Example
        if not user_logged_in:
            return "Access Denied!"
        return func(*args, **kwargs)
    return wrapper

@require_login
def view_profile():
    return "User Profile"

print(view_profile())  # 👉 User Profile

# 3. Timing a function
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.5f} sec")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    return "Done"

print(slow_function())

