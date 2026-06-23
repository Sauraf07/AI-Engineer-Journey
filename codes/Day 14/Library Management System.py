'''Task 4: Library Management System
Objective

Combine all OOP concepts

Requirements

Classes:

Library
Book
User
Student
Teacher
Features
Add Book
Issue Book
Return Book
Search Book'''

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_issued = False

    def get_details(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Issued: {self.is_issued}"
    
class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def get_details(self):
        return f"Name: {self.name}, User ID: {self.user_id}"
    
class Student(User):
    def __init__(self, name, user_id, grade):
        super().__init__(name, user_id)
        self.grade = grade

    def get_details(self):
        base_details = super().get_details()
        return f"{base_details}, Grade: {self.grade}"
    
class Teacher(User):
    def __init__(self, name, user_id, subject):
        super().__init__(name, user_id)
        self.subject = subject

    def get_details(self):
        base_details = super().get_details()
        return f"{base_details}, Subject: {self.subject}"

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def issue_book(self, book, user):
        if book in self.books and not book.is_issued:
            book.is_issued = True
            print(f"Book '{book.title}' issued to {user.name}.")
        else:
            print(f"Book '{book.title}' is not available for issue.")

    def return_book(self, book):
        if book in self.books and book.is_issued:
            book.is_issued = False
            print(f"Book '{book.title}' returned to the library.")
        else:
            print(f"Book '{book.title}' was not issued.")

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book.get_details()
        return "Book not found."

# Example usage
if __name__ == "__main__":
    library = Library()

    # Adding books
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084")
    library.add_book(book1)
    library.add_book(book2)

    # Adding users
    student = Student("Alice", 1, "10th Grade")
    teacher = Teacher("Mr. Smith", 2, "Mathematics")
    library.users.append(student)
    library.users.append(teacher)

    # Issuing a book
    library.issue_book(book1, student)

    # Searching for a book
    print(library.search_book("The Great Gatsby"))

    # Returning a book
    library.return_book(book1)
    