'''Task 5: Advanced Number Guessing Game
Objective

Master everything from Day 7.

Requirements

Computer generates random number between 1–100.

User keeps guessing.'''
import random
number_to_guess = random.randint(1, 100)
while True:
    user_guess = int(input("Guess the number between 1 and 100: "))
    if user_guess < number_to_guess:
        print("Too low! Try again.")
    elif user_guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the number!")
        break
    