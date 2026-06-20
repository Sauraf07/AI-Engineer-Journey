'''Task 4: File Reader
Requirements

Ask user for filename.

Try to open file.

Handle:

FileNotFoundError
PermissionError'''
def read_file():
    while True:
        try:
            filename = input("Enter the filename to read: ")
            with open(filename, 'r') as file:
                content = file.read()
                print(f"File content:\n{content}")
            break
        except FileNotFoundError:
            print("File not found. Please check the filename and try again.")
        except PermissionError:
            print("Permission denied. You do not have access to this file. Please try another file.")

if __name__ == "__main__":
    read_file()