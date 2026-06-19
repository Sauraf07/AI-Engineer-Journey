'''Task 5: Number Guessing Game Refactor (Challenge)
Objective

Apply recursion in a real mini-project.

Problem

Create a number guessing game where the function calls itself whenever the guess is incorrect.

Requirements
Generate random number
User enters guess
If wrong:
Tell user Higher/Lower
Call function again
If correct:
Print Success Message'''

import random

def guess_number(target, low, high):
    guess = int(input(f"Guess a number between {low} and {high}: "))
    
    if guess == target:
        print("Congratulations! You guessed the number correctly.")
    elif guess < target:
        print("Higher!")
        guess_number(target, guess + 1, high)
    else:
        print("Lower!")
        guess_number(target, low, guess - 1)

# Generate a random number between 1 and 100
target_number = random.randint(1, 100)
guess_number(target_number, 1, 100)

