tasks = []  # Empty list to store tasks

while True:
    print("\n--- To-Do List APP ---")
    print("1. Add a new Task")
    print("2. View all Tasks")
    print("3. Delete a Task")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == '1':
        task = input("Enter a new task: ")
        tasks.append(task)
        print(f"'{task}' has been added to your list.")
    
    elif choice == '2':
        if tasks:
            print("\nYour Tasks:")
            for idx, task in enumerate(tasks, 1):
                print(f"{idx}. {task}")
    elif choice == '3':
        num = int(input("Enter the task number to delete: "))
        if 0 < num <= len(tasks):
            removed_task = tasks.pop(num - 1)
            print(f"'{removed_task}' has been deleted.")
        else:
            print("Invalid task number.")
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please enter 1-4.")