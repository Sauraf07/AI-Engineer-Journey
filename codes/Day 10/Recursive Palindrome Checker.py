'''Bonus Challenge (Interview Level)
Task 6: Recursive Palindrome Checker
Problem

Check if a string is palindrome using recursion.'''
def is_palindrome(s):
    # Base case: if the string is empty or has one character, it's a palindrome
    if len(s) <= 1:
        return True
    else:
        # Recursive case: check if the first and last characters are the same
        if s[0] == s[-1]:
            # Check the substring excluding the first and last characters
            return is_palindrome(s[1:-1])
        else:
            return False
        
# Example usage
string = "racecar"
result = is_palindrome(string)
if result:
    print(f"'{string}' is a palindrome.")
else:
    print(f"'{string}' is not a palindrome.")

    