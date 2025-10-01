"""

What is Threading?
Thread = ek lightweight unit of execution.
Python mai ek process ke andar multiple threads chal sakte hain jo same memory space share karte hain.
Useful for: I/O-bound tasks (file read/write, API calls, DB operations, network requests).

"""

#
import time

def task(name):
    for i in range(3):
        print(f"{name} running {i}")
        time.sleep(1)

# Sequential
task("Task 1")
task("Task 2")
# ⏱ Isme pehle Task 1 complete hoga → phir Task 2.


# With Threading
import threading
import time

def task(name):
    for i in range(3):
        print(f"{name} running {i}")
        time.sleep(1)

# Create threads
t1 = threading.Thread(target=task, args=("Task 1",))
t2 = threading.Thread(target=task, args=("Task 2",))

# Start threads
t1.start()
t2.start()

# Wait until finish
t1.join()
t2.join()

print("✅ All tasks done")
#  Ab Task 1 aur Task 2 parallel run honge.


"""
4. Thread Locking (Avoid Race Conditions)
Agar multiple threads ek hi resource (like file, variable, db) access karte hain → data corruption ho sakta hai.
Iske liye Lock use karte hain.
"""

import threading

lock = threading.Lock()
counter = 0

def increment():
    global counter
    for _ in range(100000):
        with lock:   # 🔒 only 1 thread at a time
            counter += 1

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start(); t2.start()
t1.join(); t2.join()

print("Final counter:", counter)
# 👉 Agar lock use na kare to wrong result milega.


"""
5. Daemon Threads
Daemon thread background mai chalta hai (like auto-cleanup, monitoring).
Jab main program khatam hota hai → daemon bhi khatam ho jata hai.
"""

import threading, time

def background():
    while True:
        print("Background running...")
        time.sleep(2)

t = threading.Thread(target=background, daemon=True)
t.start()

time.sleep(5)
print("Main program exit")


"""
6. ThreadPoolExecutor (Easiest way)
Python 3.2+ mai concurrent.futures se thread pool manage karna easy hai.
"""

from concurrent.futures import ThreadPoolExecutor
import time

def task(n):
    print(f"Task {n} started")
    time.sleep(2)
    return f"Task {n} done"

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(task, [1, 2, 3, 4, 5])

print(list(results))


"""
⚡ Important Note: GIL (Global Interpreter Lock)

Python mai ek samay pe sirf ek thread CPU execute karta hai → iska matlab threading CPU-bound tasks ke liye slow ho sakta hai.
Threading best hai I/O-bound tasks ke liye (file, API, DB).
CPU-bound ke liye multiprocessing use karo.


Summary:
threading.Thread → custom threads
Lock → race condition avoid
daemon=True → background threads
ThreadPoolExecutor → easy pooling
For CPU-bound → use multiprocessing.

"""


# Real Life
import time

def download_file(file_name):
    print(f"⬇️ Downloading {file_name}...")
    time.sleep(2)   # simulate delay
    print(f"✅ Finished {file_name}")

files = ["file1.pdf", "file2.jpg", "file3.mp4", "file4.zip"]

start = time.time()
for f in files:
    download_file(f)
end = time.time()

print(f"Total time: {end - start:.2f} sec")

"""
⬇️ Downloading file1.pdf...
✅ Finished file1.pdf
⬇️ Downloading file2.jpg...
✅ Finished file2.jpg
...
Total time: ~8 sec
"""

import threading, time

def download_file(file_name):
    print(f"⬇️ Downloading {file_name}...")
    time.sleep(2)   # simulate delay
    print(f"✅ Finished {file_name}")

files = ["file1.pdf", "file2.jpg", "file3.mp4", "file4.zip"]

threads = []
start = time.time()

for f in files:
    t = threading.Thread(target=download_file, args=(f,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end = time.time()
print(f"Total time: {end - start:.2f} sec")


"""
⬇️ Downloading file1.pdf...
⬇️ Downloading file2.jpg...
⬇️ Downloading file3.mp4...
⬇️ Downloading file4.zip...
✅ Finished file2.jpg
✅ Finished file1.pdf
✅ Finished file3.mp4
✅ Finished file4.zip
Total time: ~2 sec
"""

from concurrent.futures import ThreadPoolExecutor
import time

def download_file(file_name):
    print(f"⬇️ Downloading {file_name}...")
    time.sleep(2)
    return f"✅ Finished {file_name}"

files = ["file1.pdf", "file2.jpg", "file3.mp4", "file4.zip"]

start = time.time()
with ThreadPoolExecutor(max_workers=4) as executor:
    results = executor.map(download_file, files)

for r in results:
    print(r)

end = time.time()
print(f"Total time: {end - start:.2f} sec")
