# Task 4: Password Strength Checker
password = input("Enter a password to check its strength: ")
length = len(password)
if length == 0:
    print("Password cannot be empty. Please enter a valid password.")
elif length < 6:
    print("Password is too short. It should be at least 6 characters long.")
elif length < 12:
    print("Password is of medium strength. Consider adding more characters for better security.")
else:
    print("Password is strong. Good job!")