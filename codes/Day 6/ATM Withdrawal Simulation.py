# ATM Withdrawal Simulation
bal = 5000
amount = int(input("Enter the amount to withdraw: "))
if amount <= bal:
    bal -= amount
    print(f"Withdrawal successful. Remaining balance: {bal}")
elif amount > bal:
    print("Insufficient balance. Withdrawal failed.")
else:
    print("Invalid amount entered.")
    
