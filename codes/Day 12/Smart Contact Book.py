'''Bonus Challenge (Mini Project)
Smart Contact Book

Features:

Add Contact
Search Contact
Delete Contact

Handle Errors:

Empty name
Duplicate contact
Contact not found
Invalid menu choice'''
class ContactBook:
    def __init__(self):
        self.contacts = {}
    def add_contact(self, name, phone):
        if not name:
            raise ValueError("Contact name cannot be empty.")
        if name in self.contacts:
            raise ValueError("Contact already exists.")
        self.contacts[name] = phone
        print(f"Contact '{name}' added successfully.")
    def search_contact(self, name):
        if name not in self.contacts:
            raise ValueError("Contact not found.")
        print(f"Contact '{name}': {self.contacts[name]}")
    def delete_contact(self, name):
        if name not in self.contacts:
            raise ValueError("Contact not found.")
        del self.contacts[name]
        print(f"Contact '{name}' deleted successfully.")
def main():
    contact_book = ContactBook()
    while True:
        print("\nSmart Contact Book")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. Exit")
        choice = input("Enter your choice: ")
        try:
            if choice == '1':
                name = input("Enter contact name: ")
                phone = input("Enter contact phone number: ")
                contact_book.add_contact(name, phone)
            elif choice == '2':
                name = input("Enter contact name to search: ")
                contact_book.search_contact(name)
            elif choice == '3':
                name = input("Enter contact name to delete: ")
                contact_book.delete_contact(name)
            elif choice == '4':
                print("Exiting Smart Contact Book. Goodbye!")
                break
            else:
                raise ValueError("Invalid menu choice.")
        except ValueError as ve:
            print(f"Error: {ve}. Please try again.")
if __name__ == "__main__":
    main()