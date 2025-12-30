def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet. Add your first one!\n")
        return

    print("\nYour tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "[x]" if task["done"] else "[ ]"
        print(f"{index}. {status} {task['description']}")
    print()


def add_task(tasks):
    description = input("Enter a new task: ").strip()
    if description:
        tasks.append({"description": description, "done": False})
        print("Task added.\n")
    else:
        print("Task description cannot be empty.\n")

def mark_done(tasks):
    if not tasks:
        print("No tasks to mark as done.\n")
        return

    show_tasks(tasks)
    choice = input("Enter the number of the task to mark as done: ").strip()
    if not choice.isdigit():
        print("Please enter a valid number.\n")
        return

    index = int(choice) - 1
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        print("Task marked as done.\n")
    else:
        print("Task number out of range.\n")


def delete_task(tasks):
    pass


def main():
    tasks = []
    print("Simple To-Do List")

    while True:
        print("Choose an option:")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Mark a task as done")
        print("4. Delete a task")
        print("5. Exit")

        choice = input("Enter 1-5: ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            break
        else:
            print("Invalid choice.\n")