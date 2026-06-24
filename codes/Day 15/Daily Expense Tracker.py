'''Task 3: Daily Expense Tracker
Objective

Store daily expenses in a file.

Features
Add Expense
View Expenses
Calculate Total Spending
Example
Food,150
Travel,100
Coffee,50
Expected Output
Total Expense: ₹300
Concepts Used
File Reading
String Processing
Loops'''

while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total Spending")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        category = input("Enter expense category: ")
        amount = input("Enter expense amount: ")
        with open("expenses.txt", "a") as file:
            file.write(f"{category},{amount}\n")
        print("Expense added successfully!")
        
    elif choice == '2':
        try:
            with open("expenses.txt", "r") as file:
                expenses = file.readlines()
                if expenses:
                    print("Your Expenses:")
                    for idx, expense in enumerate(expenses, start=1):
                        category, amount = expense.strip().split(",")
                        print(f"{idx}. {category} - ₹{amount}")
                else:
                    print("No expenses found.")
        except FileNotFoundError:
            print("No expenses found.")
            
    elif choice == '3':
        try:
            with open("expenses.txt", "r") as file:
                expenses = file.readlines()
                if expenses:
                    total_expense = sum(float(expense.strip().split(",")[1]) for expense in expenses)
                    print(f"Total Expense: ₹{total_expense}")
                else:
                    print("No expenses found.")
        except FileNotFoundError:
            print("No expenses found.")
            
    elif choice == '4':
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break   

    