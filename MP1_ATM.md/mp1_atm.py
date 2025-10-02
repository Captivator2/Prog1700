balance = float(input("Enter your current balance: "))
withdrawal = float(input("Enter withdrawal amount: "))

if withdrawal <= 0:
    print("Error: Invalid withdrawal")
elif withdrawal > balance:
    print("Error: Insufficient funds")
else:
    new_balance = balance - withdrawal
    print("New balance:", new_balance)
