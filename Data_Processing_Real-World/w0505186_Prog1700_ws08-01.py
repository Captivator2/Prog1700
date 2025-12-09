#step 1
temperatures = [14, 16, 18, 17, 20, 19, 15]

# Show all temperatures
print("Temperatures for the week:")
for temp in temperatures:
    print(temp)

# Average
total = 0
for temp in temperatures:
    total += temp
average = total / len(temperatures)
print("Average temperature:", average)

# Highest and lowest
print("Highest temperature:", max(temperatures))
print("Lowest temperature:", min(temperatures))

# Weather Reporter
temperatures = [14, 16, 18, 17, 20, 19, 15]

# Show all temperatures
print("Temperatures for the week:")
for temp in temperatures:
    print(temp)

# Average
total = 0
for temp in temperatures:
    total += temp
average = total / len(temperatures)
print("Average temperature:", average)

# Highest and lowest
print("Highest temperature:", max(temperatures))
print("Lowest temperature:", min(temperatures))

# Days above 18°C
count = 0
for temp in temperatures:
    if temp > 18:
        count += 1
print("Days above 18°C:", count)

# Add new temperatures
while True:
    new_temp = input("Enter a new temperature (or 'done' to stop): ")
    if new_temp == "done":
        break
    temperatures.append(int(new_temp))

# Remove duplicates using set
unique_temps = set(temperatures)
print("Unique temperatures recorded:", unique_temps)

# Days above 18°C
count = 0
for temp in temperatures:
    if temp > 18:
        count += 1
print("Days above 18°C:", count)

# Remove duplicates using set
unique_temps = set(temperatures)
print("Unique temperatures recorded:", unique_temps)

print("All temperatures now:", temperatures)

#step 2
books = {
    "Python Basics": 3,
    "Web Design 101": 2,
    "Networking Made Easy": 1
}

while True:
    for title, qty in books.items():
        print(title, "→", qty)

    action = input("\nType 'checkout', 'return', or 'done': ")

    if action == "done":
        break

    title = input("Enter book name: ")

    if action == "checkout":
        if title in books:
            if books[title] > 0:
                books[title] -= 1
                print("Checked out one copy.")
            else:
                print("No copies left!")
        else:
            print("Book not found.")

    elif action == "return":
        if title in books:
            books[title] += 1
            print("Returned one copy.")
        else:
            books[title] = 1
            print("Added new book to list.")

    else:
        print("Invalid option.")

# Fix any negatives
for title, qty in books.items():
    if qty < 0:
        books[title] = 0
        print(title, "set to 0 (cannot be negative).")

# Find fewest copies
fewest_title = min(books, key=books.get)
print("\nBook with fewest copies:", fewest_title, "→", books[fewest_title])

# Total books in circulation
total = 0
for qty in books.values():
    total += qty
print("Total books in circulation:", total)

#step 3
items = ["Latte", "Espresso", "Tea", "Muffin"]
sales = [12, 8, 10, 6]

# Show sales report
print("\nSales report:")
for i in range(len(items)):
    print(items[i], "-", sales[i], "sold")

# Add new items
while True:
    new_item = input("Add a new item (or 'done' to stop): ")
    if new_item == "done":
        break
    new_count = int(input("How many sold? "))
    items.append(new_item)
    sales.append(new_count)


# Total and average sales
total_sales = 0
for s in sales:
    total_sales = total_sales + s

average_sales = total_sales / len(sales)
print("\nTotal sales:", total_sales)
print("Average sales per item:", average_sales)

# Best-selling item
best = max(sales)
best_item = items[sales.index(best)]
print("Best-selling item:", best_item, "with", best, "sales")

# Unique menu items
unique_items = set(items)
print("Unique items sold:", unique_items)

#step 4
adoptions = {
    "Cats": 4,
    "Dogs": 6,
    "Rabbits": 2
}

# Let user log more adoptions
while True:
    add = input("Log an adoption? (yes/no): ")
    if add == "no":
        break
    species = input("Enter species: ")
    num = int(input("How many adopted?: "))
    if num < 0:
        print("Invalid number. Enter a positive number.")
        continue
    if species in adoptions:
        adoptions[species] = adoptions[species] + num
    else:
        adoptions[species] = num

#Print report
print("\nAdoption report:")
for species, count in adoptions.items():
    print(species, "-", count, "adopted")

# Unique species seen
unique_species = set(adoptions.keys())
print("\nUnique species:", unique_species)

# Total adoptions
total_adopted = 0
for count in adoptions.values():
    total_adopted = total_adopted + count
print("Total adoptions:", total_adopted)

# Most popular pet
most_popular = max(adoptions, key=adoptions.get)
print("Most popular pet:", most_popular, "with", adoptions[most_popular], "adoptions")




# Reflection:
# 1. The café sales dataset was easiest because it used two matching lists and simple sums.
# 2. Loops make repetitive tasks faster because they do the same work many times without typing it again.
# 3. The most useful collection type was the dictionary because it’s easy to match names with numbers.
# 4. Next week I would add more data or more options.

