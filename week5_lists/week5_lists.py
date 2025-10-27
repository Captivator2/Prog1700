fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

fruits[2] = "coconut"
fruits.append("fig")
fruits.remove("banana")

print("Final fruits list:", fruits)

grades = [70, 85, 90, 65, 88]
print("Original grades:")
for g in grades:
    print(g)

grades = [70, 85, 90, 65, 88]

for i in range(len(grades)):
    grades[i] = grades[i] + 5

print(grades)

grades.append(92)
lowest = min(grades)
grades.remove(lowest)

print()
print("Modified grades (after +5, add 92, removed lowest):")
print(grades)
average = sum(grades) / len(grades)
print("Average grade:", average)


#Reflection
#1.Which list operations were easiest
#The easiest list operations were printing the items and adding new ones with append. 
#It was siple to see the changes right away when i prined the list after each step.

#2.Which caused errors or unexpected results, and how did you fix them
#At first, i had a small problem with my index loop because i forgot to indent properly. 
#Python showed an error, so i fixed it by making sure the line inside the loop was indentttted by four spaces. 
#I also learned to be careful with spelling list names correctly or it wont run.

#3. How would you store additional information per item in a real-world program?
#I would put more than one thing in each list item, like a name and a grade together. 
#For example, each student could be their own small list inside a bigger list.
#That way, I can keep related information in one place and find it easily.