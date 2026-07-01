def load_expenses():
    try:
        with open("expenses.txt", "r") as file:
            expenses = file.readlines()
            return [line.strip().split(',') for line in expenses]
    except FileNotFoundError:
        return []
    
def save_expenses(expenses):
    with open("expenses.txt", "w") as file:
        for expense in expenses:
            file.write(','.join(expense) + '\n')

def add_expense():
    try:
        date = input("Enter the date (YYYY-MM-DD): ")
        category = input("Enter the category: ")
        amount = float(input("Enter the amount: "))
        description = input("Enter a description: ")
    except ValueError:
        print("Invalid input. Please enter a valid amount.")
        return

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }

    expenses = load_expenses()
    expenses.append([expense['date'], expense['category'], str(expense['amount']), expense['description']])
    save_expenses(expenses)
    print("Expense added successfully!")

def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.")
        return
    for line in expenses:
        date, category, amount, description = line
        print(f"Date: {date}, Category: {category}, Amount: {amount}, Description: {description}")


def delete_expense():
    view_expenses()
    expense_to_delete = input("Enter the date of the expense to delete (YYYY-MM-DD): ")
    expenses = load_expenses()
    expenses = [expense for expense in expenses if not expense[0].startswith(expense_to_delete)]
    save_expenses(expenses)
    print("Expense deleted successfully!")

def search_expense():
    search_term = input("Enter the category or description to search: ")
    expenses = load_expenses()
    found_expenses = [expense for expense in expenses if search_term.lower() in expense[1].lower() or search_term.lower() in expense[3].lower()]
    if not found_expenses:
        print("No matching expenses found.")
        return
    for line in found_expenses:
        date, category, amount, description = line
        print(f"Date: {date}, Category: {category}, Amount: {amount}, Description: {description}")

def view_monthly_summary():
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.")
        return

    monthly_summary = {}
    for line in expenses:
        date, category, amount, description = line
        month = date[:7]  # Extract YYYY-MM
        if month not in monthly_summary:
            monthly_summary[month] = 0
        monthly_summary[month] += float(amount)

    for month, total in monthly_summary.items():
        print(f"Month: {month}, Total Expenses: {total}")

def main():
    while True:
        print("1 to add expense")
        print("2 to view expenses")
        print("3 to delete expense")
        print("4 to search expense")
        print("5 to view monthly summary")
        print("6 to exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            delete_expense()
        elif choice == '4':
            search_expense()
        elif choice == '5':
            view_monthly_summary()
        elif choice == '6':
            print("Exiting the program.")
            break

main()