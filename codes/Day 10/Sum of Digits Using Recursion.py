'''Task 3: Sum of Digits Using Recursion
Objective

Break a number into smaller subproblems.

Problem

Find the sum of all digits in a number recursively.'''
def sum_of_digits(n):
    # Base case: if n is 0, return 0
    if n == 0:
        return 0
    else:
        # Recursive case: last digit + sum of digits of the remaining number
        return n % 10 + sum_of_digits(n // 10)
    
# Example usage
number = 12345
result = sum_of_digits(number)
print(f"The sum of digits in {number} is: {result}")