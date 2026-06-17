'''Task 5: Mini Banking System

Concepts Covered:

Functions
Global Variables
Menu Driven Programs'''
# Global variable to store account balance
account_balance = 0.0
def deposit(amount):
    global account_balance
    if amount > 0:
        account_balance += amount
        print(f"Deposited: ${amount:.2f}")
    else:
        print("Deposit amount must be positive.")
def withdraw(amount):
    global account_balance
    if amount > 0:
        if amount <= account_balance:
            account_balance -= amount
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")
    else:
        print("Withdrawal amount must be positive.")
def check_balance():
    print(f"Current Balance: ${account_balance:.2f}")
def main():
    while True:
        print("\nMini Banking System")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            withdraw(amount)
        elif choice == '3':
            check_balance()
        elif choice == '4':
            print("Thank you for using the Mini Banking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()