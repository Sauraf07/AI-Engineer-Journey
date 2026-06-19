'''Task 4: Reverse a String Using Recursion
Objective

Practice recursive thinking with strings.

Problem

Reverse a string without using loops.'''
def reverse_string(s):
    # Base case: if the string is empty or has one character, return it
    if len(s) <= 1:
        return s
    else:
        # Recursive case: last character + reverse of the substring excluding the last character
        return s[-1] + reverse_string(s[:-1])
    
# Example usage
string = "Hello, World!"
result = reverse_string(string)
print(f"The reverse of '{string}' is: '{result}'")