tasks = []

while True:
    print("\n--- TO-DO LIST ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        if not tasks:
            print("No tasks yet.")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == "2":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "3":
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

        remove = int(input("Task number to remove: "))
        tasks.pop(remove - 1)
        print("Task removed!")

    elif choice == "4":
        break

    else:
        print("Invalid option")
