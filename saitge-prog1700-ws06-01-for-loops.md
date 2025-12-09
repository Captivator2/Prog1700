![alt text](image.png)

---

## **1. Activity Details**

* **Course Code & Name:** PROG1700 – Logic & Programming
* **Instructor:** Davis Boudreau
* **Activity Title:** For Loop Fiesta – Patterns, Emojis, and Data Loops
* **Type:** Guided Tutorial / Class Activity
* **Duration:** 1.5 hours
* **Due Date:** See Brightspace
* **Submission Format:**

  * Submit through **Brightspace** or **GitHub**
  * **File Naming Format:** `studentnumber_PROG1700_ws06-01-for-loops.py`
    *Example:* `w123456_PROG1700_ws06-01-for-loops.py`

---

## **2. Overview / Purpose / Objectives**

The **`for` loop** allows you to process data efficiently and generate beautiful patterns with ease. In this workshop, you’ll learn to:

* Control iterations using `range()` and sequences
* Build visual outputs using loops and characters
* Process lists using loop indices
* Combine loops with conditions to make interactive or creative programs

---

## **3. Learning Outcomes Addressed**

* **O1:** Translate logic into executable code
* **O5:** Use loops for modular, efficient program structure
* **O6:** Design and implement iteration patterns
* **O7:** Debug and test repetitive logic

---

## **4. Assignment Description / Use Case**

This session includes **four guided examples** followed by an optional **Level-Up Challenge**.
Each section starts with a working example, then asks you to **improve it creatively** and reflect.

---

## **5. Tasks / Instructions**

---

### 🎯 **Step 1 – Counting & Ranges**

```python
# Simple range example
for i in range(1, 6):
    print("Count:", i)
print("Done!")
```

✅ **Try it:** See how `range(1, 6)` includes 1–5.
💡 **Improve it:**

* Count **by twos**: `range(2, 12, 2)`
* Print the **square** of each number.
* Add an emoji counter, e.g. `print("⭐" * i)`
* Challenge: Count backward with `range(10, 0, -1)`

---

### 🧱 **Step 2 – Pattern Printing Party**

Create art with nested `for` loops.

#### Example 1 – Triangle

```python
for i in range(1, 6):
    print("*" * i)
```

#### Example 2 – Pyramid of Emojis 🎈

```python
for i in range(1, 6):
    print(" " * (6 - i) + "🎈" * (2 * i - 1))
```

💡 **Improve it:**

* Change symbols (🌲, 🧊, 🔺, 💎).
* Create a **reverse triangle** or **diamond shape**.
* Make an animated countdown rocket using `time.sleep(1)`.
* Optional: Add color using ANSI codes (`\033[31m` for red).

---

### 💾 **Step 3 – Real-World Example: Student Grade Summary**

```python
students = ["Ava", "Noah", "Liam", "Sophia"]
grades = [88, 92, 79, 95]

print("Student Grade Report:")
for i in range(len(students)):
    print(f"{students[i]} → {grades[i]}%")

average = sum(grades) / len(grades)
print(f"\nClass Average: {average:.1f}%")
```

💡 **Improve it:**

* Add **Pass/Fail** based on grade.
* Print a ⭐ next to scores above 90.
* Let the user add another name and grade.
* If average > 85, print `"Excellent class performance!"`.

---

### 🌈 **Step 4 – Creative Challenge: Loop Your Own Way**

Pick one of these or invent your own!

#### 1. **🎲 Coin Toss Simulator**

```python
import random, time
heads = 0
tails = 0

for toss in range(10):
    result = random.choice(["Heads", "Tails"])
    print(result)
    if result == "Heads": heads += 1
    else: tails += 1
    time.sleep(0.2)
print(f"Heads: {heads}, Tails: {tails}")
```

#### 2. **🎶 Beat Maker**

Use loops and delays to simulate rhythm:

```python
import time
for i in range(8):
    print("Boom 🥁")
    time.sleep(0.3)
    print("Clap 👏")
    time.sleep(0.3)
```

#### 3. **🌊 Wave Generator**

Print patterns that flow across the screen:

```python
for i in range(1, 20):
    print("~" * i)
for i in range(20, 0, -1):
    print("~" * i)
```

💡 **Your Task:**
Customize one! Change emojis, timing, or logic. Add a loop counter or sound (`print("\a")`).

---

## 🧩 **Level-Up Challenge: Nested Loops & Pattern Mastery (Optional Extension)**

### 🎨 **Option 1 – Multiplication Table**

```python
for row in range(1, 11):
    for col in range(1, 11):
        print(f"{row * col:4}", end="")
    print()
```

💡 **Challenges**

* Highlight the diagonal (`if row == col`).
* Ask the user for table size.
* Add headers for rows/columns.

---

### 🧩 **Option 2 – Emoji Mosaic Artist**

```python
rows = 6
cols = 6
for r in range(rows):
    for c in range(cols):
        if (r + c) % 2 == 0:
            print("🟥", end="")
        else:
            print("⬜", end="")
    print()
```

💡 Add:

* Randomized colors or emojis
* Animated redraw using `time.sleep()`

---

### 🕹️ **Option 3 – Mini Maze Explorer**

```python
for row in range(5):
    for col in range(5):
        if row == 2 and col == 3:
            print("🙂", end="")
        else:
            print("⬜", end="")
    print()
```

💡 Add:

* Player movement logic
* Obstacles (`🧱`) and treasure (`💎`)
* Simple while loop for player movement

---

### 🧠 **Reflection (Optional)**

```python
# Level-Up Reflection:
# 1. Which nested loop pattern challenged you most?
# 2. Where could nested loops be useful in real applications?
# 3. How would combining 'for' and 'while' loops expand possibilities?
```

💯 **Optional**

| Criteria   | Description                                       |
| ---------- | ------------------------------------------------- |
| Creativity | Unique pattern, animation, or interactivity added |
| Accuracy   | Nested loops structured and working correctly     |

---

## **6. Deliverables**

Submit **one `.py` file** named:
`studentnumber_PROG1700_ws06-01-for-loops.py`
Your file must include:

* All four main examples (Steps 1–4)
* Any Level-Up Challenge (optional)
* Reflections as code comments

---

## **7. Reflection Questions**

```python
# Reflection:
# 1. What pattern or challenge was most fun, and why?
# 2. How does a for loop differ from a while loop?
# 3. What real-world problems could you solve using for loops?
# 4. How did you ensure your loops didn’t run infinitely?
```

---

## **8. Assessment & Rubric**

| Criteria   | Description                             | Marks                            |
| ---------- | --------------------------------------- | -------------------------------- |
| Completion | All examples complete and functional    | 3                                |
| Accuracy   | Loops perform correctly and efficiently | 3                                |
| Creativity | Original enhancements or visual output  | 2                                |
| Reflection | Thoughtful and complete answers         | 2                                |
| **Total**  |                                         | **10 marks** |

---

## **9. Submission Guidelines**

* Submit through **Brightspace** or **GitHub** by end of class.
* Ensure the file runs cleanly and includes your name and student number.
* Comment your logic and highlight any creative improvements.

---

## **10. Resources / Equipment**

* Python 3.x
* VSCode with Python extension
* [W3Schools – Python For Loops](https://www.w3schools.com/python/python_for_loops.asp)
* [Programiz – For Loops Explained](https://www.programiz.com/python-programming/for-loop)
* [Real Python – Loop Patterns](https://realpython.com/python-for-loop/)

---

## **11. Academic Policies**

All work must be your own.
Discuss logic ideas with peers, but do not share code.
Comment your reasoning to show comprehension.

---

## **12. Copyright Notice**

© 2025, NSCC. Educational use only.
