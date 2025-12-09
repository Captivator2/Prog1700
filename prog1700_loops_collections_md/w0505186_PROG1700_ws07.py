# A) List Arcade – Gift Grab Shuffle

import random
import time

gifts = ["chocolate", "teddy", "game", "book", "headphones"]

# shuffle the gifts
random.shuffle(gifts)

print("Shuffled gifts:")
print(gifts)

score = 0

print("\nRevealing gifts:")

# use a while loop to pop items until the list is empty
while len(gifts) > 0:
    print("Gifts left:", len(gifts))

    item = gifts.pop()      # take one gift from the end
    print("You got:", item)

    # scoring rules
    if item == "game" or item == "headphones":
        score += 10
    elif item == "chocolate" or item == "book":
        score += 5
    elif item == "teddy":
        score += 8

    time.sleep(0.3)         # small delay

print("\nAll gifts taken.")
print("Final score:", score)

# B) Tuple Trails – Route Runner

# simple route with distances
route = [
    ("Start", "Park", 2),
    ("Park", "Cafe", 3),
    ("Cafe", "Library", 1)
]

print("\nRoute:")
total_km = 0

for frm, to, km in route:
    print(frm, "→", to, "-", km, "km")
    total_km += km
    if km >= 3:
        print("Water break!")
        
print("Total distance:", total_km, "km")

# add one more leg from user
print("\nAdd a new route step.")
frm = input("From: ")
to = input("To: ")
km = float(input("Distance in km: "))

route.append((frm, to, km))

print("\nNew full route:")
for frm, to, km in route:
    print(frm, "→", to, "-", km, "km")


# C) Set Scrub – Unique Email Cleaner

raw_emails = []
unique_emails = set()

print("\nEnter emails one at a time. Type 'done' to stop.")

while True:
    email = input("Email: ").strip()

    if email.lower() == "done":
        break

    if "@" not in email:
        print("Invalid email. Must contain '@'.")
        continue

    # keep all raw emails (including duplicates)
    raw_emails.append(email)

    # check if already seen
    if email in unique_emails:
        print("Already added.")
    else:
        print("New email added.")
        unique_emails.add(email)

print("\n--- Email Summary ---")
print("Total entered:", len(raw_emails))
print("Unique emails:", len(unique_emails))
print("Unique list:", unique_emails)

# D) Dict Dash – Mini Inventory

inventory = {"pencils": 12, "erasers": 4, "markers": 6}
sales_log = []   # list of tuples (item, qty)

while True:
    print("\nInventory Menu:")
    print("A - Add item")
    print("S - Sell item")
    print("L - List inventory")
    print("Q - Quit")

    choice = input("Choose an option: ").lower()

    if choice == "a":
        item = input("Item name: ").lower()
        qty = int(input("Quantity to add: "))
        inventory[item] = inventory.get(item, 0) + qty
        print("Item added.")

    elif choice == "s":
        item = input("Item to sell: ").lower()
        qty = int(input("Quantity to sell: "))

        if item not in inventory:
            print("Item not found.")
            continue

        if inventory[item] - qty < 0:
            print("Not enough stock.")
            continue

        inventory[item] -= qty
        sales_log.append((item, qty))
        print("Sale recorded.")

    elif choice == "l":
        print("\nCurrent Inventory:")
        for item, qty in inventory.items():
            print(item, ":", qty)

        print("\nLow stock (<3):")
        for item, qty in inventory.items():
            if qty < 3:
                print(item, "is low.")

    elif choice == "q":
        print("Exiting inventory menu.")
        break

    else:
        print("Invalid option.")


# Reflection:
# 1) Lists worked best for the gift game, tuples worked well for routes,
#    sets were best for cleaning emails, and dictionaries were good for inventory.
# 2) A while loop made more sense when the program needed a menu or repeated input.
#    A for loop was better when just going through items one time.
# 3) One bug I had was something not updating correctly, and I fixed it by checking
#    my loop and correcting the condition.
# 4) I could reuse one of these mini-projects in a real app, like a small inventory tool.
