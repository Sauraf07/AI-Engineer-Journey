'''Task 3: ATM Withdrawal Simulator
Requirements

Balance = ₹5000

Ask user for withdrawal amount.

Handle:

Invalid input
Negative amount
Amount greater than balance'''

class InvalidWithdrawalError(Exception):
    pass

def atm_withdrawal():
    balance = 5000
    while True:
        try:
            amount = float(input("Enter the withdrawal amount: "))
            if amount < 0:
                raise InvalidWithdrawalError("Withdrawal amount cannot be negative.")
            if amount > balance:
                raise InvalidWithdrawalError("Withdrawal amount exceeds available balance.")
            balance -= amount
            print(f"Withdrawal successful. Remaining balance: ₹{balance}")
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except InvalidWithdrawalError as iwe:
            print(f"Invalid withdrawal error: {iwe}. Please try again.")

if __name__ == "__main__":
    atm_withdrawal()