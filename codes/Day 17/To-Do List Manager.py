'''Task 3: To-Do List Manager ⭐⭐
Objective

Build a task management application.

JSON Structure
[
    {
        "id": 1,
        "task": "Learn JSON",
        "completed": false
    }
]
Features
Add Task
Mark as Completed
Delete Task
Update Task
Show Pending Tasks
Show Completed Tasks
Bonus
Add due date
Filter tasks
Count completed tasks'''

import json

def add_task(task_id, task_description):
    task_data = {
        "id": task_id,
        "task": task_description,
        "completed": False
    }
    
    try:
        with open('tasks.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    
    data.append(task_data)
    
    with open('tasks.json', 'w') as file:
        json.dump(data, file, indent=4)

def view_all_tasks():
    try:
        with open('tasks.json', 'r') as file:
            data = json.load(file)
            for task in data:
                status = "Completed" if task['completed'] else "Pending"
                print(f"ID: {task['id']}, Task: {task['task']}, Status: {status}")
    except FileNotFoundError:
        print("No tasks found.")

def mark_task_completed(task_id):
    try:
        with open('tasks.json', 'r') as file:
            data = json.load(file)
            for task in data:
                if task['id'] == task_id:
                    task['completed'] = True
                    break
        with open('tasks.json', 'w') as file:
            json.dump(data, file, indent=4)
    except FileNotFoundError:
        print("No tasks found.")
    
def delete_task(task_id):
    try:
        with open('tasks.json', 'r') as file:
            data = json.load(file)
            data = [task for task in data if task['id'] != task_id]
        with open('tasks.json', 'w') as file:
            json.dump(data, file, indent=4)
    except FileNotFoundError:
        print("No tasks found.")

def update_task(task_id, new_description=None):
    try:
        with open('tasks.json', 'r') as file:
            data = json.load(file)
            for task in data:
                if task['id'] == task_id:
                    if new_description:
                        task['task'] = new_description
                    break
        with open('tasks.json', 'w') as file:
            json.dump(data, file, indent=4)
    except FileNotFoundError:
        print("No tasks found.")

def show_pending_tasks():
    try:
        with open('tasks.json', 'r') as file:
            data = json.load(file)
            pending_tasks = [task for task in data if not task['completed']]
            for task in pending_tasks:
                print(f"ID: {task['id']}, Task: {task['task']}")
    except FileNotFoundError:
        print("No tasks found.")

def show_completed_tasks():
    try:
        with open('tasks.json', 'r') as file:
            data = json.load(file)
            completed_tasks = [task for task in data if task['completed']]
            for task in completed_tasks:
                print(f"ID: {task['id']}, Task: {task['task']}")
    except FileNotFoundError:
        print("No tasks found.")

def main():
    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Update Task")
        print("6. Show Pending Tasks")
        print("7. Show Completed Tasks")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task_id = int(input("Enter task ID: "))
            task_description = input("Enter task description: ")
            add_task(task_id, task_description)
        elif choice == '2':
            view_all_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID to mark as completed: "))
            mark_task_completed(task_id)
        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == '5':
            task_id = int(input("Enter task ID to update: "))
            new_description = input("Enter new task description (leave blank to keep unchanged): ")
            update_task(task_id, new_description if new_description else None)
        elif choice == '6':
            show_pending_tasks()
        elif choice == '7':
            show_completed_tasks()
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    