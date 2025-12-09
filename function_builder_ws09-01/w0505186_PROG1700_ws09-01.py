# A) Modular Calculator
# Step 1 - Calculator Functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

print("Simple Calculator")

# ask the user for numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# ask for operation
op = input("Enter +, -, *, or / : ")

# choose the correct function
if op == "+":
    result = add(num1, num2)
elif op == "-":
    result = subtract(num1, num2)
elif op == "*":
    result = multiply(num1, num2)
elif op == "/":
    result = divide(num1, num2)
else:
    result = "Invalid operation"

# show the result
print("Result:", result)

# B) Unit Converter
# conversion functions

def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

print("\nUnit Converter")
print("1 - Kilometres to Miles")
print("2 - Miles to Kilometres")
print("3 - Celsius to Fahrenheit")
print("4 - Fahrenheit to Celsius")

choice = input("Choose a conversion (1-4): ")

value = float(input("Enter the value to convert: "))

# decide which conversion to use
if choice == "1":
    result = km_to_miles(value)
elif choice == "2":
    result = miles_to_km(value)
elif choice == "3":
    result = c_to_f(value)
elif choice == "4":
    result = f_to_c(value)
else:
    result = "Invalid choice"

print("Result:", result)

# C) Validation Functions

def is_positive(num):
    return num > 0

def is_integer(value):
    return value.isdigit()

print("\nValidation Check")

user_value = input("Enter a number: ")

# keep asking until the value is a valid integer
while not is_integer(user_value):
    print("Not a valid whole number. Try again.")
    user_value = input("Enter a number: ")

print("You entered a valid integer.")

# convert it to int so we can check positivity
num = int(user_value)

if is_positive(num):
    print("The number is positive.")
else:
    print("The number is zero or negative.")



# Reflection:
# 1. Using functions made my code more organized and easier to read.
# 2. The calculator task felt the most useful because it showed how functions can replace repeated code.
# 3. Modular code helps on bigger projects because each part is separate and easier to fix or update.
# 4. A real-world example is using functions in a budget app to calculate totals or convert money values.
