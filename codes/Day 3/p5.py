# Task 5: Palindrome Checker
def is_palindrome(s):
    s = s.replace(" ", "").lower()  # Remove spaces and convert to lowercase
    return s == s[::-1]  # Check if the string is the same as its reverse
input_string = input("Enter a string to check if it's a palindrome: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:    print("The string is not a palindrome.")   
