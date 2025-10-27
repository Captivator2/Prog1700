# extra3_pizza.py

# Ask for pizza size
size = input("Do you want a small, medium, or large pizza? ").lower()

# Set base price
if size == "small":
    price = 8
elif size == "medium":
    price = 10
elif size == "large":
    price = 12
else:
    print("Invalid size selected. Defaulting to small.")
    price = 8

# Ask about extra cheese
cheese = input("Do you want extra cheese? (yes/no) ").lower()
if cheese == "yes":
    price += 2

# Ask about delivery
delivery = input("Do you want delivery? (yes/no) ").lower()
if delivery == "yes":
    price += 3

# Check for big order discount
if size == "large" and cheese == "yes" and delivery == "yes":
    price -= 2
    print("Big order discount: -$2")

# Print final price
print(f"Your final price is: ${price}")
