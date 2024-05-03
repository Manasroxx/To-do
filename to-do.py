import datetime

def display_tasks(tasks):
    print("Your daily tasks:")
    if tasks:
        for i, (completed, task) in enumerate(tasks, 1):
            if completed:
                print(f"{i}. [x] {task}")
            else:
                print(f"{i}. [ ] {task}")
    else:
        print("No tasks for today.")

def add_tasks():
    new_tasks = input("Enter your tasks separated by commas: ").split(',')
    new_tasks = [(False, task.strip()) for task in new_tasks]
    return new_tasks

def mark_task_done(tasks):
    display_tasks(tasks)
    task_indexes = input("Enter the task numbers you want to mark as done separated by commas: ").split(',')
    task_indexes = [int(index.strip()) - 1 for index in task_indexes]
    for task_index in sorted(task_indexes, reverse=True):
        if 0 <= task_index < len(tasks):
            tasks[task_index] = (True, tasks[task_index][1])  # Mark task as done
            print(f"Task {task_index + 1} marked as done.")
        else:
            print(f"Invalid task number: {task_index + 1}")

def reset_tasks():
    confirm = input("Are you sure you want to reset all tasks? (y/n): ").lower()
    if confirm == "y":
        with open("tasks.txt", "w") as f:
            f.write("")
        print("All tasks have been reset.")
    else:
        print("Task reset aborted.")

def save_tasks(tasks):
    with open("tasks.txt", "w") as f:
        for completed, task in tasks:
            if completed:
                f.write("[x] " + task + "\n")
            else:
                f.write("[ ] " + task + "\n")

def main():
    current_date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    print(current_date_time)
    
    try:
        with open("tasks.txt", "r") as f:
            tasks = [(line.startswith("[x]"), line[4:].strip()) if line.startswith("[x]") else (False, line[4:].strip()) for line in f.readlines()]
    except FileNotFoundError:
        tasks = []

    display_tasks(tasks)

    while True:
        print("\n1. Add Tasks\n2. Mark Task as Done\n3. Reset Tasks\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            new_tasks = add_tasks()
            tasks.extend(new_tasks)
            save_tasks(tasks)
            print("Tasks added successfully.")
            display_tasks(tasks)
        elif choice == "2":
            mark_task_done(tasks)
            save_tasks(tasks)
            display_tasks(tasks)
        elif choice == "3":
            reset_tasks()
            tasks = []
            display_tasks(tasks)
        elif choice == "4":
            print("Exiting program.")
            save_tasks(tasks)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
