# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a
# message of congratulations to the winner, and ask if the players want to start a new game)
#
# Remember the rules:
#
# Rock beats scissors
# Scissors beats paper
# Paper beats rock

import random

while True:
    user = input("Enter a choice (Rock, Paper, Scissors): ")

    action = ['rock', 'paper', 'scissors']
    computer = random.choice(action)

    print(f"you chose: {user}: Computer choice: {computer}")

    if user == computer:
        print(f"Both players selected {user}. Its a tie!")

    elif user == 'rock':
        if computer == "scissors":
            print("rock smashes scissors! you win")
        else:
            print("paper covers rock! you lose")
    elif user == 'paper':
        if computer == "rock":
            print("paper covers rock! you win")
        else:
            print("scissors cut paper! you lose")
    elif user == "scissors":
        if computer == "paper":
            print("scissors cup paper! you win")
        else:
            print("rock smashes scissors! you lose")

    play_again = input("would you like to play again? (y/n): ")
    if play_again != "y":
        break

