# A) Text Log – Daily Summary Writer

while True:
    note = input("Enter a daily note (or type 'done' to stop): ")

    if note.lower() == "done":
        break

    if note.strip() == "":
        continue

    # add the note to the file
    with open("daily_log.txt", "a") as file:
        file.write(note + "\n")

# print all notes after the user finishes
print("\nAll Log Entries:")

with open("daily_log.txt", "r") as file:
    for line in file:
        print(line.strip())

# B) Text Reader – Grocery Inventory

total_value = 0

with open("inventory.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line == "":
            continue

        name, price = line.split(",")
        price = float(price)

        print(name, "costs $", price)

        total_value += price

print("\nTotal inventory value:", total_value)

# C) CSV Writer – Café Sales Export

import csv

# Simple café sales list
sales = [
    ["Latte", 12, 3.25],
    ["Tea", 10, 2.50],
    ["Muffin", 5, 2.00]
]

# Write the CSV file
with open("cafe_sales.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Item", "Quantity", "Price"])  # header row
    for row in sales:
        writer.writerow(row)

print("cafe_sales.csv has been created.")

# D) CSV Reader – Student Grades Report

import csv

grades = []

# Read the grades file
with open("grades.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # skip the header
    for row in reader:
        name = row[0]
        grade = float(row[1])
        grades.append((name, grade))

# Print each name and grade
print("\nStudent Grades:")
for name, grade in grades:
    print(name, "-", grade)

# Calculate statistics
all_grades = [g for (n, g) in grades]
average = sum(all_grades) / len(all_grades)
highest = max(all_grades)
lowest = min(all_grades)

# Find who got highest + lowest
for name, grade in grades:
    if grade == highest:
        top_student = name
    if grade == lowest:
        bottom_student = name

# Write summary to file
with open("grades_summary.txt", "w") as file:
    file.write("Grades Summary Report\n")
    file.write("----------------------\n")
    file.write(f"Average Grade: {average}\n")
    file.write(f"Highest Grade: {highest} ({top_student})\n")
    file.write(f"Lowest Grade:  {lowest} ({bottom_student})\n")

print("\ngrades_summary.txt has been created.")


# Reflection:
# 1. File persistence makes programs more useful because the data stays saved even after the program ends.
# 2. CSV files were a bit easier to use because the data was already in a clean table format.
# 3. A program that tracks sales or grades could use both text files and CSV files together.
# 4. One problem I had was the file not being found, and I fixed it by making sure the file was in the same folder as my Python file.
