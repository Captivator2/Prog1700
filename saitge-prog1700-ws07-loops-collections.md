## ![alt text](image.png)

---

## 1) Activity Details

* **Course Code & Name:** PROG1700 – Logic & Programming
* **Instructor:** Davis Boudreau
* **Activity Title:** Loops + Collections Arcade (While & For with Lists/Tuples/Sets/Dicts)
* **Type:** Guided Tutorial / Class Activity
* **Duration:** 1.5–2.0 hours
* **Due:** End of class
* **Submission Format:** One Python file
* **File Naming Format:** `studentnumber_PROG1700_ws07.py`

  * *Example:* `123456_PROG1700_ws07.py`

---

## 2) Overview / Purpose

This activity blends **iteration** (`while` / `for`) with Python’s core **collections** to solve small but **functional, fun problems**:

* Manage lists with loops (filter, transform, animate)
* Unpack tuples with loops (routes, coordinates)
* Clean and merge sets with loops (unique data)
* Build and query dictionaries with loops (lookups, reports)

---

## 3) Learning Objectives

By the end of this activity, you will be able to:

* Use `while` and `for` loops to process **lists, tuples, sets, and dictionaries**.
* Choose the right collection for a task (ordered vs unique vs key–value).
* Combine loops + collections to build small, functional utilities.

---

## 4) Concept Review / Quick Cheats

```python
# List: ordered, mutable
nums = [1, 2, 3]

# Tuple: ordered, immutable
coord = (44.65, -63.57)

# Set: unordered, unique
emails = {"a@x.com", "b@x.com"}

# Dict: key -> value
grades = {"Ava": 88, "Noah": 92}
```

* Loop patterns:

```python
for x in nums: ...
for i in range(len(nums)): ...
while condition: ...
for k, v in grades.items(): ...
```

---

## 5) Integrated Tutorial / Guided Activities

> Create `studentnumber_PROG1700_ws07.py` and add a header comment with your name & student number.

### A) 🎁 List Arcade – “Gift Grab Shuffle”

**Working example (start here):**

```python
import random, time

gifts = ["🍫", "🧸", "🎮", "📚", "🎧"]
random.shuffle(gifts)

print("Shuffled gifts:", gifts)
for item in gifts:
    print("You see:", item)
```

**Improve it (choose 2+):**

* Use a **`while` loop** to pop items until the list is empty, printing a countdown.
* Add a **score**: +10 for 🎮 or 🎧, +5 for 🍫/📚, +8 for 🧸.
* Add a **delay** (`time.sleep(0.3)`) for arcade effect.
* Ask the user how many gifts to reveal (validate with a loop).

---

### B) 🗺️ Tuple Trails – “Route Runner”

**Working example (start here):**

```python
route = [("Start", "Park"), ("Park", "Cafe"), ("Cafe", "Library")]
for frm, to in route:  # tuple unpacking
    print(f"{frm} → {to}")
```

**Improve it (choose 2+):**

* Build a **distance** tuple list: `[(frm, to, km)]` and total the km.
* Use a **`while` loop** to simulate walking: print each leg, decreasing `energy` until zero.
* If a leg is ≥ 3 km, print “🚰 Water break!”.
* Ask user to **append** a new leg (frm, to, km) and replay the route.

---

### C) ✉️ Set Scrub – “Unique Email Cleaner”

**Working example (start here):**

```python
raw = ["a@x.com", "b@x.com", "a@x.com", "c@x.com", "b@x.com"]
clean = set(raw)   # remove duplicates
print("Unique:", clean)
```

**Improve it (choose 2+):**

* Keep accepting emails in a **`while` loop** until user types `"done"`, adding to a set.
* Print counts: raw vs unique; show **newly added** vs **already present**.
* Merge with an **existing set** (`known = {...}`) using `|` or `.update()` and report **delta**.
* If email lacks “@”, **skip** (use `continue`) and warn once.

---

### D) 🧾 Dict Dash – “Mini Inventory”

**Working example (start here):**

```python
inv = {"pencils": 12, "erasers": 4, "markers": 6}
for item, qty in inv.items():
    print(f"{item}: {qty}")

# Sell 2 pencils
inv["pencils"] -= 2
print("After sale:", inv)
```

**Improve it (choose 2+):**

* **Loop menu** (`while True`): (A)dd item, (S)ell item, (L)ist, (Q)uit.
* Validate sells: if `qty` would go < 0, refuse and warn.
* Compute **low-stock report** for items < 3.
* Persist a simple **sales log** (list of tuples) then loop to print a receipt.

---

## 6) Reflection (add at bottom of your .py as comments)

```python
# Reflection:
# 1) Which collection (list/tuple/set/dict) was the best fit in each mini-project, and why?
# 2) Where did a while loop make more sense than a for loop (or vice versa)?
# 3) What bug did you hit today, and how did you fix it?
# 4) One way you could reuse any mini-project in a real app?
```

---

## 7) Deliverables / Checkpoints

Submit **one** file: `studentnumber_PROG1700_ws07.py` including:

* All four mini-projects (A–D) with your chosen improvements
* Reflection comments (Section 6)
* Clean, runnable code (no syntax errors)

---

## 8) Submission

* **Where:** Brightspace (or GitHub Classroom if instructed)
* **When:** End of class
* **File Name:** `studentnumber_PROG1700_ws07.py`
* Include your **name** and **student number** in the file header.

---

## 9) Evaluation Criteria (10 marks)

| Criteria        | Description                                     | Marks  |
| --------------- | ----------------------------------------------- | ------ |
| Completion      | All 4 mini-projects attempted with improvements | 4      |
| Accuracy        | Code runs; loops & collection ops correct       | 3      |
| Reflection      | Clear, specific, thoughtful answers             | 2      |
| Professionalism | Naming, comments, formatting                    | 1      |
| **Total**       |                                                 | **10** |

---

## 10) Resources

* Python Docs: Data Structures & Control Flow
* W3Schools: Lists / Tuples / Sets / Dictionaries / Loops
* VS Code Python Extension

---

## 11) Academic Integrity

Discuss ideas, **write your own code**. Cite any external references in comments. Add comments to show your thinking.

---

### (Optional) ⭐ Level-Up Ideas

* **Hybrid**: Use a dict of lists (e.g., inventory categories → items) and loop to print a categorized report.
* **Visualizer**: For the List Arcade, print a horizontal bar chart using `"█" * qty`.
* **Router**: For Tuple Trails, compute fastest/shortest by scanning legs in a loop.

## **12. Copyright Notice**

© 2025, NSCC – for educational use only.
