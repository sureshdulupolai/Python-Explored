from collections import Counter

# score = [10, 20, 50, 60, 80, 78, 80, 90]
score = [50, 70, 70, 90, 45, 76, 99, 88]
# score = [10, 20, 30, 40]  # test case with no duplicates

scoreLen = len(score)

# --- Mean ---
mean = sum(score) / scoreLen
print("Mean:", mean)

# --- Median ---
score_sorted = sorted(score)   # median ke liye sorting zaroori hai
find_no = scoreLen // 2

if scoreLen % 2 == 0:
    median = (score_sorted[find_no - 1] + score_sorted[find_no]) / 2
else:
    median = score_sorted[find_no]
print("Median:", median)

# --- Mode (duplicates only, safe) ---
mode = Counter(score)
duplicates = [item for item, count in mode.items() if count > 1]

if duplicates:   # agar koi duplicate hai toh
    print("Repeated items:", duplicates[0])
else:            # agar nahi hai toh None
    print("Repeated items:", None)
