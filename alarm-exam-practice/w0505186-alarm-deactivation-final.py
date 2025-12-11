# Alarm Deactivation Program

# start state from flowchart
alarm_status = "OFF"
alarm_activated_status = "ON"
password_attempts = 3  # user gets 3 tries

print("Alarm status:", alarm_status)
print("Alarm activated:", alarm_activated_status)
print("Password attempts left:", password_attempts)

# Step: Read passwords from passwords.txt
with open("passwords.txt", "r") as file:
    valid_codes = [line.strip() for line in file]

print("Loaded valid codes:", valid_codes)


# Main 3-attempt loop
while password_attempts > 0:

    user_input = input("Enter your 5-digit password: ")

    if len(user_input) != 5 or not user_input.isdigit():
        print("Invalid Password")
        password_attempts -= 1
        print("Password attempts left:", password_attempts)
        continue

    print("Valid number entered.")

    if user_input in valid_codes:
        print("SYSTEM DEACTIVATED")
        break
    else:
        print("Incorrect Password")
        password_attempts -= 1
        print("Password attempts left:", password_attempts)
        continue
# If the loop ends because attempts reached 0, trigger alarm
if password_attempts == 0:
    print("ALARM TRIGGERED")

# Now user must enter valid password to stop alarm
    while True:
        user_input = input("Enter password to disable alarm: ")

        if len(user_input) != 5 or not user_input.isdigit():
            print("Invalid Password")
            continue

        if user_input in valid_codes:
            print("ALARM DISABLED")
            alarm_activated_status = "OFF"
            break
        else:
            print("Incorrect Password – Alarm still active!")
    