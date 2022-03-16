# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
# then tell them whether they guessed too low, too high, or exactly right.

import random
guesses = 0
mystery_number = random.randint(1, 5)

def user_command():
    total = int(input("Guess a number between 1 and 10: "))
    return total

def get_winner(user_cation, computer_action):
    if user_cation == computer_action:
        print("you guessed the number just right")
        print(f"It took you guesses {guesses}")

    elif user_cation < computer_action:
        print("your guess is too low")
    else:
        print("you guessed too high")

while True:
    guesses = guesses + 1
    get_winner(user_command(), mystery_number)
    play_again = input('Would you like to keep playing? ')
    if play_again == 'n':
        break