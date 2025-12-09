import random
import time

# Data setup
valid_moves = ["rock", "paper", "scissors"]   
valid_set = {"rock", "paper", "scissors"}    
score = {"player": 0, "cpu": 0, "ties": 0}   
history = []                                 

# Functions
def get_player_move(valid_set):
    move = ""
    while move not in valid_set:
        move = input("Enter your move (rock, paper, scissors): ").lower()
        #Accessibility tweak
        if move == "r":
            move = "rock"
        elif move == "p":
            move = "paper"
        elif move == "s":
            move = "scissors"
    return move

def get_cpu_move(valid_moves):
    return random.choice(valid_moves)

def decide_winner(player, cpu):
    if player == cpu:
        return "tie"
    elif (player == "rock" and cpu == "scissors") or \
         (player == "scissors" and cpu == "paper") or \
         (player == "paper" and cpu == "rock"):
        return "player"
    else:
        return "cpu"

def print_scoreboard(score):
    print("Scoreboard:")
    print("Player:", score["player"])
    print("CPU:", score["cpu"])
    print("Ties:", score["ties"])

def print_history(history):
    for round in history:
        print(f"Round {round['round']}: Player-{round['player']} CPU-{round['cpu']} Result-{round['result']}")

# Main Game loop
while True:
    print("\nWelcome to Rock-Paper-Scissors!")
    
    # Ask how many rounds to play (best-of-N, must be odd)
    try:
        best_of = int(input("Play best of (3, 5, 7): "))
        if best_of % 2 == 0:
            print("Please enter an odd number.")
            continue
    except ValueError:
        print("Please enter a valid number.")
        continue

    # Reset scores and history for each new game
    score = {"player": 0, "cpu": 0, "ties": 0}
    history = []

    round_num = 1
    while score["player"] < (best_of // 2 + 1) and score["cpu"] < (best_of // 2 + 1):
        print(f"\nRound {round_num}")
        player_move = get_player_move(valid_set)
        cpu_move = get_cpu_move(valid_moves)
        print("CPU chose:", cpu_move)
        time.sleep(0.3)
        result = decide_winner(player_move, cpu_move)

        if result == "player":
            score["player"] += 1
            print("You win this round!")
        elif result == "cpu":
            score["cpu"] += 1
            print("CPU wins this round!")
        else:
            score["ties"] += 1
            print("It's a tie!")

        history.append({
            "round": round_num,
            "player": player_move,
            "cpu": cpu_move,
            "result": result
        })

        round_num += 1

    # Print final scoreboard and round history
    print("\nGame Over!")
    print_scoreboard(score)
    print("\nRound History:")
    print_history(history)

    # Ask if player wants to play again
    again = input("\nPlay again? (y/n): ").lower()
    if again != "y":
        print("Thanks for playing!")
        break

# Reflection:
# 1) The decide winner function helped the most because it made the code easy to follow.
# 2) I fixed a problem where wrong inputs didn’t work by adding a loop to ask again.
# 3) Lists were good for moves, sets for checking, and dicts for the score.
# 4) I would add more moves like lizard and spoc
