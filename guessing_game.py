# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
# then tell them whether they guessed too low, too high, or exactly right.

import random

guesses = 0
mystery_number = random.randint(1, 5)


def get_user_selection():
    guess = int(input("Guess a number between 1 and 10: "))
    return guess

def get_winner(user_action, computer_action):
    if user_action == computer_action:
        print("you guessed the number just right")
        print(f"It took you guesses {guesses}")
    elif user_action < computer_action:
        print("your guess is too low")
    else:
        print("you guessed too high")


while True:
    guesses = guesses + 1
    get_winner(get_user_selection(), mystery_number)
