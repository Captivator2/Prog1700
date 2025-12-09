# A) Modular Calculator

# Calculator functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "error"
    return a / b


# Counters for the final session summary
calculation_count = 0

# Calculator loop
while True:
    print("\nCalculator Menu")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("5 - View Log")
    print("Type 'exit' to stop.")

    choice = input("Choose: ").lower().strip()

    if choice == "exit":
        break

    # Show calculation log
    if choice == "5":
        try:
            with open("calc_log.txt", "r") as f:
                print("\n--- Calculation Log ---")
                print(f.read())
        except FileNotFoundError:
            print("No log file yet.")
        continue

    # Validate choice
    if choice not in {"1", "2", "3", "4"}:
        print("Invalid option.")
        continue

    # Get numbers
    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
    except ValueError:
        print("Numbers only.")
        continue

    # Perform operation
    if choice == "1":
        result = add(x, y)
        op_symbol = "+"
    elif choice == "2":
        result = subtract(x, y)
        op_symbol = "-"
    elif choice == "3":
        result = multiply(x, y)
        op_symbol = "*"
    else:
        result = divide(x, y)
        op_symbol = "/"

    print("Result:", result)

    # Log to file
    with open("calc_log.txt", "a") as file:
        file.write(f"{x} {op_symbol} {y} = {result}\n")

    calculation_count += 1

# B) Unit Converter (CSV)

import csv

# Converter functions
def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

def km_to_mi(km):
    return km * 0.621371

def mi_to_km(mi):
    return mi / 0.621371


conversion_count = 0  # for session summary

while True:
    print("\nUnit Converter Menu")
    print("1 - Celsius → Fahrenheit")
    print("2 - Fahrenheit → Celsius")
    print("3 - KM → Miles")
    print("4 - Miles → KM")
    print("5 - View Previous Conversions")
    print("Type 'exit' to stop.")

    choice = input("Choose: ").lower().strip()

    if choice == "exit":
        break

    # Read past conversions
    if choice == "5":
        try:
            with open("conversions.csv", "r") as file:
                print("\n--- Conversion History ---")
                print(file.read())
        except FileNotFoundError:
            print("No conversion file yet.")
        continue

    if choice not in {"1", "2", "3", "4"}:
        print("Invalid option.")
        continue

    # Get input number
    try:
        value = float(input("Enter value: "))
    except ValueError:
        print("Numbers only.")
        continue

    # Perform conversion
    if choice == "1":
        result = c_to_f(value)
        ctype = "C_to_F"
    elif choice == "2":
        result = f_to_c(value)
        ctype = "F_to_C"
    elif choice == "3":
        result = km_to_mi(value)
        ctype = "KM_to_MI"
    else:
        result = mi_to_km(value)
        ctype = "MI_to_KM"

    print("Result:", round(result, 2))

    # Save to CSV
    with open("conversions.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([ctype, value, round(result, 2)])

    conversion_count += 1

# C) Validation Functions
# -----------------------------

# Checks if value is a positive number
def is_positive(num):
    return num > 0

# Checks if input is an integer (only digits)
def is_integer(value):
    return value.isdigit()


# Main validation loop
while True:
    print("\nValidation Menu")
    print("1 - Check Positive Number")
    print("2 - Check Integer")
    print("Type 'exit' to stop.")

    choice = input("Choose: ").lower().strip()

    if choice == "exit":
        break

    if choice == "1":
        # positive number check
        try:
            number = float(input("Enter a number: "))
            if is_positive(number):
                print("This is a positive number.")
            else:
                print("This is NOT positive.")
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "2":
        # integer check
        value = input("Enter something: ")
        if is_integer(value):
            print("This is an integer.")
        else:
            print("This is NOT an integer.")

    else:
        print("Invalid option.")


# Reflection:
# 1. Using functions made my code more organized because each job was in its own place.
# 2. The calculator task was the most useful because it showed how functions can be reused.
# 3. Modular code helps on bigger projects because it keeps everything cleaner and easier to fix.
# 4. A real-world example would be using functions in a small app that converts money or units.
