# Step 1 - Tuple Basics: Airline Ticket

ticket = ("Halifax", "Toronto", "AC702", 349.99)

print("Flight:", ticket)
print("From", ticket[0], "to", ticket[1], "on flight", ticket[2], "costing $", ticket[3])

# Challenge: unpacking
origin, destination, flightnum, price = ticket
print("Trip from", origin, "to", destination, "costs", price)

# Step 2 - Tuple Collections: Travel Itinerary

flights = [
    ("Halifax", "Montreal", 189.99),
    ("Montreal", "Ottawa", 99.99),
    ("Ottawa", "Toronto", 159.99)
]

# Print all flights
for origin, destination, price in flights:
    print(origin, "to", destination, "costs $", price)

# Challenge 1: print flights cheaper than $150
print("\nFlights under $150:")
for f in flights:
    if f[2] < 150:
        print(f[0], "to", f[1], "costs $", f[2])

# Challenge 2: total price using while loop
total = 0
i = 0
while i < len(flights):
    total += flights[i][2]
    i += 1

# Challenge 3: average
average = total / len(flights)
print("\nAverage flight cost:", average)

# Step 3 - Simulating Updates (Immutability)

flight = ("Halifax", "Toronto", 349.99)
print("Before:", flight)

# "Update" the tuple by creating a new one
flight = (flight[0], "Vancouver", flight[2] + 150)
print("After:", flight)

# Simple update function (challenge)
def update_flight(f, new_dest, new_price):
    return (f[0], new_dest, new_price)

# Example of using the function
new_flight = update_flight(flight, "Calgary", flight[2] + 100)
print("Updated again:", new_flight)


# Reflection:
# 1. Tuples are useful because they keep data together and can’t change by accident.
# 2. I noticed immutability most in Step 3 because I had to make a new tuple instead of editing it.
# 3. I liked the pizza orders because it was easy to understand and felt like a real example.
# 4. A real-life example for tuples is storing coordinates or a record like a name and age.

