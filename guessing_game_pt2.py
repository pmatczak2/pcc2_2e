# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
# then tell them whether they guessed too low, too high, or exactly right.

import random


def user_command():
    total = int(input("Guess a number between 1 and 5: "))
    return total

def get_winner(user_acation, computer_action):
    if user_acation == computer_action:
        print("you guessed the number just right")
        print(f"It took you guesses {guesses}")
        return True
    elif user_acation < computer_action:
        print("your guess is too low")
    else:
        print("you guessed too high")
    return False

while True:
    guesses = 0
    mystery_number = random.randint(1, 5)
    while True:
        guesses = guesses + 1
        did_i_win = get_winner(user_command(), mystery_number)
        if did_i_win:
            break


    play_again = input('Would you like to keep playing? ')
    if play_again == 'n':
        break