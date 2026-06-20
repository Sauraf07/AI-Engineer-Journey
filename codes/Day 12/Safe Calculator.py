'''Task 1: Safe Calculator
Requirements

Create a calculator that:

Takes two numbers from the user
Takes an operator (+, -, *, /)
Handles:
Invalid numbers
Division by zero
Invalid operators'''
def safe_calculator():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operator = input("Enter an operator (+, -, *, /): ")

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Cannot divide by zero.")
                result = num1 / num2
            else:
                raise ValueError("Invalid operator. Please use +, -, *, or /.")

            print(f"The result is: {result}")
            break

        except ValueError as ve:
            print(f"Value error: {ve}. Please try again.")
        except ZeroDivisionError as zde:
            print(f"Zero division error: {zde}. Please try again.")
if __name__ == "__main__":    
    safe_calculator()
