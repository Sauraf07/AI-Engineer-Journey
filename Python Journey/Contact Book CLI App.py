contact = {}
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    contact[name] = {"phone": phone, "email": email}
    print("Contact added successfully!")

def view_contacts():
    if not contact:
        print("No contacts found.")
    else:
        for name, details in contact.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")
            
def search_contact():
    name = input("Enter contact name to search: ")
    if name in contact:
        details = contact[name]
        print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter contact name to delete: ")
    if name in contact:
        del contact[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")
    
def search_contact():
    name = input("Enter contact name to search: ")
    if name in contact:
        details = contact[name]
        print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\nContact Book CLI App")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()
