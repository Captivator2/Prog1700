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

# Main 3-attempt loop
while password_attempts > 0:

    user_input = input("Enter your 5-digit password: ")

# Ask the user to enter a 5-digit password
user_input = input("Enter your 5-digit password: ")

# Check if the password is exactly 5 characters AND all digits
if len(user_input) != 5 or not user_input.isdigit():
    print("Invalid Password")
    password_attempts -= 1   
    print("Password attempts left:", password_attempts)
    # later we will loop back depending on attempts
else:
    print("Valid number entered.")


