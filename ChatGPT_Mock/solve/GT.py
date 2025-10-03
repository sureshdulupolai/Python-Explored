"""
1️⃣ GIL & Threading in Python

GIL = Global Interpreter Lock
CPython me ek time me sirf ek thread Python bytecode execute kar sakta hai.
Threading CPU-bound tasks ke liye slow ho sakta hai, lekin I/O-bound tasks me efficient hai.
"""

# 🔹 Example 1: CPU-bound task with threading
import threading
import time

def cpu_task(n):
    count = 0
    for i in range(n):
        count += i*i
    print("Done counting")

# Large N
N = 10**7

start = time.time()

t1 = threading.Thread(target=cpu_task, args=(N,))
t2 = threading.Thread(target=cpu_task, args=(N,))

t1.start()
t2.start()
t1.join()
t2.join()

end = time.time()
print("Time taken with threading:", end - start)


# 🔹 Example 2: I/O-bound task (network / sleep)
import threading
import time

def io_task():
    time.sleep(2)
    print("Done sleeping")

threads = []
for _ in range(5):
    t = threading.Thread(target=io_task)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("All threads done")


# 2️⃣ Garbage Collection (GC) & Reference Counting

# Python me memory automatically manage hoti hai.
# Reference counting: Python objects track karte hai kitne references point kar rahe hain.
# Garbage Collector (GC): Cyclic references ko clean karta hai jo reference counting se handle nahi hote.

# 🔹 Example 1: Reference Counting
import sys

a = [1, 2, 3]
b = a

print(sys.getrefcount(a))  # number of references (1 extra for getrefcount)
del b
print(sys.getrefcount(a))  # references reduced

# sys.getrefcount(obj) → kitne references object ke liye exist karte hain.

# Extra +1 hota hai because argument pass ho raha hai.
# 🔹 Example 2: Garbage Collector

import gc

# Disable automatic GC (just for demo)
gc.disable()

# Create cyclic reference
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

a = Node(1)
b = Node(2)
a.next = b
b.next = a  # cyclic reference

del a
del b

print("Before GC:", gc.collect())  # manually collect cyclic objects
print("After GC enabled:", gc.collect())

gc.enable()