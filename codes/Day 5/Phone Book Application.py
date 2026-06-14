'''Task 2: Phone Book Application (Easy-Medium)
Objective

Create a simple phone book using dictionaries.'''
phone_book = {
    'John Doe': '123-456-7890',
    'Jane Smith': '987-654-3210',
    'Alice Johnson': '555-123-4567'

}
print("Phone Book:")
for name,number in phone_book.items():
    print(f"{name}: {number}")