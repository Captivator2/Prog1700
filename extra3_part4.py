# ATM Simulator

# Start with a fixed balance
balance = 500

# Allow up to 2 attempts for PIN
attempts = 0
pin_correct = False

while attempts < 2:
    pin = input("Enter PIN: ")
    if pin == "4321":
        pin_correct = True
        break
    else:
        print("Wrong PIN")
        attempts += 1

if pin_correct:
    option = input("Choose (balance/withdraw/deposit): ")

    if option == "balance":
        print("Your balance is $", balance)

    elif option == "withdraw":
        amount = int(input("Enter amount: "))
        if amount <= balance:
            balance -= amount
            print("Withdrawal successful. New balance: $", balance)
        else:
            print("Insufficient funds")

    elif option == "deposit":
        amount = int(input("Enter deposit amount: "))
        balance += amount
        print("Deposit successful. New balance: $", balance)

    else:
        print("Invalid option")
else:
    print("Account locked. Too many wrong attempts.")
