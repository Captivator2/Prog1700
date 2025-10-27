#step 1
import random

secret = random.randint(1, 10)
guess = 0
tries = 0

while guess != secret and tries < 5:
    guess = int(input("Guess a number (1–10): "))
    tries += 1
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("You got it!")

if guess != secret:
    print("You're out of tries!")

    #step 2
import random

heads = 0
tails = 0
count = 0

flips1 = input("How many times do you want to flip the coin? ")
while count < int(flips1):
    flip = random.choice(["Heads", "Tails"])
    print(flip)
    if flip == "Heads":
        heads += 1
    else:
        tails += 1
    count += 1

print("Heads:", heads)
print("Tails:", tails)

#step 3
import time

count = input("Enter the number to start counting down from: ")

while int(count) >= 0:
    print(count)
    time.sleep(1)  # Wait 1 second
    count = str(int(count) - 1)

print("Blast off! 🚀")

#step 4
rows = input("How many rows do you want in the pattern? ")

current = 1
while current <= int(rows):
    print("*" * current)
    current = current + 1

# Reflection:
# 1. I found the Number Guesser the most fun because it was like a game.
# 2. A common mistake that caused infinite loops was forgetting to change the counter or stop condition.
# 3. While loops could be used in a real app to repeat asking the user for input until it is correct.
# 4. The Pattern Generator helped me understand loop conditions best because I could see the  number go down each time.
