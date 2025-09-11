# import time


# def blink(seconds, repeats=5):
#     """Blink for given seconds delay, repeats times"""
#     for _ in range(repeats):
#         print("Blinking!!")
#         time.sleep(seconds)

# print("--Checking Even Or Odd No--")
# while True:
#     data = float(input("Enter a numerical value: "))
#     if data % 2 == 0:
#         blink(1, repeats=5)

import time
import threading

# Global flag to control blinking
stop_blinking = False

def blink(seconds):
    global stop_blinking
    while not stop_blinking:
        print("Blinking!!")
        time.sleep(seconds)

print("--Checking Even Or Odd No--")

while True:
    try:
        data = input("Enter a numerical value (or 'exit' to quit): ").strip().lower()

        # Exit conditions
        if data in ["exit", "quit", "e", "q"]:
            print("👋 Exiting program...")
            break

        # Only allow numeric input
        if data.isdigit():
            num = int(data)

            if num % 2 == 0:  # Only for even numbers
                stop_blinking = False
                t = threading.Thread(target=blink, args=(1,))  # 1 sec delay
                t.start()

                input("👉 Press Enter to stop blinking...\n")
                stop_blinking = True
                t.join()
        else:
            print("❌ Please enter a valid number or type 'exit' to quit")

    except ValueError:
        print("❌ Invalid input, try again")
