# Task 3: Simple Calculator
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

if operation == "+":
    print("The sum of the two numbers is: " + str(a + b))
elif operation == "-":
    print("The difference of the two numbers is: " + str(a - b))
elif operation == "*":
    print("The product of the two numbers is: " + str(a * b))
elif operation == "/":
    print("The quotient of the two numbers is: " + str(a / b))
else:
    print("Invalid operation. Please enter one of the following: +, -, *, /")