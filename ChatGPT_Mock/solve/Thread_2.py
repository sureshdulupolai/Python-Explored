"""
=======================================
   ThreadPoolExecutor Example (Python)
=======================================

👉 ThreadPoolExecutor ek thread pool banata hai.
   - 'max_workers' decide karta hai ek time par kitne threads parallel chalenge.
   - 'submit()' se ek-ek task dal sakte ho.
   - 'map()' se ek saath iterable tasks dal sakte ho.
   - 'initializer' har thread start hone par ek baar run hota hai.

💡 General Rule:
   - CPU Bound tasks (heavy calculation) → max_workers = os.cpu_count()
   - IO Bound tasks (network/file/db calls) → max_workers zyada rakhna safe hai

"""

from concurrent.futures import ThreadPoolExecutor
import time
import threading
import os
import requests


# -----------------------------
#  Example 1: Simple Calculation
# -----------------------------
def square(x):
    """Return square of a number (simulate delay)"""
    print(f"[{threading.current_thread().name}] Starting task for {x}")
    time.sleep(1)
    print(f"[{threading.current_thread().name}] Finished task for {x}")
    return x * x


def demo_calculation():
    print("\n=== Demo: Simple Calculation ===")
    with ThreadPoolExecutor(max_workers=3, thread_name_prefix="calc") as executor:
        numbers = [1, 2, 3, 4, 5, 6]
        results = executor.map(square, numbers)

        for result in results:
            print("Result:", result)


# -----------------------------
#  Example 2: Network Calls (I/O Bound)
# -----------------------------
URLS = [
    "https://www.google.com",
    "https://www.python.org",
    "https://www.github.com",
    "https://www.stackoverflow.com",
]


def fetch(url):
    """Fetch a URL and return status code"""
    print(f"[{threading.current_thread().name}] Fetching: {url}")
    r = requests.get(url)
    return f"{url} -> {r.status_code}"


def demo_network():
    print("\n=== Demo: Network Calls ===")
    with ThreadPoolExecutor(max_workers=5, thread_name_prefix="net") as executor:
        results = executor.map(fetch, URLS)
        for res in results:
            print("Response:", res)


# -----------------------------
#  Example 3: Using initializer
# -----------------------------
def init_thread():
    """Initializer runs when a new thread is created"""
    print(f"[{threading.current_thread().name}] Initialized (PID={os.getpid()})")


def multiply(a, b):
    return f"{a} * {b} = {a*b}"


def demo_initializer():
    print("\n=== Demo: Initializer ===")
    pairs = [(2, 3), (3, 4), (4, 5)]
    with ThreadPoolExecutor(max_workers=2, initializer=init_thread, thread_name_prefix="init") as executor:
        results = executor.map(lambda args: multiply(*args), pairs)
        for res in results:
            print(res)


# -----------------------------
#  MAIN EXECUTION
# -----------------------------
if __name__ == "__main__":
    demo_calculation()
    demo_network()
    demo_initializer()
