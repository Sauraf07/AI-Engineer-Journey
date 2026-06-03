# Task 1
'''try:
    with open("data.txt", "r") as file:
        data = file.read()
        print(data)
except FileNotFoundError:   
    print("The file 'data.txt' was not found.")
except Exception as e:  
    print(f"An error occurred: {e}")
    '''
# ==============================================
# Task 2

'''note = input("Enter a note: ")
try:
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("Note saved successfully!")
except Exception as e:
    print(f"An error occurred: {e}")'''
# ==============================================
# Task 3
'''note = input("Enter a note: ")
try:
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("Note saved successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
        '''
# =============================================
# Task 4
'''note = input("Enter a note: ")
try:
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("Note saved successfully!")
except Exception as e:
    print(f"An error occurred: {e}")'''

#   =============================================
# Task 5
'''try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    op = input("Enter the operation (+, -, *, /): ")
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
            result = None
    else:
        print("Invalid operation.")
        result = None
except ValueError:
    print("Invalid input. Please enter numeric values.")
    result = None
except Exception as e:
    print(f"An error occurred: {e}")
    result = None
if result is not None:
    print(f"The result is: {result}")'''

# =============================================
# Task 6
'''file = input("Enter the filename to read: ")
try:
    with open(file, "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("The file was not found.")
except Exception as e:
    print(f"An error occurred: {e}")'''

# ============================================

