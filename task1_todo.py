todo_list = []
def show_menu():
    print("\n---To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
while True:
    show_menu()
    choice = input("Enter choice:")
    if choice == "1":
        task = input("Enter a new task:")
        todo_list.append(task)
        print("Task added.")
    elif choice == "2":
        print("\nyour tasks:")
        for i, t in enumerate(todo_list, 1):
            print(f"{i}. {t}")
    elif choice == "3":
        num = int(input("Enter task number to remove:"))
        if 0 < num <= len(todo_list):
            removed = todo_list.pop(num-1)
            print(f"Removed task: {removed}")
        else:
            print("Invalid task number.")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")                 
