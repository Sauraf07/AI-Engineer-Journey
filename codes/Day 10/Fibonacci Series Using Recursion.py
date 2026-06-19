'''Task 2: Fibonacci Series Using Recursion
Objective

Learn recursive branching.

Problem

Print the nth Fibonacci number.'''
def fibonacci(n):
    # Base case: if n is 0, return 0; if n is 1, return 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive case: sum of the two preceding numbers
        return fibonacci(n - 1) + fibonacci(n - 2)
    
# Example usage
number = 7
result = fibonacci(number)
print(f"The {number}th Fibonacci number is: {result}")