#step 1
ticket = ("Halifax", "Toronto", "AC702", 349.99)
print("Flight:", ticket)
print(f"From {ticket[0]} to {ticket[1]} on flight {ticket[2]} costing ${ticket[3]}")

origin, destination, flight_num, price = ticket
print(f"{origin} ✈️ {destination} — Flight {flight_num} 🧳 Price: ${price} 🌎")

#step 2
flights = [
    ("Halifax", "Montreal", 189.99),
    ("Montreal", "Ottawa", 99.99),
    ("Ottawa", "Toronto", 159.99)
]

print("All Flights:")
for flight in flights:
    print(flight)

print("\nFlights cheaper than $150:")
for flight in flights:
    if flight[2] < 150:
        print(flight)

total = 0
for flight in flights:
    total = total + flight[2]

average = total / len(flights)
print("\nAverage flight cost:", average)

#step 3
flight = ("Halifax", "Toronto", 349.99)
print("Before update:", flight)

flight = (flight[0], "Vancouver", 499.99)
print("After update:", flight)

#step 4

orders = [
    ("Alex", "Large", ["Pepperoni", "Mushroom"]),
    ("Priya", "Medium", ["Cheese"]),
    ("Jordan", "Small", ["Veggie", "Onion"])
]
for order in orders:
    print(order[0], "ordered a", order[1], "pizza with", order[2])

count = 0
for order in orders:
    if order[1] == "Large":
        count = count + 1
print("\nNumber of Large pizzas:", count)

toppings = []
for order in orders:
    for t in order[2]:
        if t not in toppings:
            toppings.append(t)
print("All unique toppings:", toppings)



# Reflection:
# 1. Tuples are useful because they keep data safe and cannot be changed by accident.
# 2. I noticed in Step 3 that I had to make a new tuple instead of changing the old one, and that helped me understand immutability better.
# 3. I liked the pizza order exercise the most because it was easy to understand.
# 4. Tuples make sense in real life for things like flight details or student records, where the information should stay the same.

