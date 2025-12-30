import os
TASKS_FILE = "tasks.txt"

def load_tasks():
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                done_flag, description = line.split(";", 1)
                tasks.append({
                    "description": description,
                    "done": done_flag == "1"
                })
    return tasks


def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        for task in tasks:
            done_flag = "1" if task["done"] else "0"
            f.write(f"{done_flag};{task['description']}\n")


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
    if not tasks:
        print("No tasks to delete.\n")
        return

    show_tasks(tasks)
    choice = input("Enter the number of the task to delete: ").strip()
    if not choice.isdigit():
        print("Please enter a valid number.\n")
        return

    index = int(choice) - 1
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"Deleted task: {removed['description']}\n")
    else:
        print("Task number out of range.\n")


def main():
    print("Simple To-Do List")
    print("-----------------\n")

    tasks = load_tasks()

    while True:
        print("Choose an option:")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Mark a task as done")
        print("4. Delete a task")
        print("5. Save and exit")

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
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.\n")


if __name__ == "__main__":
    main()
