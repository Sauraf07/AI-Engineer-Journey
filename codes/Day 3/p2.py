'''Task 2: Email Username Extractor'''
email = input("Enter an email address: ")
email = email.strip()  # Remove leading and trailing whitespace
if '@' in email:
    username = email.split('@')[0]  # Extract the part before '@'
    print("Username:", username)
else:
    print("Invalid email address. Please include an '@' symbol.")