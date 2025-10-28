#step 1
groceries = {
    "Apples": 3.50,
    "Bananas": 2.75,
    "Bread": 2.99,
    "Milk": 4.29,
    "Eggs": 3.49
}

while True:
    add_item = input("Do you want to add a new item? (yes/no): ")
    if add_item.lower() == "no":
        break
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    groceries[name] = price

for item in groceries:
    if groceries[item] > 4.00:
        groceries[item] = groceries[item] * 0.9

#step 2
students = ["Ava", "Noah", "Liam"]
grades = [88, 92, 79]

print("Student Grades:")
for i in range(len(students)):
    print(students[i], "-", grades[i])

while True:
    name = input("Enter a student name (or done to stop): ")
    if name == "done":
        break
    grade = int(input("Enter grade: "))
    students.append(name)
    grades.append(grade)

print("\nUpdated List:")
for i in range(len(students)):
    print(students[i], "-", grades[i])

average = sum(grades) / len(grades)
print("\nAverage grade:", average)
print("Highest grade:", max(grades))

#step 3
scores = {"Alex": 12, "Priya": 18, "Jordan": 9}

print("Player Scores:")
for name in scores:
    print(name, "-", scores[name])

while True:
    player = input("Enter player name (or done to stop): ")
    if player == "done":
        break
    points = int(input("Enter score: "))
    scores[player] = points

print("\nFinal Scores:")
for name in scores:
    print(name, "-", scores[name])

top = max(scores, key=scores.get)
print("\nTop player:", top, "with", scores[top], "points")

for name in scores:
    if scores[name] > 20:
        print(name, "leveled up!")

#step 4
songs = ["Song A", "Song B", "Song C"]
plays = [5, 10, 7]

print("Songs and plays:")
for i in range(len(songs)):
    print(songs[i], "-", plays[i], "plays")

while True:
    new_song = input("Add a new song (or done to stop): ")
    if new_song == "done":
        break
    new_plays = int(input("How many plays? "))
    songs.append(new_song)
    plays.append(new_plays)

most = max(plays)
least = min(plays)
print("\nMost played song:", songs[plays.index(most)])
print("Least played song:", songs[plays.index(least)])

total = sum(plays)
average = total / len(plays)
print("Total plays:", total)
print("Average plays per song:", average)

#Reflection
# 1. The grocery analyzer felt most realistic because people often check prices and totals.
# 2. Loops make data easier to handle because they repeat work automatically.
# 3. It was hard to keep track of indexes when using lists together.
# 4. I could expand the playlist project to show total play time or favorite songs.