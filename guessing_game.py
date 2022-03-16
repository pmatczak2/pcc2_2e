# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
# then tell them whether they guessed too low, too high, or exactly right.

import random
guesses = 0
mystery_number = random.randint(1, 5)


while True:
    guesses = guesses + 1
    guess = int(input("Guess a number between 1 and 10: "))

    if guess == mystery_number:
        print("you guessed the number just right")
        print(f"It took you guesses {guesses}")
        play_again = input('Would you like to keep playing? ')
        if play_again == 'n':
            break
    elif guess < mystery_number:
        print("your guess is too low")
    else:
        print("you guessed too high")

