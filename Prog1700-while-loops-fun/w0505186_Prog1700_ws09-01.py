#step 1
count = 10
while count >= 1:
    print("Launching in... 10", count, "🚀")
    count -= 1

print("Liftoff!")

#step 2
import random

play_again = "y"

while play_again == "y":
    secret = random.randint(1, 10)
    guess = 0
    tries = 0
    score = 10

    while guess != secret and tries < 5:
        guess = int(input("Guess a number between 1 and 10: "))
        tries += 1
        if guess < secret:
            print("Too low! 📉")
        elif guess > secret:
            print("Too high! 📈")
        else:
            print("You got it! 🎉")
            print("Your score:", score - tries)
            break

    if guess != secret:
        print("Game Over 😢 The number was", secret)

    play_again = input("Play again? (y/n): ")

print("Thanks for playing!")

#step 3
sips = 5
while sips > 0:
    print("You take a sip... ")
    if random.choice([True, False]):
        print("You found a boba pearl! ")
    else:
        print("Smooth and sweet ")
    sips -= 1
print("Cup empty. Refill time!")


# Reflection:
# 1. My first infinite loop was when I forgot to change the counter.
# 2. I fixed it by adding count -= 1 inside the loop.
# 3. I liked the guessing game most because it was fun to play.
# 4. While loops can make games repeat until you win or lose.