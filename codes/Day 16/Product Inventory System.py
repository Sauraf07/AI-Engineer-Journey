'''Task 4: Product Inventory System
Objective

Manage product information using a CSV file.

CSV Structure
ProductID,Name,Price,Stock
1,Laptop,55000,10
2,Mouse,500,50
Features
Add Product
Update Stock
Delete Product
Search Product
Calculate Inventory Value
Formula
Inventory Value = Price × Stock
Bonus

Display products with stock below 5.'''

import csv
def add_product():
    product_id = input("Enter Product ID: ")
    name = input("Enter Product Name: ")
    price = float(input("Enter Price: "))
    stock = int(input("Enter Stock Quantity: "))
    
    with open('products.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([product_id, name, price, stock])
    
    print(f"Product {name} added successfully!")

def update_stock(product_id):
    with open('products.csv', 'r') as file:
        reader = list(csv.reader(file))
    
    for i, row in enumerate(reader):
        if row[0] == product_id:
            print(f"Current Stock: {row[3]}")
            new_stock = int(input("Enter new stock quantity: "))
            row[3] = new_stock
            reader[i] = row
            break
    else:
        print("Product not found.")
        return
    
    with open('products.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(reader)
    
    print(f"Stock for Product {product_id} updated successfully!")

def delete_product(product_id):
    with open('products.csv', 'r') as file:
        reader = list(csv.reader(file))
    
    for i, row in enumerate(reader):
        if row[0] == product_id:
            del reader[i]
            break
    else:
        print("Product not found.")
        return
    
    with open('products.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(reader)
    
    print(f"Product {product_id} deleted successfully!")

def search_product(product_id):
    with open('products.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == product_id:
                print(f"Product Found: {row}")
                return
    print("Product not found.")

def calculate_inventory_value():
    total_value = 0
    with open('products.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            price = float(row[2])
            stock = int(row[3])
            total_value += price * stock
    print(f"Total Inventory Value: {total_value}")

def display_low_stock_products():
    with open('products.csv', 'r') as file:
        reader = csv.reader(file)
        low_stock_products = [row for row in reader if int(row[3]) < 5]
    
    if low_stock_products:
        print("Products with stock below 5:")
        for product in low_stock_products:
            print(product)
    else:
        print("No products with stock below 5.")

def view_all_products():
    with open('products.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
def main():
    while True:
        print("\nProduct Inventory System")
        print("1. Add Product")
        print("2. Update Stock")
        print("3. Delete Product")
        print("4. Search Product")
        print("5. Calculate Inventory Value")
        print("6. Display Low Stock Products")
        print("7. View All Products")
        print("8. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_product()
        elif choice == '2':
            product_id = input("Enter Product ID to update stock: ")
            update_stock(product_id)
        elif choice == '3':
            product_id = input("Enter Product ID to delete: ")
            delete_product(product_id)
        elif choice == '4':
            product_id = input("Enter Product ID to search: ")
            search_product(product_id)
        elif choice == '5':
            calculate_inventory_value()
        elif choice == '6':
            display_low_stock_products()
        elif choice == '7':
            view_all_products()
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    