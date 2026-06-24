'''Task 4: To-Do List Application
Objective

Build a file-based task manager.

Features
1. Add Task
2. View Tasks
3. Mark Complete
4. Exit
Example File
Buy Groceries
Learn Python
Build Project
Bonus

Store completed tasks in:

completed_tasks.txt
Concepts Used
Read
Write
Append'''

while True:
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Complete")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        task = input("Enter your task: ")
        with open("tasks.txt", "a") as file:
            file.write(task + "\n")
        print("Task added successfully!")
        
    elif choice == '2':
        try:
            with open("tasks.txt", "r") as file:
                tasks = file.readlines()
                if tasks:
                    print("Your Tasks:")
                    for idx, task in enumerate(tasks, start=1):
                        print(f"{idx}. {task.strip()}")
                else:
                    print("No tasks found.")
        except FileNotFoundError:
            print("No tasks found.")
            
    elif choice == '3':
        try:
            with open("tasks.txt", "r") as file:
                tasks = file.readlines()
                if tasks:
                    print("Your Tasks:")
                    for idx, task in enumerate(tasks, start=1):
                        print(f"{idx}. {task.strip()}")
                    task_number = int(input("Enter the task number to mark as complete: "))
                    if 1 <= task_number <= len(tasks):
                        completed_task = tasks.pop(task_number - 1).strip()
                        with open("tasks.txt", "w") as file:
                            file.writelines(tasks)
                        with open("completed_tasks.txt", "a") as file:
                            file.write(completed_task + "\n")
                        print(f"Task '{completed_task}' marked as complete!")
                    else:
                        print("Invalid task number.")
                else:
                    print("No tasks found.")
        except FileNotFoundError:
            print("No tasks found.")
            
    elif choice == '4':
        print("Exiting the To-Do List Application. Goodbye!")
        break

    