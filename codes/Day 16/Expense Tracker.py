'''Task 3: Expense Tracker
Objective

Maintain daily expenses using a CSV file.

CSV Structure
Date,Category,Amount
2026-06-20,Food,250
2026-06-20,Travel,150
Features
Add Expense
View All Expenses
Search by Date
Search by Category
Calculate Daily Total
Calculate Monthly Total
Bonus

Display the category with the highest spending.'''

import csv
def add_expense():  
    date = input("Enter Date (YYYY-MM-DD): ")
    category = input("Enter Category: ")
    amount = float(input("Enter Amount: "))
    
    with open('expenses.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])
    
    print(f"Expense added successfully!")

def view_all_expenses():
    with open('expenses.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def search_by_date(date):
    with open('expenses.csv', 'r') as file:
        reader = csv.reader(file)
        found = False
        for row in reader:
            if row[0] == date:
                print(row)
                found = True
        if not found:
            print("No expenses found for this date.")

def search_by_category(category):
    with open('expenses.csv', 'r') as file:
        reader = csv.reader(file)
        found = False
        for row in reader:
            if row[1].lower() == category.lower():
                print(row)
                found = True
        if not found:
            print("No expenses found for this category.")
        
def calculate_daily_total(date):
    total = 0
    with open('expenses.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == date:
                total += float(row[2])
    print(f"Total expenses for {date}: {total}")

def calculate_monthly_total(month):
    total = 0
    with open('expenses.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0].startswith(month):
                total += float(row[2])
    print(f"Total expenses for {month}: {total}")

def highest_spending_category():
    category_totals = {}
    with open('expenses.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            category = row[1]
            amount = float(row[2])
            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount
    
    if category_totals:
        highest_category = max(category_totals, key=category_totals.get)
        print(f"Category with the highest spending: {highest_category} with total {category_totals[highest_category]}")
    else:
        print("No expenses recorded.")

def main():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Search by Date")
        print("4. Search by Category")
        print("5. Calculate Daily Total")
        print("6. Calculate Monthly Total")
        print("7. Highest Spending Category")
        print("8. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_all_expenses()
        elif choice == '3':
            date = input("Enter Date (YYYY-MM-DD): ")
            search_by_date(date)
        elif choice == '4':
            category = input("Enter Category: ")
            search_by_category(category)
        elif choice == '5':
            date = input("Enter Date (YYYY-MM-DD): ")
            calculate_daily_total(date)
        elif choice == '6':
            month = input("Enter Month (YYYY-MM): ")
            calculate_monthly_total(month)
        elif choice == '7':
            highest_spending_category()
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()