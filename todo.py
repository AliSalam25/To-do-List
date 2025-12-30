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
    pass


def delete_task(tasks):
    pass