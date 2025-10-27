students = [["Alice", 85], ["Bob", 90], ["Charlie", 78]]

print("Original students and grades:")
for s in students:
    print(s[0], "-", s[1])

students.append(["Diana", 88])

for s in students:
    s[1] = s[1] + 2


print()
print("Updated students and grades:")
for s in students:
    print(s[0], "-", s[1])
