## ![alt text](image.png)

---

## **Course Information**

* **Course Code & Name:** PROG1700 – Logic & Programming
* **Instructor:** Davis Boudreau
* **Workshop Title:** While Loop Challenge Lab
* **Activity Type:** Guided Workshop / Lab
* **Duration:** 1.5 hours
* **Due:** See Brightspace
* **Submission Format:**
  Submit through **Brightspace** or **GitHub**
* **File Naming Format:**
  `studentnumber_PROG1700_ws06-03.py`
  *Example:* `123456_PROG1700_ws06-03.py`

---

## **1. Activity Overview**

In this lab, you’ll explore **while loops** through a series of short, fun programming challenges.
You’ll create programs that repeat actions until a condition changes — the core idea behind **iteration and automation** in programming.

Each challenge builds your ability to:

* Control program flow using logical conditions
* Use counters and sentinels (flags)
* Validate input and repeat until correct
* Create loops that are efficient and predictable

By the end of this workshop, you’ll understand how to write, debug, and refine while loops to solve real problems.

---

## **2. Learning Objectives**

After completing this activity, you will be able to:

* Implement while loops for repetition and control.
* Use Boolean conditions and counters effectively.
* Combine loops with user input and data validation.
* Debug infinite loops and logical errors in loop conditions.

---

## **3. Concept Review / Lesson Content**

A **while loop** repeats a block of code **as long as** its condition is `True`.

```python
count = 0
while count < 5:
    print("Loop number:", count)
    count += 1
```

The key difference from a `for` loop is that **you control the stopping condition manually** — which is both powerful and dangerous (hello, infinite loops 👀).

---

## **4. Integrated Tutorial / Guided Activity**

### 🎯 **Step 1 – Number Guesser**

Challenge the computer or let it challenge you!

```python
import random
secret = random.randint(1, 10)
guess = 0

while guess != secret:
    guess = int(input("Guess a number (1–10): "))
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("You got it!")
```

💡 **Try This:**

* Limit the number of guesses to 5.
* Use a counter to print “You’re out of tries!” if exceeded.
* Add input validation for non-numeric entries.

---

### 🪙 **Step 2 – Coin Flipper**

Simulate flipping a coin multiple times.

```python
import random

heads = 0
tails = 0
count = 0

while count < 10:
    flip = random.choice(["Heads", "Tails"])
    print(flip)
    if flip == "Heads":
        heads += 1
    else:
        tails += 1
    count += 1

print(f"Heads: {heads}, Tails: {tails}")
```

💡 **Try This:**

* Ask the user how many flips they want.
* Track percentage of heads vs. tails.
* Stop early if one side reaches 70%.

---

### ⏱️ **Step 3 – Countdown Timer**

Make a countdown loop that ticks down to launch 🚀

```python
import time

count = 10
while count >= 0:
    print(count)
    time.sleep(1)
    count -= 1
print("Blast off! 🚀")
```

💡 **Try This:**

* Add sound (`print("\a")`) each second.
* Ask the user for the starting number.
* Print emojis or “progress bars” (`"=" * count`).

---

### 🎨 **Step 4 – Pattern Generator**

Use a while loop to draw patterns dynamically.

```python
rows = 1
while rows <= 5:
    print("*" * rows)
    rows += 1
```

💡 **Try This:**

* Ask user for pattern size and character.
* Invert it: print decreasing stars.
* Combine with loops to print emoji art (`"💫" * rows`).

---

## **5. Reflection**

Add your reflection at the bottom of your file as comments:

```python
# Reflection:
# 1. Which challenge did you find most fun or surprising?
# 2. What is one common mistake that caused infinite loops today?
# 3. How could while loops be used in a real-world app?
# 4. Which activity helped you best understand “loop conditions”?
```

---

## **6. Deliverables**

Submit **one `.py` file** named:
`studentnumber_PROG1700_ws06-03.py`

Include:

* All four challenges (Steps 1–4)
* Any improvements or variations you added
* Your reflection comments

---

## **7. Submission**

* Submit via **Brightspace** (or GitHub if instructed).
* **Due:** End of class.
* Ensure file runs without syntax errors.
* Include your name and student number in file header.

---

## **8. Evaluation Criteria**

| Criteria   | Description                                          | Marks        |
| ---------- | ---------------------------------------------------- | ------------ |
| Completion | All examples and variations completed                | 3            |
| Accuracy   | Code executes correctly and loops terminate properly | 3            |
| Creativity | Personalized or enhanced versions                    | 2            |
| Reflection | Clear, thoughtful responses                          | 2            |
| **Total**  |                                                      | **10 marks** |

---

## **9. Resources**

* [W3Schools – Python While Loops](https://www.w3schools.com/python/python_while_loops.asp)
* [Real Python – Looping in Python](https://realpython.com/python-while-loop/)
* [Programiz – Python While Examples](https://www.programiz.com/python-programming/while-loop)
* VSCode with Python Extension

---

## **10. Academic Integrity**

All code must be written individually.
Collaboration for learning is encouraged — copying code is not.
Use comments to explain your thought process.

---

## **11. Copyright Notice**

© 2025, NSCC – for educational use only.
