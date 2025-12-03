# Final Project - Python Game
# Written by Jennifer
# December 3, 2025

# This is code to generate a random number between 1 to 100 for the player to guess

import random

number = random.randint(1, 100)
# Create counter for the number of guesses made by user
attempts = 0

while True:
    guess = input("Guess a number between 1 and 100: ")
    # Confirm user input is a number
    if not guess.isdigit():
        print("Please enter a number between 1 and 100")
        continue
    guess=int(guess)
    # Increase attempt counter with each guess
    attempts += 1

    # Evaluate guess to see if the user got the randomly selected number.
    if guess<number:
        print("Guess is too low, please try again")
    elif guess>number:
        print("Guess is too high, please try again")
    else:
        print('You are correct! You guessed the number in', attempts, 'attempts.')
        break