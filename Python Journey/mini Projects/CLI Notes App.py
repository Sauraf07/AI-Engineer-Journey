FileName = "notes.txt"

# Add Note
def add_note():
    note = input("Enter a note: ")
    try:
        with open(FileName, "a") as file:
            file.write(note + "\n")
        print("Note saved successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

# View Notes
def view_notes():
    try:
        with open(FileName, "r") as file:
            notes = file.readlines()
            if notes:
                print("Your Notes:")
                for note in notes:
                    print(note.strip())
            else:
                print("No notes found.")
    except FileNotFoundError:
        print("No notes found. Please add a note first.")
    except Exception as e:
        print(f"An error occurred: {e}")    

# Main Menu
def main():
    while True:
        print("\nCLI Notes App")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_note()
        elif choice == '2':
            view_notes()
        elif choice == '3':
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
    