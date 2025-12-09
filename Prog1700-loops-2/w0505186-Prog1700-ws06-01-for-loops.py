# Step 1
print("Count by twos:")
for i in range(2, 12, 2):
    print(i)

print()

print("Squares 1 to 5:")
for i in range(1, 6):
    print(i, "squared is", i * i)

print()

print("Count down from 10:")
for i in range(10, 0, -1):
    print(i)

print("Done!")

#step 2
print("Triangle pattern:")
for i in range(1, 6):
    print("*" * i)

print() 

print("Reverse triangle pattern:")
for i in range(5, 0, -1):
    print("*" * i)

print() 

print("Pyramid pattern:")
for i in range(1, 6):
    print(" " * (6 - i) + "*" * (2 * i - 1))

#step 3
students = ["Ava", "Noah", "Liam", "Sophia"]
grades = [88, 92, 79, 95]

print("Student Grade Report:")
for i in range(len(students)):
    star = "⭐" if grades[i] > 90 else ""
    print(students[i], "-", grades[i], "%", star)

average = sum(grades) / len(grades)
print("\nClass Average:", average)

#add pass/fail
for i in range(len(grades)):
    if grades[i] >= 90:
        print(students[i], "passed with high grade!")
    elif grades[i] >= 60:
        print(students[i], "passed.")
    else:
        print(students[i], "failed.")

if average > 85:
    print("Excellent class performance!")

# Step 4: Coin Toss Simulator

import random

heads = 0
tails = 0

for toss in range(10):
    result = random.choice(["Heads", "Tails"])
    print(result)
    if result == "Heads": 
        heads += 1
    else:
        tails += 1

print("Heads:", heads)
print("Tails:", tails)

# Reflection:
# 1. The pyramid pattern was the hardest because of spacing.
# 2. Nested loops can be used in tables or  patterns in real apps.
# 3. Combining for and while loops can make games or repeated actions work better.
