tasks = []

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added")

def view_tasks():
    if not tasks:
        print("No tasks")
        return
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def delete_task():
    view_tasks()
    if not tasks:
        return
    num = int(input("Enter task number to delete: "))
    if 1 <= num <= len(tasks):
        removed = tasks.pop(num-1)
        print(f"Removed: {removed}")
    else:
        print("Invalid number")

while True:
    print("\n1.Add Task 2.View Tasks 3.Delete Task 4.Exit")
    choice = input("Choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        break
    else:
        print("Invalid choice")