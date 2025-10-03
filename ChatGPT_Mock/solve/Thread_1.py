import threading
import time

def func(seconds, ind):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    print(f"Task Done for {ind}")
    return seconds

def main():
    time1 = time.perf_counter()
    func(4, 1)
    func(2, 2)
    func(1, 3)
    time2 = time.perf_counter()
    print(f"Time Taken : {time2 - time1}") # Time Taken : 7.00441980001051

    print()
    time1 = time.perf_counter()
    t1 = threading.Thread(target=func, args=[4, 1])
    t2 = threading.Thread(target=func, args=[2, 2])

    # Start Means => Work is starting in background it work in background and move to next line
    # dont wait to finish the program it start in backgorund and move for next program
    t1.start()
    t2.start()

    # if you want to wait to finish the program then use .join()
    # after finishing the parallel program then it show
    t1.join()
    t2.join()


    time2 = time.perf_counter()
    print(f"Time Taken : {time2 - time1}") # Time Taken : 4.0050077000050806 => 4 for highest running
    """
    sleep main sabse jada => 4 diya hai matlab 4 second rukna hai parallel chalega aur sabse jada time 4 lega
    4 second mai dono execute kar dega

    4 + 2 = 6 Second Take in Normal Function Call
    4 & 2 = 4 Second Take in Thread Function Call
    """

from concurrent.futures import ThreadPoolExecutor

def poolingDemo():
    with ThreadPoolExecutor() as executor:
        # other program
        # future = executor.submit(pow, 323, 1234)
        # print(future.result())

        # own program 
        future1 = executor.submit(func, 4, 1)
        future2 = executor.submit(func, 2, 2)
        future3 = executor.submit(func, 1, 3)

        future1.result() 
        future2.result()
        future3.result() # if your write inside print then it return None


        # Multiple args with map → alag alag lists pass karo
        a_list = [3, 4]
        ind_list = [1, 2]

        result = executor.map(func, a_list, ind_list)
        for i in result:
            print(i)

# poolingDemo()

# Demo For Thread_2.py file
from concurrent.futures import ThreadPoolExecutor
import time
import threading

def task(n):
    """Har task sirf apna number print karega aur 2 sec wait karega"""
    print(f"[{threading.current_thread().name}] --> Task {n} START")
    time.sleep(2)
    print(f"[{threading.current_thread().name}] --> Task {n} END")
    return n

def main():
    with ThreadPoolExecutor(max_workers=3) as executor:  # ek time pe 3 hi worker
        results = executor.map(task, range(1, 11))  # 10 task diye

        # results me task ke return values sequentially milti hain
        for r in results:
            print("Result returned:", r)

if __name__ == "__main__":
    main()

"""
[ThreadPoolExecutor-0_0] --> Task 1 START
[ThreadPoolExecutor-0_1] --> Task 2 START
[ThreadPoolExecutor-0_2] --> Task 3 START
... (2 sec delay)
[ThreadPoolExecutor-0_0] --> Task 1 END
[ThreadPoolExecutor-0_0] --> Task 4 START
[ThreadPoolExecutor-0_1] --> Task 2 END
[ThreadPoolExecutor-0_1] --> Task 5 START
[ThreadPoolExecutor-0_2] --> Task 3 END
[ThreadPoolExecutor-0_2] --> Task 6 START
... aur aise chalta rahega ...

"""