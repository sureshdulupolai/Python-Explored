"""
Python Advanced Notes.
"""

# -------------------------------
# 1️⃣ Object-Oriented Programming (OOP)
# -------------------------------
# Use-case: Real-life scenario - Car Management System
# Classes represent entities, inheritance represent relationships
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def display(self):
        # Print vehicle info
        print(f"{self.brand} runs at {self.speed} km/h")

# Example 1: Basic Vehicle object
car = Vehicle("Toyota", 120)
car.display()  # Use-case: print car details in fleet management system

# Example 2: Inheritance - Car is a Vehicle
class Car(Vehicle):
    def fuel_type(self, fuel):
        # Print fuel type of car
        print(f"{self.brand} uses {fuel} fuel")

my_car = Car("Honda", 150)
my_car.display()        # Prints inherited info
my_car.fuel_type("Petrol")  # Prints specific info for Car

# -------------------------------
# 2️⃣ Decorators & Closures
# -------------------------------
# Use-case: Logging function calls in real projects

# Example 1: Decorator for logging
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Running {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOG] Completed {func.__name__}")
        return result
    return wrapper

@logger
def calculate_salary(base, bonus):
    return base + bonus

print(calculate_salary(50000, 5000))  # Decorator logs before and after function call

# Example 2: Closure for discount calculation
def discount(rate):
    # rate stored in outer function
    def apply_discount(price):
        return price - (price * rate / 100)
    return apply_discount

ten_percent = discount(10)
print(ten_percent(2000))  # Output: 1800, use-case: e-commerce discount system

# -------------------------------
# 3️⃣ Generators & Iterators
# -------------------------------
# Use-case: Processing large data without loading all in memory

# Example 1: Generator - reading huge log file line by line
def log_reader(lines):
    for line in lines:
        yield line.upper()  # Process each line

for log in log_reader(["error 1", "warning 2", "info 3"]):
    print(log)

# Example 2: Custom Iterator - paginate API results
class APIResult:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            val = self.data[self.index]
            self.index += 1
            return val
        else:
            raise StopIteration

results = APIResult([100, 200, 300])
for r in results:
    print(r)  # Use-case: iterate API responses one by one

# -------------------------------
# 4️⃣ Context Managers
# -------------------------------
# Use-case: File handling or DB connections safely

# Example 1: Using 'with' statement to write a file
with open("report.txt", "w") as f:
    f.write("Sales Report 2025")  # Auto close file after write

# Example 2: Custom context manager - DB connection simulation
class ManagedDB:
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        print(f"Connecting to {self.db_name} DB")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing connection to {self.db_name} DB")

with ManagedDB("Oracle") as db:
    print("Performing DB operations")  # Use-case: real DB context handling

# -------------------------------
# 5️⃣ Advanced Data Structures
# -------------------------------
from collections import deque, Counter

# Example 1: deque for task queue
tasks = deque(["Task1", "Task2", "Task3"])
tasks.appendleft("UrgentTask")
print(tasks)  # Use-case: prioritize urgent tasks in queue

# Example 2: Counter for word frequency in document
text = "python django python fastapi"
freq = Counter(text.split())
print(freq)  # Use-case: analyze most common words in text

# -------------------------------
# 6️⃣ Error Handling & Exceptions
# -------------------------------
# Use-case: Handle errors gracefully in production apps

# Example 1: ZeroDivisionError
try:
    val = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero")  # Real-life: avoid crash in calculations

# Example 2: Custom Exception
class InsufficientBalance(Exception):
    pass

try:
    balance = 500
    withdraw = 600
    if withdraw > balance:
        raise InsufficientBalance("Not enough balance")
except InsufficientBalance as e:
    print(e)  # Banking app simulation

# -------------------------------
# 7️⃣ Concurrency & Parallelism
# -------------------------------
import threading

# Example 1: Threading - sending emails concurrently
def send_email(email):
    print(f"Sending email to {email}")

emails = ["a@example.com", "b@example.com"]
threads = []
for e in emails:
    t = threading.Thread(target=send_email, args=(e,))
    threads.append(t)
    t.start()
for t in threads:
    t.join()

# Example 2: Multiprocessing - heavy computation
from multiprocessing import Process

def compute_square(n):
    print(f"Square of {n} is {n*n}")

p1 = Process(target=compute_square, args=(5,))
p1.start()
p1.join()  # Use-case: parallelize heavy calculations

# -------------------------------
# 8️⃣ Testing & Debugging
# -------------------------------
# Example 1: Unit test for a function
import unittest

def multiply(a, b):
    return a * b

class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)  # Use-case: ensure function correctness

# Example 2: Logging important events
import logging
logging.basicConfig(level=logging.INFO)
logging.info("Server started successfully")  # Real-life: monitoring app logs
