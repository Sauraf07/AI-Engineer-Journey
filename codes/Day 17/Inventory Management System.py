'''Task 5: Inventory Management System ⭐⭐⭐ (Recommended)
Objective

Build a real-world inventory management system.

JSON Structure
[
    {
        "id": 101,
        "name": "Laptop",
        "price": 55000,
        "quantity": 5
    }
]
Features
Add Product
View Products
Search Product
Update Stock
Delete Product
Calculate Total Inventory Value
Bonus Features
Low Stock Alert
Search by Product Name
Sort by Price
Export Inventory Report
Skills Covered
JSON Parsing
CRUD Operations
Loops
Functions
Dictionaries
Error Handling
Challenge Task 🚀
Personal Expense Tracker
JSON Structure
[
    {
        "date": "2026-06-27",
        "category": "Food",
        "amount": 250,
        "description": "Lunch"
    }
]
Features
Add Expense
Delete Expense
Update Expense
View All Expenses
Search by Category
Search by Date
Calculate Total Expenses
Calculate Monthly Expenses
Bonus
Show highest expense
Export monthly report
Category-wise summary'''


import json

def add_product(product_id, name, price, quantity):
    product_data = {
        "id": product_id,
        "name": name,
        "price": price,
        "quantity": quantity
    }
    
    try:
        with open('inventory.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    
    data.append(product_data)
    
    with open('inventory.json', 'w') as file:
        json.dump(data, file, indent=4)

def view_all_products():
    try:
        with open('inventory.json', 'r') as file:
            data = json.load(file)
            for product in data:
                print(f"ID: {product['id']}, Name: {product['name']}, Price: {product['price']}, Quantity: {product['quantity']}")
    except FileNotFoundError:
        print("No products found.")

def search_product_by_id(product_id):
    try:
        with open('inventory.json', 'r') as file:
            data = json.load(file)
            for product in data:
                if product['id'] == product_id:
                    print(f"ID: {product['id']}, Name: {product['name']}, Price: {product['price']}, Quantity: {product['quantity']}")
                    return
            print("Product not found.")
    except FileNotFoundError:
        print("No products found.")

def update_stock(product_id, new_quantity):
    try:
        with open('inventory.json', 'r') as file:
            data = json.load(file)
            for product in data:
                if product['id'] == product_id:
                    product['quantity'] = new_quantity
                    break
        with open('inventory.json', 'w') as file:
            json.dump(data, file, indent=4)
    except FileNotFoundError:
        print("No products found.")

def delete_product(product_id):
    try:
        with open('inventory.json', 'r') as file:
            data = json.load(file)
            data = [product for product in data if product['id'] != product_id]
        with open('inventory.json', 'w') as file:
            json.dump(data, file, indent=4)
    except FileNotFoundError:
        print("No products found.")

def calculate_total_inventory_value():
    try:
        with open('inventory.json', 'r') as file:
            data = json.load(file)
            total_value = sum(product['price'] * product['quantity'] for product in data)
            print(f"Total Inventory Value: {total_value}")
    except FileNotFoundError:
        print("No products found.")

def low_stock_alert(threshold):
    try:
        with open('inventory.json', 'r') as file:
            data = json.load(file)
            low_stock_products = [product for product in data if product['quantity'] < threshold]
            if low_stock_products:
                print("Low Stock Products:")
                for product in low_stock_products:
                    print(f"ID: {product['id']}, Name: {product['name']}, Quantity: {product['quantity']}")
            else:
                print("No products below the specified threshold.")
    except FileNotFoundError:
        print("No products found.")

def search_product_by_name(name):
    try:
        with open('inventory.json', 'r') as file:
            data = json.load(file)
            for product in data:
                if product['name'].lower() == name.lower():
                    print(f"ID: {product['id']}, Name: {product['name']}, Price: {product['price']}, Quantity: {product['quantity']}")
                    return
            print("Product not found.")
    except FileNotFoundError:
        print("No products found.")

def sort_products_by_price():
    try:
        with open('inventory.json', 'r') as file:
            data = json.load(file)
            sorted_products = sorted(data, key=lambda x: x['price'])
            print("Products sorted by price:")
            for product in sorted_products:
                print(f"ID: {product['id']}, Name: {product['name']}, Price: {product['price']}, Quantity: {product['quantity']}")
    except FileNotFoundError:
        print("No products found.")

def export_inventory_report():
    try:
        with open('inventory.json', 'r') as file:
            data = json.load(file)
            with open('inventory_report.txt', 'w') as report_file:
                for product in data:
                    report_file.write(f"ID: {product['id']}, Name: {product['name']}, Price: {product['price']}, Quantity: {product['quantity']}\n")
            print("Inventory report exported to inventory_report.txt")
    except FileNotFoundError:
        print("No products found.")

def main():
    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. View All Products")
        print("3. Search Product by ID")
        print("4. Update Stock")
        print("5. Delete Product")
        print("6. Calculate Total Inventory Value")
        print("7. Low Stock Alert")
        print("8. Search Product by Name")
        print("9. Sort Products by Price")
        print("10. Export Inventory Report")
        print("11. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            product_id = int(input("Enter Product ID: "))
            name = input("Enter Product Name: ")
            price = float(input("Enter Product Price: "))
            quantity = int(input("Enter Product Quantity: "))
            add_product(product_id, name, price, quantity)
            print("Product added successfully.")
        elif choice == '2':
            view_all_products()
        elif choice == '3':
            product_id = int(input("Enter Product ID to search: "))
            search_product_by_id(product_id)
        elif choice == '4':
            product_id = int(input("Enter Product ID to update stock: "))
            new_quantity = int(input("Enter new quantity: "))
            update_stock(product_id, new_quantity)
            print("Stock updated successfully.")
        elif choice == '5':
            product_id = int(input("Enter Product ID to delete: "))
            delete_product(product_id)
            print("Product deleted successfully.")
        elif choice == '6':
            calculate_total_inventory_value()
        elif choice == '7':
            threshold = int(input("Enter low stock threshold: "))
            low_stock_alert(threshold)
        elif choice == '8':
            name = input("Enter Product Name to search: ")
            search_product_by_name(name)
        elif choice == '9':
            sort_products_by_price()
        elif choice == '10':
            export_inventory_report()
        elif choice == '11':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    