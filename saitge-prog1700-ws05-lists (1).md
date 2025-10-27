![alt text](image.png)

**Instructor:** Davis Boudreau

**Activity Title:** Working with Python Lists (CRUD Operations)

**Activity Type:** Integrated Tutorial & Guided Practice

**Duration:** 1 Lab Session (~2 hours)

**Submission:** Completed script submitted at end of class via Brightspace or GitHub repository.

---

## **1. Activity Overview**

In this tutorial, students will learn how to **store, access, and modify collections of data using Python lists**.
Through a series of short, guided exercises, students will perform CRUD operations (Create, Read, Update, Delete) and explore **real-world examples**, including inventory tracking, to-do lists, and classroom data management.

By the end, students will have hands-on experience writing and modifying list-based programs that model practical, everyday problems.

---

## **2. Learning Objectives**

By completing this activity, you will be able to:

* Define and create lists in Python.
* Access list elements using indices and slicing.
* Add, update, and remove items from a list.
* Iterate through lists using loops.
* Apply list operations in simple real-world scenarios.

---

## **3. Lesson Content / Concept Review**

### 🧠 What is a List?

A **list** is an ordered, changeable collection in Python that can hold multiple items.
Example:

```python
fruits = ["apple", "banana", "cherry"]
```

### ⚙️ Common Operations (CRUD)

| Operation  | Action        | Example                   |
| ---------- | ------------- | ------------------------- |
| **Create** | Add new data  | `fruits.append("orange")` |
| **Read**   | Retrieve data | `print(fruits[0])`        |
| **Update** | Change data   | `fruits[1] = "grape"`     |
| **Delete** | Remove data   | `fruits.remove("apple")`  |

---

## **4. Integrated Tutorial & Activities**

### 🪜 **Step 1: Create Your First List**

**Goal:** Create a list of your top 5 favorite movies.

1. Open VSCode and create a file named `student_number_prog1700-lists-01.py`.
2. Create a list named `movies` with 5 of your favorite movies.
3. Print the entire list using `print()`.
4. Use indexing to print the *first* and *last* movie in the list.

**Challenge:**
Change one movie and print the updated list.

---

### 🧾 **Step 2: Reading & Accessing Data**

**Goal:** Practice indexing and slicing.

```python
numbers = [10, 20, 30, 40, 50]
```

Try:

* Printing the 3rd number.
* Printing the last 2 numbers (use slicing).
* Printing the total count using `len(numbers)`.

**Challenge:**
Write a loop that prints each element with its position (index + 1).

---

### 🛒 **Step 3: Real-World Example – Grocery Inventory**

Imagine you’re building a **grocery inventory app** for a small store.
Start with a list of items:

```python
inventory = ["milk", "bread", "eggs"]
```

Perform the following:

1. Add `"butter"` and `"cheese"` to your list using `.append()`.
2. Insert `"apples"` at the beginning of the list.
3. Replace `"bread"` with `"whole grain bread"`.
4. Remove `"eggs"` from the list.
5. Print the updated list after each change.

**Challenge:**
Print how many items are left in inventory using `len(inventory)`.

---

### 📋 **Step 4: To-Do List Manager (Mini Exercise)**

Create a simple **to-do list manager** that:

1. Starts with an empty list called `tasks = []`.
2. Allows the user to:

   * Add new tasks (`append()`)
   * Mark a task as done (`pop()` or `remove()`)
   * View all tasks (`for` loop)
3. Prints a friendly message when the user exits.

**Hint:** Use a loop to display a small menu like:

```
1. Add Task
2. Remove Task
3. View Tasks
4. Exit
```

**Challenge:**
Can you make your program keep running until the user chooses “Exit”?

---

### 🧩 **Step 5: Reflection (At End of Class)**

Answer the following reflection questions **in a comment block** at the bottom of your Python file:

```python
# Reflection:
# 1. What is one real-world use of lists you can think of in your life or work?
# 2. Which list operation (Create, Read, Update, Delete) do you find easiest or hardest, and why?
# 3. How would you explain the concept of indexing to someone new to Python?
```

---

## **5. Deliverables**

At the end of class, submit the following via **Brightspace**:

* Completed file: `student_number_prog1700-lists-01.py`
* Ensure your reflection is included as a comment.

---

## **6. Evaluation**

| Criteria        | Description                           | Marks  |
| --------------- | ------------------------------------- | ------ |
| Completion      | All steps and exercises completed     | 4      |
| Accuracy        | Code runs without major errors        | 3      |
| Understanding   | Reflection answers show comprehension | 2      |
| Professionalism | Proper formatting and comments        | 1      |
| **Total**       |                                       | **10** |

---

## **7. Resources**

* **Python Docs:** [https://docs.python.org/3/tutorial/datastructures.html](https://docs.python.org/3/tutorial/datastructures.html)
* **W3Schools Lists Tutorial:** [https://www.w3schools.com/python/python_lists.asp](https://www.w3schools.com/python/python_lists.asp)
* **Replit (optional practice):** [https://replit.com/~](https://replit.com/~)

---

## **8. Academic Integrity**

All submitted work must be your own.
You are encouraged to discuss and debug with peers but **not to copy code**.
Use comments to explain your logic whenever possible.
