'''Task 3: Even or Odd Checker

Concepts Covered:

Functions
Modulus Operator'''
def is_even(number):
    return number % 2 == 0

def is_odd(number):
    return number % 2 != 0

# Example usage:
num = 7
if is_even(num):
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")
num = 10
if is_even(num):
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")
    