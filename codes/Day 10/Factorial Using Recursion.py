'''Task 1: Factorial Using Recursion
Objective

Understand how a function calls itself until it reaches a base case.

Problem

Create a function that calculates the factorial of a number.'''
def factorial(n):
    # Base case: if n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n * factorial of (n-1)
        return n * factorial(n - 1)
    
# Example usage
number = 5
result = factorial(number)
print(f"The factorial of {number} is: {result}")
