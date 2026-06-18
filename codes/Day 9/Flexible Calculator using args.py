'''Task 1: Flexible Calculator using *args
Objective

Create a function that can add any number of values.'''

def add_numbers(*args):
    return sum(args)

print(add_numbers(10, 20))
print(add_numbers(10, 20, 30, 40))