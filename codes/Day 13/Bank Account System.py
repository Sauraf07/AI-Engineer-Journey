'''Task 2: Bank Account System
Requirements

Create a BankAccount class.

Attributes
account_number
account_holder
balance
Methods
deposit(amount)
withdraw(amount)
display_balance()
Conditions
Prevent withdrawal if balance is insufficient.'''
class BankAccount:
    def __init__(self,account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance for withdrawal.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew: ${amount}")

    def display_balance(self):
        print(f"Current Balance: ${self.balance}")
# Example usage
account1 = BankAccount("123456789", "John Doe", 1000)
account1.display_balance()
account1.deposit(500)
account1.withdraw(200)
account1.display_balance()