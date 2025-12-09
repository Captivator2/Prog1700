# -----------------------------
# Function Definitions
# -----------------------------

# Adds two numbers and returns the result
def add(a, b): 
    return a + b

# Subtracts the second number from the first and returns the result
def subtract(a, b): 
    return a - b

# Multiplies two numbers and returns the result
def multiply(a, b): 
    return a * b

# Divides the first number by the second
# Includes a check to prevent division by zero
def divide(a, b): 
    if b == 0:
        return "Cannot divide by Zero"  # Return a message instead of crashing
    else:
        return a / b

# -----------------------------
# Main Program Loop
# -----------------------------

# This loop will keep running until the user types 'exit'
while True:
    # Display the calculator menu
    print("\nWelcome to our Calculator")
    print("Enter the operation:")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("Type 'exit' to end calculator.")
    
    # Get the user's choice of operation
    operation = input().strip().lower()  \
        # .strip() removes extra spaces, .lower() allows case-insensitive 'exit'

    # Check if the user wants to exit
    if operation == "exit":
        print("Goodbye!")  # Friendly exit message
        break  # Exit the loop and end the program

    # Validate the operation input
    if operation not in {"1", "2", "3", "4"}:
        print("Invalid operation. Please choose 1-4 or type 'exit'.")
        continue  # Skip the rest of the loop and ask again

    # Try to get two valid numbers from the user
    try:
        num1 = float(input("Enter number 1: "))  # Convert input to float
        num2 = float(input("Enter number 2: "))  # Convert input to float
    except ValueError:
        # If conversion fails, inform the user and restart the loop
        print("Invalid input. Please enter numeric values.")
        continue

    # Perform the selected operation
    if operation == "1":
        result = add(num1, num2)
    elif operation == "2":
        result = subtract(num1, num2)
    elif operation == "3":
        result = multiply(num1, num2)
    elif operation == "4":
        result = divide(num1, num2)

    # Display the result of the calculation
    print("Result:", result)