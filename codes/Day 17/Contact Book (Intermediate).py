'''Task 2: Contact Book (Intermediate)
Objective

Build a phonebook application using JSON.

JSON Structure
[
    {
        "name": "Aman",
        "phone": "9876543210",
        "email": "aman@gmail.com"
    }
]
Features
Add Contact
Search Contact
Edit Contact
Delete Contact
Show All Contacts
Bonus Features
Search by phone number
Sort alphabetically
Export contacts to another JSON file'''

import json


def add_contact(name, phone, email):
    contact_data = {
        "name": name,
        "phone": phone,
        "email": email
    }
    
    try:
        with open('contacts.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    
    data.append(contact_data)
    
    with open('contacts.json', 'w') as file:
        json.dump(data, file, indent=4)
        
def view_all_contacts():
    try:
        with open('contacts.json', 'r') as file:
            data = json.load(file)
            for contact in data:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    except FileNotFoundError:
        print("No contacts found.")

def search_contact_by_name(name):
    try:
        with open('contacts.json', 'r') as file:
            data = json.load(file)
            for contact in data:
                if contact['name'].lower() == name.lower():
                    print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
                    return
            print("Contact not found.")
    except FileNotFoundError:
        print("No contacts found.")

def search_contact_by_phone(phone):
    try:
        with open('contacts.json', 'r') as file:
            data = json.load(file)
            for contact in data:
                if contact['phone'] == phone:
                    print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
                    return
            print("Contact not found.")
    except FileNotFoundError:
        print("No contacts found.")

def edit_contact(name, new_name=None, new_phone=None, new_email=None):
    try:
        with open('contacts.json', 'r') as file:
            data = json.load(file)
            for contact in data:
                if contact['name'].lower() == name.lower():
                    if new_name:
                        contact['name'] = new_name
                    if new_phone:
                        contact['phone'] = new_phone
                    if new_email:
                        contact['email'] = new_email
                    with open('contacts.json', 'w') as file:
                        json.dump(data, file, indent=4)
                    print("Contact updated.")
                    return
            print("Contact not found.")
    except FileNotFoundError:
        print("No contacts found.")

def delete_contact(name):
    try:
        with open('contacts.json', 'r') as file:
            data = json.load(file)
            for i, contact in enumerate(data):
                if contact['name'].lower() == name.lower():
                    del data[i]
                    with open('contacts.json', 'w') as file:
                        json.dump(data, file, indent=4)
                    print("Contact deleted.")
                    return
            print("Contact not found.")
    except FileNotFoundError:
        print("No contacts found.")

