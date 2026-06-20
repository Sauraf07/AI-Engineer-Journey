'''Task 5: Login System with Custom Exception
Requirements

Create:

username = "admin"
password = "1234"'''

class InvalidCredentialsError(Exception):
    pass
def login_system():
    username = "admin"
    password = "1234"
    while True:
        try:
            input_username = input("Enter username: ")
            input_password = input("Enter password: ")
            if input_username != username or input_password != password:
                raise InvalidCredentialsError("Invalid username or password.")
            print("Login successful!")
            break
        except InvalidCredentialsError as ice:
            print(f"Login error: {ice}. Please try again.")

if __name__ == "__main__":
    login_system()