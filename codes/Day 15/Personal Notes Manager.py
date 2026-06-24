'''Task 1: Personal Notes Manager
Objective

Learn basic file operations.

Features
Add Note
View Notes
Delete All Notes
Example
1. Add Note
2. View Notes
3. Delete Notes
4. Exit
Concepts Used
open()
write()
read()
file modes
with open("notes.txt", "a") as file:
    file.write(note + "\n")
Learning Outcome
File creation
File writing
File reading'''

while True:
    print("1. Add Note")
    print("2. View Notes")
    print("3. Delete Notes")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        note = input("Enter your note: ")
        with open("notes.txt", "a") as file:
            file.write(note + "\n")
        print("Note added successfully!")
        
    elif choice == '2':
        try:
            with open("notes.txt", "r") as file:
                notes = file.readlines()
                if notes:
                    print("Your Notes:")
                    for idx, note in enumerate(notes, start=1):
                        print(f"{idx}. {note.strip()}")
                else:
                    print("No notes found.")
        except FileNotFoundError:
            print("No notes found.")
            
    elif choice == '3':
        with open("notes.txt", "w") as file:
            pass  # This will clear the contents of the file
        print("All notes deleted successfully!")
        
    elif choice == '4':
        print("Exiting the Personal Notes Manager. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please try again.")

        