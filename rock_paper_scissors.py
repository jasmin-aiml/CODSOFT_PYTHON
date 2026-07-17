# Task 4: Rock Paper Scissors Game
import random

options_list = ["rock", "paper", "scissors"]

print("Welcome to Rock, Paper, Scissors against the Computer!")

while True:
    my_turn = input("\nType your choice (rock/paper/scissors) or 'quit': ").lower().strip()

    if my_turn == "quit":
        print("Thanks for playing my game! Goodbye.")
        break

    if my_turn not in options_list:
        print("That choice doesn't exist. Please check your spelling.")
        continue

    comp_turn = random.choice(options_list)
    print("Computer picked:", comp_turn)

    # game rules check
    if my_turn == comp_turn:
        print("It's a draw! Try again.")
    elif my_turn == "rock":
        if comp_turn == "scissors":
            print("Wow, you win! Rock breaks scissors.")
        else:
            print("You lose! Paper covers rock.")
    elif my_turn == "paper":
        if comp_turn == "rock":
            print("Wow, you win! Paper covers rock.")
        else:
            print("You lose! Scissors cuts paper.")
    elif my_turn == "scissors":
        if comp_turn == "paper":
            print("Wow, you win! Scissors cuts paper.")
        else:
            print("You lose! Rock breaks scissors.")

      
