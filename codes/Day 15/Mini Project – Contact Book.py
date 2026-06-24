'''Task 5: Mini Project – Contact Book
Objective

Create a simple contact management system.

Features
1. Add Contact
2. Search Contact
3. View Contacts
4. Delete Contact
5. Exit
Example Storage
Aman,9876543210
Priya,9988776655
Rahul,8899776655
Concepts Used
File Handling
Loops
Functions
Search Algorithms'''

while True:
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. View Contacts")
    print("4. Delete Contact")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        with open("contacts.txt", "a") as file:
            file.write(f"{name},{phone}\n")
        print("Contact added successfully!")
        
    elif choice == '2':
        search_name = input("Enter the name to search: ")
        try:
            with open("contacts.txt", "r") as file:
                contacts = file.readlines()
                found = False
                for contact in contacts:
                    name, phone = contact.strip().split(",")
                    if name.lower() == search_name.lower():
                        print(f"Found: {name} - {phone}")
                        found = True
                        break
                if not found:
                    print("Contact not found.")
        except FileNotFoundError:
            print("No contacts found.")
            
    elif choice == '3':
        try:
            with open("contacts.txt", "r") as file:
                contacts = file.readlines()
                if contacts:
                    print("Your Contacts:")
                    for idx, contact in enumerate(contacts, start=1):
                        name, phone = contact.strip().split(",")
                        print(f"{idx}. {name} - {phone}")
                else:
                    print("No contacts found.")
        except FileNotFoundError:
            print("No contacts found.")
            
    elif choice == '4':
        delete_name = input("Enter the name of the contact to delete: ")
        try:
            with open("contacts.txt", "r") as file:
                contacts = file.readlines()
            with open("contacts.txt", "w") as file:
                deleted = False
                for contact in contacts:
                    name, phone = contact.strip().split(",")
                    if name.lower() != delete_name.lower():
                        file.write(contact)
                    else:
                        deleted = True
                if deleted:
                    print(f"Contact '{delete_name}' deleted successfully!")
                else:
                    print(f"Contact '{delete_name}' not found.")
        except FileNotFoundError:
            print("No contacts found.")
            
    elif choice == '5':
        print("Exiting the Contact Book. Goodbye!")
        break

    