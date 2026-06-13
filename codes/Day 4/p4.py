# Task 4: To-Do List Manager (Medium)
'''Create an empty to-do list'''
todo_list = []
def add_task(task):
    todo_list.append(task)
def remove_task(task):
    if task in todo_list:
        todo_list.remove(task)
    else:
        print(f"{task} not found in to-do list.")
def show_tasks():
    print("To-Do List:")
    for task in todo_list:
        print(task)
def total_tasks():
    print("Total Number of Tasks:", len(todo_list))
# Example usage
add_task("Buy groceries")
add_task("Finish homework")
add_task("Call mom")
show_tasks()
total_tasks()
remove_task("Finish homework")
show_tasks()
total_tasks()

