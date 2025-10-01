from tasks.add_task import add_task
from tasks.view_tasks import view_tasks
from tasks.update_task import update_task
from tasks.mark_done import mark_done
from tasks.delete_task import delete_task
tasks = []
def menu():
    while True:
        print("\n===== To-Do List Application =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark Task as Done")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            mark_done(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            print("Exiting program... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
