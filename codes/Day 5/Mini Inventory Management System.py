'''Task 5: Mini Inventory Management System (Challenge)
Objective
Menu:

1. View Products
2. Update Quantity
3. Add Product
4. Exit
Manage products using a dictionary.'''
inventory = {
    "Laptop": 10,
    "Mouse": 25,
    "Keyboard": 15
}
print("Mini Inventory Management System")
while True:
    print("\nMenu:")
    print("1. View Products")
    print("2. Update Quantity")
    print("3. Add Product")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        print("\nProducts in Inventory:")
        for product, quantity in inventory.items():
            print(f"{product}: {quantity}")
    
    elif choice == '2':
        product_name = input("Enter the product name to update quantity: ")
        if product_name in inventory:
            new_quantity = int(input(f"Enter new quantity for {product_name}: "))
            inventory[product_name] = new_quantity
            print(f"Quantity of {product_name} updated to {new_quantity}.")
        else:
            print(f"{product_name} not found in inventory.")
    
    elif choice == '3':
        new_product = input("Enter the name of the new product: ")
        if new_product not in inventory:
            quantity = int(input(f"Enter quantity for {new_product}: "))
            inventory[new_product] = quantity
            print(f"{new_product} added to inventory with quantity {quantity}.")
        else:
            print(f"{new_product} already exists in inventory.")
    
    elif choice == '4':
        print("Exiting Mini Inventory Management System.")
        break
    
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
        