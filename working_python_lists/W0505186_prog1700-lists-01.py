#step 1
movies = ["The Matrix", "Inception", "The Lion King", "Spirited Away", "Back to the Future"]
print("All movies:", movies)

print("First movie:", movies[0])
print("Last movie:", movies[-1])

movies[2] = "Toy Story"
print("Updated movies:", movies)

#step 2
numbers = [10, 20, 30, 40, 50]
print("Third number:", numbers[2])
print("Last two numbers:", numbers[-2:])
print("Total count:", len(numbers))

print("Numbers with positions:")

position = 1
for number in numbers:
    print("Position", position, "->", number)
    position = position + 1

    #step 3
    inventory = ["milk", "bread", "eggs"]
print("Starting inventory:", inventory)

inventory.append("butter")
inventory.append("cheese")
print("After adding butter and cheese:", inventory)

inventory.insert(0, "apples")
print("After adding apples at the beginning:", inventory)

inventory[2] = "whole grain bread"
print("After replacing bread:", inventory)

inventory.remove("eggs")
print("After removing eggs:", inventory)

print("Total items in inventory:", len(inventory))

# step 4
tasks = []

while True:
    print("\nTo-Do List Menu")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Added!")

    elif choice == "2":
        task = input("Enter a task to remove: ")
        if task in tasks:
            tasks.remove(task)
            print("Removed!")
        else:
            print("Not found.")

    elif choice == "3":
        print("Your To-Do List:")
        if tasks:
            for t in tasks:
                print("-", t)
        else:
            print("No tasks yet.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")


# ---------------------------------------------------
# Step 5: Reflection
# ---------------------------------------------------

# Reflection:
# 1. One real-world use of lists I can think of is keeping track of tasks or shopping items.
# 2. The easiest operation was adding items with append(), and the hardest was removing items if they were not in the list.
# 3. Indexing is like giving each item a number so you can find or change it easily.
