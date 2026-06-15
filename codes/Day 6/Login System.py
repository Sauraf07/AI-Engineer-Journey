'''onus Challenge (Mini Project)
Login System
Create a simple login system.'''
Username = 'admin'
Password = 1234
input_username = input("Enter username: ")
input_password = int(input("Enter password: "))
if input_username == Username and input_password == Password:
    print("Login successful!")
else:    print("Login failed. Incorrect username or password.")
