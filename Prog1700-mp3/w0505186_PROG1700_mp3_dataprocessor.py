import os
print("Running from:", os.getcwd())

# Step 2 – Plan for my program
# 1. Read the grades.csv file.
# 2. Store each student name and grade in a list.
# 3. Loop through the list to find:
#  - average grade
#  - highest grade
#  - lowest grade
# 4. Make a summary of the results.
# 5. Save the summary to a file called grades_summary.txt
# 6. Also print the main results on the screen.

# Step 6 – Functions

def read_file(filename):
    records = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            name, score = line.split(",")
            records.append((name, float(score)))
    return records


def process_data(records):
    grades = [grade for (name, grade) in records]

    avg_grade = sum(grades) / len(grades)
    highest = max(grades)
    lowest = min(grades)

    top_name = ""
    low_name = ""

    for name, grade in records:
        if grade == highest:
            top_name = name
        if grade == lowest:
            low_name = name

    return avg_grade, highest, lowest, top_name, low_name


def write_report(filename, avg, high, low, top, bottom):
    with open(filename, "w") as f:
        f.write("Grades Summary\n")
        f.write("-----------------\n")
        f.write(f"Average Grade: {avg}\n")
        f.write(f"Highest Grade: {high} ({top})\n")
        f.write(f"Lowest Grade: {low} ({bottom})\n")

# Step 3 & Step 4 – Read and store file data

records = read_file("grades.csv")

print("Data loaded from file:")
for item in records:
    print(item)

# Step 5 – Process the data

avg_grade, highest_grade, lowest_grade, top_student, bottom_student = process_data(records)

print("\nSummary of Grades:")
print("Average grade:", avg_grade)
print("Highest grade:", highest_grade)
print("Lowest grade:", lowest_grade)
print("Top student:", top_student)
print("Lowest student:", bottom_student)

# Step 7 – Write the summary to a file

write_report("grades_summary.txt", avg_grade, highest_grade, lowest_grade, top_student, bottom_student)

print("\nSummary written to grades_summary.txt")



# Reflection:
# 1) I used lists and tuples because they were the easiest way for me to store the names and grades together. 
#    A list let me hold all the records, and each record was a small tuple with two values.
# 2) The hardest bug I fixed was when the program couldn’t find the grades.csv file. 
#    I realized the issue was that my terminal wasn’t in the same folder as the file.
#    Once I changed the folder in VS Code, it worked properly.
# 3) Saving the summary to a file makes the program more useful because it keeps the results even after the program closes.
#    I can open the summary anytime, and it feels more like a real tool.
# 4) If I expanded the project, I would add a feature that shows which students passed or failed 
#    or maybe sort the grades from highest to lowest to make the report more detailed.
