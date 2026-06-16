'''Task 3: ATM Simulation
Objective

Practice infinite loops and menu systems.'''
balance = 1000
while True:
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        print(f"Your current balance is: ${balance}")
    elif choice == '2':
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print(f"${amount} deposited. New balance: ${balance}")
    elif choice == '3':
        amount = float(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient funds.")
        else:
            balance -= amount
            print(f"${amount} withdrawn. New balance: ${balance}")
    elif choice == '4':
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")