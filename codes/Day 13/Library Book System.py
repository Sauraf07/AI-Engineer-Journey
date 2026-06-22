'''Task 4: Library Book System
Requirements

Create a Book class.

Attributes
title
author
price
Methods
display_book()
apply_discount(percent)'''
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_book(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price}")

    def apply_discount(self, percent):
        if 0 < percent < 100:
            discount_amount = self.price * (percent / 100)
            self.price -= discount_amount
            print(f"Discount of {percent}% applied. New price: ${self.price}")
        else:
            print("Invalid discount percentage. Must be between 0 and 100.")
# Example usage
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 20)
book1.display_book()
book1.apply_discount(10)
book1.display_book()
