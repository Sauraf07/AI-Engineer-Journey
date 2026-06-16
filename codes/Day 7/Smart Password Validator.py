# Smart Password Validator
'''Task 2: Smart Password Validator
Objective
Practice loops and conditions.
Requirements
User enters password repeatedly until valid.
Rules:
Minimum 8 characters
At least 1 uppercase
At least 1 lowercase
At least 1 digit'''
password = input("Enter a password: ")
while True:
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
    elif not any(char.isupper() for char in password):
        print("Password must contain at least one uppercase letter.")
    elif not any(char.islower() for char in password):
        print("Password must contain at least one lowercase letter.")
    elif not any(char.isdigit() for char in password):
        print("Password must contain at least one digit.")
    else:
        print("Password is valid!")
        break
    password = input("Enter a password: ")
    