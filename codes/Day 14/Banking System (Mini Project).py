'''Task 5: Banking System (Mini Project)
Objective

Industry-Level OOP Practice

Requirements

Create:

Account
│
├── SavingsAccount
└── CurrentAccount
Features
deposit()
withdraw()
check_balance()
Rules

Savings Account:

Minimum Balance = 1000

Current Account:

No Minimum Balance'''

class Account:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        raise NotImplementedError("Subclasses must implement this method")

    def check_balance(self):
        return self.balance
    
class SavingsAccount(Account):
    MIN_BALANCE = 1000

    def withdraw(self, amount):
        if amount > 0 and (self.balance - amount) >= self.MIN_BALANCE:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print(f"Cannot withdraw {amount}. Minimum balance of {self.MIN_BALANCE} must be maintained.")

class CurrentAccount(Account):
    def withdraw(self, amount):
        if amount > 0 and (self.balance - amount) >= 0:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print(f"Cannot withdraw {amount}. Insufficient funds.")

# Example usage
if __name__ == "__main__":
    savings = SavingsAccount("SA123", "Alice")
    current = CurrentAccount("CA456", "Bob")

    savings.deposit(2000)
    savings.withdraw(500)
    print(f"Savings Account Balance: {savings.check_balance()}")

    current.deposit(1500)
    current.withdraw(1600)  # Should fail due to insufficient funds
    print(f"Current Account Balance: {current.check_balance()}")
    