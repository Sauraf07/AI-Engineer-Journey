'''Task 3: Online Payment Gateway
Objective

Practice Abstraction

Requirements

Create abstract class:

Payment

Methods:

pay()
generate_receipt()

Implement:

UPIPayment
CreditCardPayment
PayPalPayment
Example
upi.pay()
card.pay()
paypal.pay()
Learning Outcome
Abstract Classes
Abstract Methods
Real Industry Pattern
'''

class Payment:
    def pay(self, amount):
        raise NotImplementedError("Subclasses must implement this method")

    def generate_receipt(self):
        raise NotImplementedError("Subclasses must implement this method")
    
class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Processing UPI payment of {amount}...")
        # Logic for UPI payment processing

    def generate_receipt(self):
        print("Generating UPI payment receipt...")
        # Logic for generating UPI receipt

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Processing credit card payment of {amount}...")
        # Logic for credit card payment processing

    def generate_receipt(self):
        print("Generating credit card payment receipt...")
        # Logic for generating credit card receipt

class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Processing PayPal payment of {amount}...")
        # Logic for PayPal payment processing

    def generate_receipt(self):
        print("Generating PayPal payment receipt...")
        # Logic for generating PayPal receipt

# Example usage
if __name__ == "__main__":
    upi = UPIPayment()
    upi.pay(1000)
    upi.generate_receipt()

    card = CreditCardPayment()
    card.pay(2000)
    card.generate_receipt()

    paypal = PayPalPayment()
    paypal.pay(1500)
    paypal.generate_receipt()
    